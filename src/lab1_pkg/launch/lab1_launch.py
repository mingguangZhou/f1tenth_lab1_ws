from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Node for the talker with parameters
    talker_node = Node(
        package='lab1_pkg',
        executable='talker.py',
        name='talker',
        output='screen',
        parameters=[
            {'v': 1.0},
            {'d': 2.0}
        ]
    )

    # Node for the relay
    relay_node = Node(
        package='lab1_pkg',
        executable='relay',
        name='relay',
        output='screen'
    )

    # Create and return launch description
    return LaunchDescription([
        talker_node,
        relay_node
    ])
