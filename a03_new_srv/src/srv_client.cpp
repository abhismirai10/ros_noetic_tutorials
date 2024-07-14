#include "ros/ros.h"
#include "a03_new_srv/new_srv.h"
#include <iostream>
#include <sstream> //for string related operations

using namespace std;

int main(int argc, char **argv){
    ros::init(argc, argv, "new_client");
    ros::NodeHandle n;

    ros::ServiceClient client = n.serviceClient<a03_new_srv::new_srv>("new_srv");
    a03_new_srv::new_srv srv;
    std::stringstream ss;
    ss<< "what is the answer of the world, universe and everything";
    srv.request.que = ss.str(); 

    if (client.call(srv)){ //sending the service request 
        ROS_INFO("From Client: [%s], Server says :[%s]",srv.request.que.c_str(),srv.response.ans.c_str());

    }
    else{ 
        ROS_ERROR("Failed to call service"); 
        return 1; 
    } 
    return 0;
}