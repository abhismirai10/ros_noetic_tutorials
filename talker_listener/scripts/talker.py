import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("chatter", String, queue_size=10) #it can rememner upto 10 msg before publishing
    rospy.init_node("talker", anonymous=True) #resolve name conficts
    rate = rospy.Rate(10) #10hz #there are other methods as well for timeing

    while not rospy.is_shutdown():
        hello_str = "hello world %s" %rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass