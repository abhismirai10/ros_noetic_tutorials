import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
    rospy.loginfo("also I am fine")

def listener():
    sub = rospy.Subscriber("chatter", String, callback)
    rospy.init_node("listener", anonymous=True)

    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass