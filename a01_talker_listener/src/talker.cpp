#include "ros/ros.h"
#include "std_msgs/String.h"
#include <iostream>

int main(int argc, char **argv){ //see listener node
    ros::init(argc, argv, "talker"); //init node
    ros::NodeHandle n;

    ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000); //publication init
    ros::Rate loop_rate(10);

    int count = 0;
    while(ros::ok()){ //ctrl+c stops this
        std_msgs::String msg;
        std::stringstream ss;
        ss<< "hello world "<< count;
        msg.data = ss.str();

        ROS_INFO("%s", msg.data.c_str());//printing or logging the data by publisher node
        chatter_pub.publish(msg);// publishing
        ros::spinOnce();
        loop_rate.sleep();
        count++;
    }
    return 0;
}