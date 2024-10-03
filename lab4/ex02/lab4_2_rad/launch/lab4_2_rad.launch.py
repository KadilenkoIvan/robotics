from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        # Аргументы для задания радиуса и направления вращения
        DeclareLaunchArgument(
            'radius',
            default_value='1.0',
            description='Радиус вращения фрейма морковки'
        ),
        DeclareLaunchArgument(
            'direction_of_rotation',
            default_value='1',
            description='Направление вращения фрейма морковки (1 - по часовой стрелке, -1 - против)'
        ),
        
        # Запуск симуляции turtlesim
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # Управление первой черепашкой с клавиатуры
        #Node(
        #    package='turtlesim',
        #    executable='turtle_teleop_key',
        #    name='teleop_turtle1',
        #),
        
        # Спавн второй черепашки
        Node(
            package='lab4_2_rad',
            executable='turtle_spawner',
            name='turtle_spawner',
            output='screen'
        ),

        # Статический транслятор фрейма для первой черепашки
        Node(
            package='lab4_2_rad',
            executable='static_broadcaster',
            name='static_broadcaster',
            output='screen',
            arguments=['turtle1']
        ),

        # Транслятор фрейма морковки
        Node(
            package='lab4_2_rad',
            executable='carrot_broadcaster',
            name='carrot_broadcaster',
            output='screen',
            parameters=[{
                'radius': LaunchConfiguration('radius'),
                'direction_of_rotation': LaunchConfiguration('direction_of_rotation')
            }]
        ),

        # Фолловер второй черепашки за морковкой
        Node(
            package='lab4_2_rad',
            executable='turtle_follower',
            name='turtle_follower',
            output='screen'
        )
    ])

