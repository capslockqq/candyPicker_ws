from std_msgs.msg import String
import rospy

class inverseKinematic():
    def __init__(self):
        print "init"
    def goTo(self, coords):
        print coords
