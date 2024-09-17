import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class TextToCmdVel(Node):
    def __init__(self):
        super().__init__('text_to_cmd_vel')

        # Подписчик на топик "cmd_text"
        self.subscription = self.create_subscription(
            String,
            'cmd_text',
            self.listener_callback,
            10)
        
        # Публикация в топик "/turtle1/cmd_vel"
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def listener_callback(self, msg):
        command = msg.data.lower()
        twist = Twist()

        if command == 'move_forward':
            twist.linear.x = 1.0  # 1 м/с вперед
        elif command == 'move_backward':
            twist.linear.x = -1.0  # 1 м/с назад
        elif command == 'turn_left':
            twist.angular.z = 1.5  # 1.5 радиан/с поворот налево
        elif command == 'turn_right':
            twist.angular.z = -1.5  # 1.5 радиан/с поворот направо
        else:
            self.get_logger().info(f"Неизвестная команда: {command}")
            return

        # Публикация сообщения Twist
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = TextToCmdVel()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
