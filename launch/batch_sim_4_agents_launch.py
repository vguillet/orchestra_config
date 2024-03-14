from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

from maaf_allocation_node.node_config import *


def generate_launch_description():
    nodes = []

    # # -> Add the GraphEnvView node
    # nodes.append(
    #     Node(
    #         package="controller_graph",
    #         executable="controller_graph",
    #         name="controller_graph",
    #         output="screen",
    #         parameters=[
    #             {"agent_id": "0"},
    #             {"env_type": "graph"}
    #         ]
    #     )
    # )

    # > Declare scenario config launch argument
    nodes.append(
        DeclareLaunchArgument(
            'scenario_id',
            default_value='free_scenario',
            description='The scenario configuration to use for the simulation'
        )
    )

    data_path_arg = DeclareLaunchArgument(
        'data_path',
        default_value='/my/data/path'
    )

    scenario_id_value = LaunchConfiguration('scenario_id')
    data_path_value = LaunchConfiguration('data_path')

    nodes.append(
        ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '-a', '-o', scenario_id_value],
            output='screen'
        )
    )

    # -> Add the RLB_simple_sim node with arguments
    nodes.append(
        Node(
            package="rlb_simple_sim",
            executable="rlb_simple_sim",
            name="rlb_simple_sim",
            output="screen",
            parameters=[{
                "scenario_id": LaunchConfiguration("scenario_id"),
            }]
        )
    )

    # -> Add the controller_graph node
    nodes.append(
        Node(
            package="controller_graph",
            executable="controller_graph",
            name="controller_graph",
            output="screen"
        )
    )

    # -> Add the maaf_allocation_node launcher
    nodes.append(
        IncludeLaunchDescription(
            launch_description_source=[get_package_share_directory('maaf_allocation_node'), '/maaf_4_launch.py'],
            launch_arguments={'scenario_id': scenario_id_value}.items()
        )
    )

    # -> Add the mbawi_sim node
    nodes.append(
        Node(
            package="mbawi_sim",
            executable="mbawi_sim",
            name="mbawi_sim",
            output="log"
        )
    )

    return LaunchDescription(nodes)
