import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import sys

class MoveToGoal(Node):
    def __init__(self, x_goal, y_goal, theta_goal):
        super().__init__('move_to_goal')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = None

        self.x_goal = x_goal
        self.y_goal = y_goal
        self.theta_goal = theta_goal

        self.timer = self.create_timer(0.1, self.move_turtle)

    def pose_callback(self, msg):
        self.pose = msg

    def move_turtle(self):
        if self.pose is None:
            return

        angle_to_goal = math.atan2(self.y_goal - self.pose.y, self.x_goal - self.pose.x)

        twist = Twist()

        if abs(angle_to_goal - self.pose.theta) > 0.1:
            twist.angular.z = 1.0
        else:
            twist.linear.x = 1.0

        self.publisher_.publish(twist)

        # Остановка, когда близко к цели
        if abs(self.pose.x - self.x_goal) < 0.1 and abs(self.pose.y - self.y_goal) < 0.1:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.publisher_.publish(twist)
            self.get_logger().info('Reached the goal!')
            exit()

def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 4:
        print("Usage: ros2 run move_to_goal move_to_goal <x> <y> <theta>")
        return

    x_goal = float(sys.argv[1])
    y_goal = float(sys.argv[2])
    theta_goal = float(sys.argv[3])

    node = MoveToGoal(x_goal, y_goal, theta_goal)
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
