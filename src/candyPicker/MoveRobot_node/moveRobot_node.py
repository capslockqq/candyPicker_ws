#!/usr/bin/env python
from std_msgs.msg import String, Bool, Int32MultiArray
import rospy
import inverseKinematic

class moveRobot_node():
    def __init__(self):
        rospy.init_node('MoveRobot_node', anonymous=True)
        rospy.Subscriber("physicalCoords", Int32MultiArray, self.callback)
        self.doneMoving_puplisher = rospy.Publisher("doneMoving", Bool)
        
        self.invKin = inverseKinematic.inverseKinematic()
        rospy.spin()
        
    def doneMoving(self): 
        self.sort_string_puplisher.publish(True)      
        
    def callback(info,coords):
        print "Callback moveRobot"
        self.invKin.goTo(coords)
        self.doneMoving()
        print message

if __name__ == "__main__":
    node = moveRobot_node()
    

