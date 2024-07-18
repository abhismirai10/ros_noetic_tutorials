cmake_minimum_required(VERSION 3.0.2)
project(a05_seven_dof_arm)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  rviz
  tf
  urdf
  xacro

  gazebo_msgs
  gazebo_plugins
  gazebo_ros
  gazebo_ros_control
)

catkin_package(
  CATKIN_DEPENDS gazebo_ros
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

# Install launch files
install(FILES
  launch/seven_dof_arm.launch
  launch/seven_dof_arm_with_rgbd_gazebo.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)