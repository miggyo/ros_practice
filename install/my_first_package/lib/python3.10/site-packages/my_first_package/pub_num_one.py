import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import Int32


class TurtlesimPublisher(Node):

    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Int32, '/quiz/turtle1/set_flag', 10) 
        timer_period = 5  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = 1
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)


def main(args=None):
    rp.init(args=args)

    turtlesim_publisher = TurtlesimPublisher()
    rp.spin(turtlesim_publisher)

    turtlesim_publisher.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()