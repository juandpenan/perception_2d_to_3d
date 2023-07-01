# Copyright 2023 (c) StressOverflow
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():

    #
    # ARGS
    #
    camera_depth_info_topic = LaunchConfiguration("camera_depth_info_topic")
    camera_depth_info_topic_cmd = DeclareLaunchArgument(
        "camera_depth_info_topic",
        default_value="/camera/depth/camera_info",
        description="Name of the camera depth info topic")

    depth_image_raw_topic = LaunchConfiguration("depth_image_raw_topic")
    depth_image_raw_topic_cmd = DeclareLaunchArgument(
        "depth_image_raw_topic",
        default_value="/camera/depth/image_raw",
        description="Name of the camera depth image raw topic")

    detections_2d_topic = LaunchConfiguration("detections_2d_topic")
    detections_2d_topic_cmd = DeclareLaunchArgument(
        "detections_2d_topic",
        default_value="/yolo/detections",
        description="Name of the 2d detections topic")

    detections_3d_topic = LaunchConfiguration("detections_3d_topic")
    detections_3d_topic_cmd = DeclareLaunchArgument(
        "detections_3d_topic",
        default_value="/yolo/detections_3d",
        description="Name of the output 3d detections topic")

    #
    # NODES
    #
    detector_node_cmd = Node(
        package="perception_2d_to_3d",
        executable="detection_2d_to_3d_depth",
        name="detection_2d_to_3d_depth_node",
        output="screen",
        remappings=[
            ("camera_info", camera_depth_info_topic),
            ("input_depth", depth_image_raw_topic),
            ("input_detection_2d", detections_2d_topic),
            ("output_detection_3d", detections_3d_topic),
        ]
    )

    ld = LaunchDescription()

    ld.add_action(camera_depth_info_topic_cmd)
    ld.add_action(depth_image_raw_topic_cmd)
    ld.add_action(detections_2d_topic_cmd)
    ld.add_action(detections_3d_topic_cmd)

    ld.add_action(detector_node_cmd)

    return ld
