import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import Int32

class TurtlesimSubscriber(Node):

    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/quiz/turtle1/set_flag',
            self.callback,
            10)
        self.subscription

    def callback(self,msg):
        self.get_logger().info('I heard: "%d"' % msg.data)

def main(args=None):
    rp.init(args=args)
    
    turtlesim_subscriber = TurtlesimSubscriber()
    rp.spin(turtlesim_subscriber)

    turtlesim_subscriber.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()