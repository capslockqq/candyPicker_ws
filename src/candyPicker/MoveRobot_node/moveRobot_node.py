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
        self.goalCoord = [coords.data[0],coords.data[1],coords.data[2]]
        self.desCoord = [coords.data[3],coords.data[4],coords.data[5]]
        self.safetyHeight = [coords.data[0],coords.data[1], 10]
        
        self.goal = self.move.coordToGoal(self.goalCoord)
        
        
        self.client.wait_for_server()
        self.my_publisher.publish(0)
        self.client.wait_for_result()
        self.client.send_goal(self.goal)
        self.client.wait_for_result()
        rospy.sleep(1)
        self.my_publisher.publish(1)
        rospy.sleep(1)  
        
        self.client.wait_for_server()
        self.safetyHeightGoal = self.move.coordToGoal(self.safetyHeight)
        self.goal = self.move.coordToGoal(self.safetyHeightGoal)
        self.client.wait_for_server()
        self.goal = self.move.coordToGoal(self.desCoord)
        self.client.send_goal(self.goal)
        self.client.wait_for_result()
        rospy.sleep(1)
        self.my_publisher.publish(1)
        self.doneMoving()
        
        

if __name__ == "__main__":
    node = moveRobot_node()
    

