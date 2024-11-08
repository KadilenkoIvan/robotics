#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2  # Для обработки данных с камеры глубины
from geometry_msgs.msg import Twist
import sensor_msgs_py.point_cloud2 as pc2  # Для преобразования PointCloud2 в список
import math
import numpy as np

class RobotControlNode(Node):
    def __init__(self):
        super().__init__('robot_control_node')

        # Подписка на данные с камеры глубины
        self.depth_subscription = self.create_subscription(
            PointCloud2,
            '/depth/points',
            self.depth_callback,
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
        self.height_threshold = 0.25  # Порог для высоты точки (в метрах)

        # Таймер для периодической проверки и публикации команд движения
        self.timer = self.create_timer(0.1, self.control_loop)

    def depth_callback(self, msg: PointCloud2):
        # Преобразование PointCloud2 в список точек (x, y, z)
        point_cloud = pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)
        
        # Инициализируем минимальное расстояние
        self.closest_distance = float('inf')

        # Преобразуем в массив numpy для более удобной обработки
        point_array = np.array(list(point_cloud))

        # Проверяем каждую точку в облаке и вычисляем минимальное расстояние
        for point in point_array:
            x, y, z = point
            distance = math.sqrt(x**2 + y**2 + z**2)  # Расстояние от камеры до точки

            # Фильтрация точек по высоте (игнорируем точки, которые на уровне пола)
            if abs(z) < self.height_threshold:  # Проверяем, что точка не слишком близка к полу
                continue

            # Вычисляем угол этой точки относительно робота
            angle = math.degrees(math.atan2(y, x))  # Угол в градусах

            # Проверка, находится ли точка в переднем конусе
            if -self.front_cone_angle <= angle <= self.front_cone_angle:
                # Обновляем минимальное расстояние
                if distance < self.closest_distance:
                    self.closest_distance = distance

        # Вывод минимального расстояния для отладки
        self.get_logger().info(f"Closest obstacle in front at: {self.closest_distance} meters")

    def control_loop(self):
        # Проверка, получены ли данные от камеры глубины
        if self.closest_distance is None:
            self.get_logger().warn("No depth data received yet.")
            return

        # Создание объекта Twist для управления движением
        twist = Twist()

        # Если ближайшее препятствие внутри фронтального конуса на расстоянии меньше безопасного
        if self.closest_distance < self.safe_distance or self.closest_distance == float('inf'):
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
