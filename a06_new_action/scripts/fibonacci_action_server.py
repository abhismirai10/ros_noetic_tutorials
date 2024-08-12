#!/usr/bin/env python3

import rospy
import actionlib
from a06_new_action.msg import FibonacciAction, FibonacciFeedback, FibonacciResult

class FibonacciActionServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('fibonacci', FibonacciAction, self.execute, False)
        self.server.start()
        rospy.loginfo("Fibonacci Action Server started")

    def execute(self, goal):
        feedback = FibonacciFeedback()
        result = FibonacciResult()
        
        # Initialize the Fibonacci sequence
        a, b = 0, 1
        feedback.partial_sequence = [a, b]
        
        # Calculate Fibonacci sequence
        for i in range(1, goal.order):
            if self.server.is_preempt_requested():
                self.server.set_preempted()
                rospy.loginfo("Goal preempted")
                return
            
            # Calculate next Fibonacci number
            a, b = b, a + b
            feedback.partial_sequence.append(b)
            
            # Publish feedback
            self.server.publish_feedback(feedback)
            rospy.sleep(0.5)  # Simulate some work being done
        
        # Set the final result
        result.sequence = feedback.partial_sequence
        self.server.set_succeeded(result)
        rospy.loginfo(f"Goal succeeded. Final sequence: {result.sequence}")

if __name__ == '__main__':
    rospy.init_node('fibonacci_action_server')
    server = FibonacciActionServer()
    rospy.spin()