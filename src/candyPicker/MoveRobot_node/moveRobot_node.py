#!/usr/bin/env python
from std_msgs.msg import String, Bool, Int32MultiArray
import rospy
import actionlib
import moveRobot
from candyPicker.msg import arrayCoord
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryFeedback
from control_msgs.msg import FollowJointTrajectoryResult
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Float64
class moveRobot_node():
    def __init__(self):
        rospy.init_node('MoveRobot_node', anonymous=True)
        rospy.Subscriber("physicalCoord", arrayCoord, self.callback)
        self.doneMoving_publisher = rospy.Publisher("doneMoving", Bool)
        self.client = actionlib.SimpleActionClient("/arm_controller/follow_joint_trajectory", FollowJointTrajectoryAction)
        self.my_publisher = rospy.Publisher("/gripper/command",Float64)

        
        self.move = moveRobot.moveRobot()
        rospy.spin()
        
    def doneMoving(self): 
        self.doneMoving_publisher.publish(True)      
        
    def callback(self,coords):
        print "Callback moveRobot \r"
        print coords, "\r"
        goal = self.move.coordToGoal(coords.data)
        
        
        self.client.wait_for_server()
        self.my_publisher.publish(0)
        self.client.wait_for_result()
        self.client.send_goal(goal)
        self.client.wait_for_result()
        rospy.sleep(1)
        self.my_publisher.publish(1)
        rospy.sleep(1)
        self.client.wait_for_server()
        goal = self.move.coordToGoal([0,0,45])
        self.client.send_goal(goal)
        self.client.wait_for_result()
        self.doneMoving()
        
        

if __name__ == "__main__":
    node = moveRobot_node()
    

