cmake_minimum_required(VERSION 3.0.2)
project(talker_listener)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
    CATKIN_DEPENDS
    std_msgs
    rospy
    roscpp
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(talker.cpp src/talker.cpp)
add_executable(listener.cpp src/listener.cpp)

target_link_libraries(talker.cpp ${catkin_LIBRARIES})
target_link_libraries(listener.cpp ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS
  scripts/talker.py
  scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(FILES
  launch/talker_listener.launch
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
