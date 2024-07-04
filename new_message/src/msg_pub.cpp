#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include "new_message/new_msg.h"
#include "iostream"
#include "sstream"

using namespace std;

int main(int argc, char **argv){
    ros::init(argc, argv, "msg_pub");
    ros::NodeHandle node;
    ros::Publisher pub = node.advertise<new_message::new_msg>("new_msg_chatter",10);
    ros::Rate loop_rate(10);

    while(ros::ok()){
        new_message::new_msg msg;

        std::stringstream ss;
        ss << "ans to the universe is ";
        msg.greeting = ss.str();
        msg.number = 42;

        pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}