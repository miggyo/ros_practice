import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import Int32
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_first_package_msgs.msg import CmdAndPoseVel

class TurtlesimSubscriber(Node):

    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription(Int32, '/quiz/turtle1/set_flag', self.callback_num_1, 10)
        # self.sub_pose = self.create_subscription(Pose, '/quiz/turtle1/pose', self.callback_pose, 10)
        # self.sub_cmdvel = self.create_subscription(Twist, '/quiz/turtle1/cmd_vel', self.callback_cmd, 10)
        # self.cmd_pose = CmdAndPoseVel()

        self.cmd_vel_publisher = self.create_publisher(Twist, '/quiz/turtle1/cmd_vel', 10)

    # def callback_pose(self, msg):
    #     self.cmd_pose.pose_x = msg.x
    #     self.cmd_pose.pose_y = msg.y
    #     self.cmd_pose.linear_vel = msg.linear_velocity
    #     self.cmd_pose.angular_vel = msg.angular_velocity
    #     print(self.cmd_pose)

    def callback_num_1(self, msg):
        # 1을 받았을 때 cmd_vel 메시지 발행
        if msg.data == 1:
            # cmd_vel 메시지 생성
            self.get_logger().info('I heard: "%d"' % msg.data)
            cmd_msg = Twist()
            cmd_msg.angular.z = 2.0

            linear_vel = 2.0  # 1초에 원의 둘레를 도는데 필요한 거리
        
            
            cmd_msg.linear.x = linear_vel
            
            self.cmd_vel_publisher.publish(cmd_msg)

    # def callback_cmd(self, msg):
    #     self.cmd_pose.cmd_vel_linear = msg.linear.x
    #     self.cmd_pose.cmd_vel_angular = msg.angular.y
    #     print(self.cmd_pose)

def main(args=None):
    rp.init(args=args)

    turtlesim_subscriber = TurtlesimSubscriber()
    rp.spin(turtlesim_subscriber)

    turtlesim_subscriber.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()