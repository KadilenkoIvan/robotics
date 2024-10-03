import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import StaticTransformBroadcaster

class StaticFramePublisher(Node):
    def __init__(self):
        super().__init__('static_frame_publisher')
        self.tf_static_broadcaster = StaticTransformBroadcaster(self)

        # Publish static transforms
        self.publish_static_transform('world', 'turtle1', 5, 5, 0)
        self.publish_static_transform('world', 'turtle2', 2, 2, 0)

    def publish_static_transform(self, parent_frame, child_frame, x, y, z):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = parent_frame
        t.child_frame_id = child_frame
        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = z
        t.transform.rotation.w = 1.0

        self.tf_static_broadcaster.sendTransform(t)

def main():
    rclpy.init()
    node = StaticFramePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
