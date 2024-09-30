import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from for_lab3_2.action import MessageTurtleCommands
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class ActionTurtleServer(Node):
    def __init__(self):
        super().__init__('action_turtle_server')
        
        # Инициализация атрибута current_pose
        self.current_pose = None
        
        self._action_server = ActionServer(
            self,
            MessageTurtleCommands,
            'move_turtle',
            self.execute_callback)
        
        # Публикация команд движения
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        
        # Подписка на топик /turtle1/pose
        self.pose_subscription = self.create_subscription(
            Pose, 'turtle1/pose', self.pose_callback, 10)

        self.get_logger().info("Action Turtle Server started")

    def pose_callback(self, msg):
        """Callback для обновления текущей позиции черепахи."""
        self.current_pose = msg
        self.get_logger().info(f"Текущая позиция: x={msg.x}, y={msg.y}, theta={msg.theta}")

    def execute_callback(self, goal_handle):
        goal = goal_handle.request
        feedback_msg = MessageTurtleCommands.Feedback()

        if goal.command == "forward":
            distance = goal.s
            self.move_forward(distance, feedback_msg)
        elif goal.command == "turn_left":
            angle = goal.angle
            self.turn(-angle, feedback_msg)
        elif goal.command == "turn_right":
            angle = goal.angle
            self.turn(angle, feedback_msg)

        goal_handle.succeed()
        result = MessageTurtleCommands.Result()
        result.result = True
        return result

    def move_forward(self, distance, feedback_msg):
        if not self.current_pose:
            return False  # Если нет данных о позиции, движение невозможно

        start_x = self.current_pose.x
        start_y = self.current_pose.y

        vel_msg = Twist()
        vel_msg.linear.x = 1.0
        vel_msg.angular.z = 0.0

        self.publisher_.publish(vel_msg)

        while True:
            # Рассчитываем пройденное расстояние
            current_distance = math.sqrt(
                (self.current_pose.x - start_x)**2 + (self.current_pose.y - start_y)**2)

            feedback_msg.odom = int(current_distance)
            if current_distance >= distance:
                break

            self.publisher_.publish(vel_msg)
            rclpy.spin_once(self)

        # Остановить черепаху после достижения цели
        vel_msg.linear.x = 0.0
        self.publisher_.publish(vel_msg)
        return True

    def turn(self, angle, feedback_msg):
        if not self.current_pose:
            return False  # Если нет данных о позиции, поворот невозможен

        target_theta = self.current_pose.theta + math.radians(angle)
        vel_msg = Twist()
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 1.0 if angle > 0 else -1.0

        self.publisher_.publish(vel_msg)

        while True:
            current_angle = self.current_pose.theta
            if abs(current_angle - target_theta) < 0.05:  # Допускаем небольшую погрешность
                break

            self.publisher_.publish(vel_msg)
            rclpy.spin_once(self)

        # Остановить черепаху после поворота
        vel_msg.angular.z = 0.0
        self.publisher_.publish(vel_msg)
        return True

def main(args=None):
    rclpy.init(args=args)
    action_turtle_server = ActionTurtleServer()
    rclpy.spin(action_turtle_server)
    #action_turtle_server.destroy_node()
    #rclpy.shutdown()

if __name__ == '__main__':
    main()
