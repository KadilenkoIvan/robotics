import sys
import rclpy
from rclpy.node import Node
from ex09.srv import FullNameSumService

class FullNameClient(Node):

    def __init__(self):
        super().__init__('client_name')
        self.client = self.create_client(FullNameSumService, 'SummFullName')

    def send_request(self, first_name, name, last_name):
        request = FullNameSumService.Request()
        request.first_name = first_name
        request.name = name
        request.last_name = last_name

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.future = self.client.call_async(request)

def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 4:
        print("Usage: client_name first_name name last_name")
        return

    client = FullNameClient()
    client.send_request(sys.argv[1], sys.argv[2], sys.argv[3])

    rclpy.spin_until_future_complete(client, client.future)
    if client.future.result() is not None:
        response = client.future.result()
        client.get_logger().info(f"Full name: {response.full_name}")
    else:
        client.get_logger().error('Exception while calling service: %r' % (client.future.exception(),))

    rclpy.shutdown()

if __name__ == '__main__':
    main()

