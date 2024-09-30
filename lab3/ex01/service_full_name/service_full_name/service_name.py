import rclpy
from rclpy.node import Node
from ex09.srv import FullNameSumService

class FullNameService(Node):

    def __init__(self):
        super().__init__('service_name')
        self.srv = self.create_service(FullNameSumService, 'SummFullName', self.handle_service)

    def handle_service(self, request, response):
        response.full_name = f"{request.first_name} {request.name} {request.last_name}"
        self.get_logger().info(f"Request: {request.first_name} {request.name} {request.last_name}")
        self.get_logger().info(f"Sending back response: {response.full_name}")
        return response

def main(args=None):
    rclpy.init(args=args)
    full_name_service = FullNameService()
    rclpy.spin(full_name_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
