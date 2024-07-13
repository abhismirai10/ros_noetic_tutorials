cmake_minimum_required(VERSION 3.0.2)
project(seven_dof_arm_gazebo)

find_package(catkin REQUIRED COMPONENTS
  gazebo_msgs
  gazebo_plugins
  gazebo_ros
  gazebo_ros_control
  robot_description
)

# Install launch files
install(FILES
  launch/seven_dof_arm_world.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

catkin_package(
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

