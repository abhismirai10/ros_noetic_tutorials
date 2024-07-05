cmake_minimum_required(VERSION 3.0.2)
project(robot_description)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  rviz
  tf
  urdf
  xacro
)

# Install launch files
install(FILES
  launch/pan_tilt.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

catkin_package(

)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
