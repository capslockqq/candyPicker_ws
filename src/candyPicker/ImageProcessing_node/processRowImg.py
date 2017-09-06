#!/usr/bin/env python
from std_msgs.msg import String
import rospy

class ProcessRawImg():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("sort_by_color", String, self.callback)
        rospy.spin()
        
        
    def callback(info, message):
        print message

if __name__ == "__main__":
    node = ProcessRawImg()
