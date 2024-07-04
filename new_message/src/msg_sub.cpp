#include "ros/ros.h"
#include "new_message/new_msg.h"
#include "iostream"
#include "sstream"

void callback(const new_message::new_msg::ConstPtr& msg){
    ROS_INFO("%s", msg->greeting.c_str());
    ROS_INFO("%d",msg->number);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "msg_sub");
    ros::NodeHandle node;
    ros::Subscriber sub = node.subscribe("new_msg_chatter",10,callback);
    ros::spin();
    return 0;
}