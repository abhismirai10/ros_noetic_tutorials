#name and cmake version requirements
cmake_minimum_required(VERSION 3.0.2)
project(talker_listener)

#find and set up required packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

#declaration of dependence
catkin_package(CATKIN_DEPENDS
    std_msgs
    rospy
    roscpp
)

#path to include for eg catkin header files path
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

#for cpp
add_executable(talker.cpp src/talker.cpp)
add_executable(listener.cpp src/listener.cpp)

target_link_libraries(talker.cpp ${catkin_LIBRARIES})
target_link_libraries(listener.cpp ${catkin_LIBRARIES})

#for python
catkin_install_python(PROGRAMS
  scripts/talker.py
  scripts/listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#for launch files
install(FILES
  launch/talker_listener.launch
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
