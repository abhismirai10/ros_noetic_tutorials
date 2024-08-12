cmake_minimum_required(VERSION 3.0.2)
project(a06_new_action)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  actionlib
  actionlib_msgs
)

# Generate actions in the 'action' folder
add_action_files(
  FILES
  Fibonacci.action
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
)

## Include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
catkin_install_python(PROGRAMS
  scripts/fibonacci_action_client.py
  scripts/fibonacci_action_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)