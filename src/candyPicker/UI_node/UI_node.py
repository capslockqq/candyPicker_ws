#!/usr/bin/env python
from std_msgs.msg import Bool, String
import rospy

class UI_node():
	def __init__(self):
		rospy.init_node("UI_node")
		self.Sort_publisher = rospy.Publisher("sort", String)
		self.FullyErrect_publisher = rospy.Publisher("fully_erect", Bool)
		
		rospy.spin()
		

if __name__ == "__main__":
	node = UI_node()

