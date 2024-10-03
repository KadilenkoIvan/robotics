import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class CarrotFramePublisher(Node):
    def __init__(self):
        super().__init__('carrot_frame_publisher')

        # ПАРАМЕТРЫ
        self.declare_parameter('radius', 1.0)
        self.declare_parameter('direction_of_rotation', 1)

        self.radius = self.get_parameter('radius').get_parameter_value().double_value
        self.direction = self.get_parameter('direction_of_rotation').get_parameter_value().integer_value

        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_carrot_frame)
        self.angle = 0.0

    def broadcast_carrot_frame(self):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'turtle1'
        t.child_frame_id = 'carrot'

        # МОРКОВЬ
        t.transform.translation.x = self.radius * math.cos(self.angle)
        t.transform.translation.y = self.radius * math.sin(self.angle)
        t.transform.translation.z = 0.0

        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)

        self.angle -= 0.1 * self.direction

def main():
    rclpy.init()
    node = CarrotFramePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
