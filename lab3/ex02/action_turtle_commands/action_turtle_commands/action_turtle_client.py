import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from for_lab3_2.action import MessageTurtleCommands
import time

class ActionTurtleClient(Node):
    def __init__(self):
        super().__init__('action_turtle_client')
        self._action_client = ActionClient(self, MessageTurtleCommands, 'move_turtle')

    def send_goal(self, command, s, angle):
        goal_msg = MessageTurtleCommands.Goal()
        goal_msg.command = command
        goal_msg.s = s
        goal_msg.angle = angle

        #self._action_client.wait_for_server()
        return self._action_client.send_goal(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    action_turtle_client = ActionTurtleClient()

    #action_turtle_client.send_goal("forward", 2, 0)  # проехать вперед 2 метра
    #time.sleep(5)
    action_turtle_client.send_goal("turn", 90, 0)  # повернуть направо на 90 градусов
    action_turtle_client.get_logger().info("turn")
    time.sleep(5)
    action_turtle_client.send_goal("forward", 1, 0)  # проехать еще 1 метр
    action_turtle_client.get_logger().info("second")

    rclpy.spin(action_turtle_client)
    action_turtle_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
