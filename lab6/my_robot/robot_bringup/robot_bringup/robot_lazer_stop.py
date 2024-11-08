#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan  # Для обработки данных лидара
from geometry_msgs.msg import Twist    # Для публикации команд скорости
import math

class RobotControlNode(Node):
    def __init__(self):
        super().__init__('robot_control_node')

        # Подписка на данные лидара
        self.lidar_subscription = self.create_subscription(
            LaserScan,
            '/robot/scan',
            self.lidar_callback,
            10
        )

        # Публикация команд на управление движением робота
        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            '/robot/cmd_vel',
            10
        )

        # Установка начальных значений
        self.closest_distance = None  # Изначально данных нет
        self.safe_distance = 0.5  # Минимально безопасное расстояние в метрах
        self.front_cone_angle = 22.5  # Угол конуса впереди робота, градусов

        # Таймер для периодической проверки и публикации команд движения
        self.timer = self.create_timer(0.1, self.control_loop)

    def lidar_callback(self, msg: LaserScan):
        # Инициализируем значение для ближайшей точки внутри конуса
        self.closest_distance = float('inf')
        
        # Перебор точек лидара
        for i, range_distance in enumerate(msg.ranges):
            # Пропуск значений вне допустимого диапазона
            if range_distance < msg.range_min or range_distance > msg.range_max:
                continue

            # Угол текущего луча лидара (в градусах)
            angle = math.degrees(msg.angle_min + i * msg.angle_increment)

            # Проверка, находится ли точка внутри фронтального конуса
            if -self.front_cone_angle <= angle <= self.front_cone_angle:
                # Обновление минимального расстояния, если точка ближе
                if range_distance < self.closest_distance:
                    self.closest_distance = range_distance

        # Вывод минимального расстояния для отладки
        self.get_logger().info(f"Closest obstacle in front at: {self.closest_distance} meters")

    def control_loop(self):
        # Проверка, получены ли данные от лидара
        if self.closest_distance is None:
            self.get_logger().warn("No lidar data received yet.")
            return

        # Создание объекта Twist для управления движением
        twist = Twist()

        # Если ближайшее препятствие внутри фронтального конуса на расстоянии меньше безопасного
        if self.closest_distance < self.safe_distance:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.get_logger().info("Obstacle detected in front! Stopping the robot.")
        else:
            twist.linear.x = 0.1  # Скорость движения вперёд
            twist.angular.z = 0.0
            self.get_logger().info("Path is clear. Moving forward.")

        # Публикация команды движения
        self.cmd_vel_publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    robot_control_node = RobotControlNode()

    try:
        rclpy.spin(robot_control_node)
    except KeyboardInterrupt:
        pass
    finally:
        robot_control_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
