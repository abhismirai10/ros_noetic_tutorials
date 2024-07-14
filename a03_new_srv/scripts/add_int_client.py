import sys
import os
import rospy

from a03_new_srv.srv import add_two_int

def add_two_ints_client():
    rospy.init_node("add_int_client")
    rospy.wait_for_service("add_int")
    
    try:
        add_int = rospy.ServiceProxy("add_int", add_two_int)
        print("Requesting %s + %s" % (21, 21))
        resp1 = add_int(21, 21)
        print("%s + %s = %s" % (21, 21, resp1.sum))

        if resp1.sum != (21 + 21):
            raise Exception("Test failure, returned sum was %s" % resp1.sum)
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    add_two_ints_client()