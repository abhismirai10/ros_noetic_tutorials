import rospy
from a02_new_msg_type.msg import new_msg

def new_msg_talker():
    pub = rospy.Publisher("new_msg_chatter", new_msg, queue_size=10)
    rospy.init_node("new_msg_talker", anonymous=True)
    
    while not rospy.is_shutdown():
        str = "answer to the universe is "
        pub.publish(new_msg(str, 42))
        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        new_msg_talker()
    except rospy.ROSInterruptException:
        pass