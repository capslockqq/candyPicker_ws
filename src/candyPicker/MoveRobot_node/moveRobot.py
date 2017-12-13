#!/usr/bin/env python


import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction
from control_msgs.msg import FollowJointTrajectoryFeedback
from control_msgs.msg import FollowJointTrajectoryResult
from control_msgs.msg import FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Float64

import math

class moveRobot():
    N_JOINTS = 4
    def coordToGoal(self, coords):
        self.joint_positions = []
        self.names =["joint1",
                "joint2",
                "joint3",
                "joint4"
                ]
        dur = rospy.Duration(1)
        xyz_positions = [coords]
        print "efter vi gsnger", xyz_positions
        # construct a list of joint positions by calling invkin for each xyz point
        for p in xyz_positions:
            jtp = JointTrajectoryPoint(positions=invkin(p),velocities=[0.2]*self.N_JOINTS ,time_from_start=dur)
            dur += rospy.Duration(2)
            self.joint_positions.append(jtp)

        self.jt = JointTrajectory(joint_names=self.names, points=self.joint_positions)
        self.goal = FollowJointTrajectoryGoal( trajectory=self.jt, goal_time_tolerance=dur+rospy.Duration(2) )
        return self.goal
        
def invkin(xyz):
    """
    Python implementation of the the inverse kinematics for the crustcrawler
    Input: xyz position
    Output: Angels for each joint: q1,q2,q3,q4
    
    You might adjust parameters (d1,a1,a2,d4).
    The robot model shown in rviz can be adjusted accordingly by editing au_crustcrawler_ax12.urdf
    """

    d1 = 16.7; # cm (height of 2nd joint)
    a1 = 0.0; # (distance along "y-axis" to 2nd joint)
    a2 = 17.35; # (distance between 2nd and 3rd joints)
    d4 = 24.9; # (distance from 3rd joint to gripper center - all inclusive, ie. also 4th joint)    
    offset = 3
    hyp = math.sqrt(math.pow(offset,2)+math.pow(20.3,2));
    angle = math.sin(offset/hyp);
    #print(angle), "\r" 

    q1 = math.atan2(xyz[1], xyz[0]);
    
    r2 = math.pow(xyz[0]-(a1*math.cos(q1)),2)+math.pow(xyz[1]-(a1*math.sin(q1)),2);
#     print('R2'), "\r" 
#     print(r2), "\r" 
    s = (xyz[2] - d1)*(-1);
    D = (r2+math.pow(s,2)-math.pow(a2,2)-math.pow(d4,2))/(2*a2*d4);
    q3 = math.atan2(+math.sqrt(1-math.pow(D, 2)), D);
    q2 = math.atan2(s,math.sqrt(r2))-math.atan2(d4*math.sin(q3),a2+d4*math.cos(q3));
    
    q3 = q3+(3.14/2)
    q1 = q1*(-1);
    
#     print('s'), "\r" 
#     print(s), "\r" 
#     print('Q1'), "\r" 
#     print(q1), "\r" 
#     print('Q3 before correction'), "\r" 
#     print(q3), "\r" 
#     print('Q2 before correction'), "\r" 
#     print(q2), "\r" 
#     print('fuckfuck'), "\r" 
    
    q4 = 0;
    
    q2 = q2 + (3.14/2);
    q3 = q3 - (3.14/2);
    
    q2 = q2*(-1);
    q3 = q3*(-1);
#     
#     print('q2 after correction'), "\r" 
#     print(q2), "\r" 
#     print('q3 after correction'), "\r" 
#     print(q3), "\r" 
#     
#     print('D'), "\r" 
#     print(D), "\r" 
    
    #q1 = 0;
    #q2 = 0;
    #q3 = 0;
    #q4 = 0;
    
    return q1,q2,q3,q4
