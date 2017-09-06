#!/usr/bin/env python
from std_msgs.msg import String, Bool, Int32MultiArray
import rospy
import inverseKinematic
from candyPicker.msg import arrayCoord
class moveRobot_node():
    def __init__(self):
        rospy.init_node('MoveRobot_node', anonymous=True)
        rospy.Subscriber("physicalCoord", arrayCoord, self.callback)
        self.doneMoving_publisher = rospy.Publisher("doneMoving", Bool)
        
        self.invKin = inverseKinematic.inverseKinematic()
        rospy.spin()
        
    def doneMoving(self): 
        self.doneMoving_publisher.publish(True)      
        
    def callback(self,coords):
        print "Callback moveRobot \r"
        print coords, "\r"
        self.invKin.goTo(10)
        self.doneMoving()

if __name__ == "__main__":
    node = moveRobot_node()
    

