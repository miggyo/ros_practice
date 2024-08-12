from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                namespace='quiz', name='num_1_publisher',package='my_first_package',
                executable='pub_num_one', output= 'screen'),
            Node(
                namespace='quiz', name='num_1_subscribe',package='my_first_package',
                executable='subscribe_num_one', output= 'screen'),
            Node(
                namespace='quiz',name='turtlesim',package='turtlesim',
                executable='turtlesim_node', output='screen'),
        ]
    )