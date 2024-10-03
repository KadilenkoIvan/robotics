import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from for_lab3_2.action import MessageTurtleCommands

# Глобальный список сообщений для отправки команд черепахе
pending_commands = []

class TurtleActionClient(Node):
    def __init__(self):
        super().__init__('action_client')
        self._action_client = ActionClient(self, MessageTurtleCommands, 'move_turtle')

    def send_command(self, command, distance, angle):
        # Формирование сообщения с целью
        msg = MessageTurtleCommands.Goal()
        msg.command = command
        msg.s = distance
        msg.angle = angle

        # Ожидание готовности сервера
        self._action_client.wait_for_server()
        # Асинхронная отправка цели
        self._goal_future = self._action_client.send_goal_async(msg, feedback_callback=self.on_feedback)
        self._goal_future.add_done_callback(self.on_goal_response)

    def on_goal_response(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Цель отклонена сервером')
            return

        self.get_logger().info('Цель принята сервером')

        # Получение результата асинхронно
        self._result_future = goal_handle.get_result_async()
        self._result_future.add_done_callback(self.on_result)

    def on_result(self, future):
        result = future.result().result
        self.get_logger().info(f'Результат выполнения: {result.result}')

        # Удаление выполненной команды и отправка следующей
        global pending_commands
        pending_commands.pop(0)

        if pending_commands:
            self.send_command(*pending_commands[0])
        else:
            rclpy.shutdown()

    def on_feedback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Обратная связь: {feedback}')


def main(args=None):
    rclpy.init(args=args)
    turtle_client = TurtleActionClient()

    # Заполнение списка команд для выполнения
    global pending_commands
    pending_commands = [
        ['forward', 2, 0],
        ['turn_right', 0, 90],
        ['forward', 1, 0]
    ]

    # Отправка первой команды
    turtle_client.send_command(*pending_commands[0])

    rclpy.spin(turtle_client)


if __name__ == '__main__':
    main()
