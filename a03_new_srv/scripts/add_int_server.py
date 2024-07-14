import rospy
from a03_new_srv.srv import add_two_int

def callback(req):
    print("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    response = add_two_int._response_class(req.a + req.b)
    return response
def add_int_server():
    rospy.init_node("add_int_server")
    s = rospy.Service("add_int", add_two_int, callback)
    print("ready!!!")
    rospy.spin()

if __name__ == "__main__":
    add_int_server()