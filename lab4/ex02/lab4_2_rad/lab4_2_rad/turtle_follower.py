import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from tf2_ros import Buffer, TransformListener
import math

class TurtleFollower(Node):
    def __init__(self):
        super().__init__('turtle_follower')

        self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.1, self.follow_carrot)

    def follow_carrot(self):
        try:
            trans = self.tf_buffer.lookup_transform('turtle2', 'carrot', rclpy.time.Time())

            msg = Twist()
            msg.linear.x = 1.0 * math.sqrt(trans.transform.translation.x**2 + trans.transform.translation.y**2)
            msg.angular.z = 4.0 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)

            self.publisher.publish(msg)

        except Exception as e:
            self.get_logger().info(f'Error: {e}')

def main():
    rclpy.init()
    node = TurtleFollower()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
