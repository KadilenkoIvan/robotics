import os
import subprocess
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('lab5_31')
    xacro_file = os.path.join(pkg_path, 'urdf', 'robot.urdf.xacro')
    urdf_file = os.path.join(pkg_path, 'urdf', 'robot.urdf')

    subprocess.run(['xacro', xacro_file, '-o', urdf_file], check=True)
    
    rviz_config_file = os.path.join(pkg_path, 'rviz', 'robot.rviz')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        )
    )
    
    # Robot State Publisher для публикации состояний робота из URDF
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': Command(['xacro ', xacro_file])}]
    )

    # Joint State Publisher GUI
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    #robot_state_publisher = Node(
    #    package='robot_state_publisher',
    #    executable='robot_state_publisher',
    #    output='screen',
    #    arguments=[xacro_file],
    #)

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'my_robot', '-file', urdf_file],
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher_node,
        spawn_entity,
        rviz_node,
        joint_state_publisher_gui_node,
    ])
