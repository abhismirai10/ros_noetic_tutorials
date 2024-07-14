#include "ros/ros.h"
#include "std_msgs/String.h"

//subscriber callback function
void chatterCallback(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("I heard: [%s]", msg->data.c_str());
}

//main function
int main(int argc, char **argv){ //argc and argv are argument provided in cmd 
                                 //when running the node eg node name
    ros::init(argc, argv, "listerner"); //init node
    ros::NodeHandle n;      
    
    ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback); //subscription
    ros::spin();
    return 0;
}