import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import Int32
from turtlesim.msg import Pose

class TurtlesimPenController(Node):

    def __init__(self):
        super().__init__('turtlesim_pen_controller')
        self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
        self.pub_pen = self.create_publisher(Int32, '/turtle1/set_pen', 10)
        self.timer = self.create_timer(5.0, self.timer_callback)  # 5초에 한 번씩 타이머 콜백 호출
        self.last_x = 0.0  # 초기화

    def callback_pose(self, msg):
        color_msg = Int32()

        if msg.x < 5:
            color_msg.data = 2  # Red color
        else:
            color_msg.data = 0  # Black color

        self.pub_pen.publish(color_msg)
        self.last_x = msg.x  # 터틀의 x 좌표 저장

    def timer_callback(self):
        # 터틀의 x 좌표를 5초에 한 번씩 출력
        self.get_logger().info("Turtle's x coordinate: %f", self.last_x)

def main(args=None):
    rp.init(args=args)

    pen_controller = TurtlesimPenController()
    rp.spin(pen_controller)

    pen_controller.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
