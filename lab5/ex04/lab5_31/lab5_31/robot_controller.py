import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64  # Импортируем тип сообщения для управления колесами

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # Подписка на топик /cmd_vel
        self.cmd_vel_subscriber = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )

        # Публикация на топики для управления колесами
        self.left_front_wheel_pub = self.create_publisher(Float64, '/left_front_wheel_joint/command', 10)
        self.right_front_wheel_pub = self.create_publisher(Float64, '/right_front_wheel_joint/command', 10)
        self.left_back_wheel_pub = self.create_publisher(Float64, '/left_back_wheel_joint/command', 10)
        self.right_back_wheel_pub = self.create_publisher(Float64, '/right_back_wheel_joint/command', 10)

        self.get_logger().info("Robot Controller is ready to receive commands on /cmd_vel")

    def cmd_vel_callback(self, msg):
        linear_x = msg.linear.x  # Линейная скорость
        angular_z = msg.angular.z  # Угловая скорость

        # Размеры робота
        wheel_base = 1.0  # Расстояние между колесами (должно соответствовать реальному расстоянию в метрах)
        wheel_radius = 0.3  # Радиус колеса (должен соответствовать реальному радиусу в метрах)

        # Расчет скорости для каждого колеса
        left_front_speed = (linear_x - angular_z * wheel_base / 2) / wheel_radius
        right_front_speed = (linear_x + angular_z * wheel_base / 2) / wheel_radius
        left_back_speed = (linear_x - angular_z * wheel_base / 2) / wheel_radius
        right_back_speed = (linear_x + angular_z * wheel_base / 2) / wheel_radius

        # Логирование
        self.get_logger().info(f"Calculated wheel speeds: LF={left_front_speed}, RF={right_front_speed}, LB={left_back_speed}, RB={right_back_speed}")

        # Публикация скоростей на соответствующие топики
        self.left_front_wheel_pub.publish(Float64(data=left_front_speed))
        self.right_front_wheel_pub.publish(Float64(data=right_front_speed))
        self.left_back_wheel_pub.publish(Float64(data=left_back_speed))
        self.right_back_wheel_pub.publish(Float64(data=right_back_speed))

def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    rclpy.spin(robot_controller)
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
