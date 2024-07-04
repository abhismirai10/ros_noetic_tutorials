cmake_minimum_required(VERSION 3.0.2)
project(new_message)

#find and set up ruquired packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation #for msg gen.
)

#for new msg generation
add_message_files(
  FILES
  new_msg.msg
)

#dependences for new msg
generate_messages(
  #std_msgs
)

#declaration of dependence
catkin_package(CATKIN_DEPENDS 
  roscpp 
  rospy
  message_runtime   #important for msg gen.
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#for cpp
add_executable(msg_pub.cpp src/msg_pub.cpp)
add_executable(msg_sub.cpp src/msg_sub.cpp)

add_dependencies(msg_pub.cpp new_message_generate_messages_cpp)
add_dependencies(msg_sub.cpp new_message_generate_messages_cpp)

target_link_libraries(msg_pub.cpp ${catkin_LIBRARIES})
target_link_libraries(msg_sub.cpp ${catkin_LIBRARIES})

#for python
catkin_install_python(PROGRAMS
  scripts/msg_pub.py
  scripts/msg_sub.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

