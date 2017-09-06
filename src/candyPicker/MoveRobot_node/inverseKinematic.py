from std_msgs.msg import String
import rospy

class inverseKinematic():
    def __init__(self):
        self.something = 0
    def goTo(self, coords):
        self.some = coords
