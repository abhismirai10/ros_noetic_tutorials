cmake_minimum_required(VERSION 3.0.2)
project(a03_new_srv)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

# Generate services in the 'srv' folder
add_service_files(
  FILES
  new_srv.srv
  add_two_int.srv
)

#dependences for new srv
generate_messages(
  #std_msgs
)

catkin_package(CATKIN_DEPENDS
  roscpp
  rospy
  message_runtime 
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#for cpp
add_executable(srv_server.cpp src/srv_server.cpp)
add_executable(srv_client.cpp src/srv_client.cpp)

#we need to add this for srv as well.
add_dependencies(srv_server.cpp a03_new_srv_generate_messages_cpp)
add_dependencies(srv_client.cpp a03_new_srv_generate_messages_cpp)

target_link_libraries(srv_server.cpp ${catkin_LIBRARIES})
target_link_libraries(srv_client.cpp ${catkin_LIBRARIES})

#for python
catkin_install_python(PROGRAMS
  scripts/add_int_server.py
  scripts/add_int_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)