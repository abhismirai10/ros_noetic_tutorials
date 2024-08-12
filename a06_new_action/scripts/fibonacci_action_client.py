#!/usr/bin/env python3

import rospy
import actionlib
from a06_new_action.msg import FibonacciAction, FibonacciGoal

def fibonacci_client():
    # Create an action client
    client = actionlib.SimpleActionClient('fibonacci', FibonacciAction)

    # Wait for the server to start up
    rospy.loginfo("Waiting for action server to start...")
    client.wait_for_server()

    # Create a goal to send to the action server
    goal = FibonacciGoal(order=20)

    # Send the goal to the action server
    rospy.loginfo("Sending goal to action server...")
    client.send_goal(goal, feedback_cb=feedback_callback)

    # Wait for the server to finish performing the action
    client.wait_for_result()

    # Get the result of executing the action
    result = client.get_result()
    rospy.loginfo(f"Result: {result.sequence}")

def feedback_callback(feedback):
    rospy.loginfo(f"Feedback: {feedback.partial_sequence}")

if __name__ == '__main__':
    try:
        # Initialize the ROS node
        rospy.init_node('fibonacci_action_client')
        fibonacci_client()
    except rospy.ROSInterruptException:
        rospy.loginfo("Program interrupted before completion")