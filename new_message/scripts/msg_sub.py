import rospy
from new_message.msg import new_msg

def callback(data):
    print("%s = %d" %(data.greeting, data.number))

def new_msg_listener():
    sub = rospy.Subscriber("new_msg_chatter", new_msg, callback)
    rospy.init_node("new_msg_talker", anonymous=True)

    rospy.spin()

if __name__ == "__main__":
    try:
        new_msg_listener()
    except rospy.ROSInterruptException:
        pass