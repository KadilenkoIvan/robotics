import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class TurtleSpawner(Node):
    def __init__(self):
        super().__init__('turtle_spawner')
        self.spawn_client = self.create_client(Spawn, 'spawn')
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for spawn service...')
        self.spawn_turtle(4.0, 2.0, 0.0, 'turtle2')

    def spawn_turtle(self, x, y, theta, name):
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name
        future = self.spawn_client.call_async(request)
        future.add_done_callback(self.turtle_spawned)

    def turtle_spawned(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Successfully spawned {response.name}')
        except Exception as e:
            self.get_logger().error(f'Failed to spawn turtle: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
