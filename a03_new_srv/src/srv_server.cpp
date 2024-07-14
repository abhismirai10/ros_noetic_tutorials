#include "ros/ros.h"
#include "a03_new_srv/new_srv.h"
#include <iostream>
#include <sstream> //for string related operations

using namespace std; //using standered name space 

bool callback(a03_new_srv::new_srv::Request &req, 
              a03_new_srv::new_srv::Response &res){
    std::stringstream ss;
    ss << "42";
    res.ans = ss.str(); 
    ROS_INFO("From Client [%s], Server says [%s]",req.que.c_str(),res.ans.c_str()); 

    return true;
}

int main(int argc, char **argv) {   //to get cmd inputs
    ros::init(argc, argv, "srv_server");
    ros::NodeHandle n;
    
    ros::ServiceServer service = n.advertiseService("new_srv", callback);
    ROS_INFO("Ready to receive service request");
    ros::spin();
    return 0;
}
