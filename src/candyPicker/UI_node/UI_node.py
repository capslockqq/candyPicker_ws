#!/usr/bin/env python
from std_msgs.msg import Bool, String, Int32MultiArray
import rospy
import UI
class UI_node():
	def __init__(self):
		rospy.init_node("UI_node")
		self.Sort_publisher = rospy.Publisher("sort", String)
		self.FullyErrect_publisher = rospy.Publisher("fullyErrect", Bool)
		someUI = UI.UI(self)
		rospy.spin()
		
	def sort(self, color):
		self.Sort_publisher.publish(color);

		
	def fullyErrect(self):
		a = Bool()
		a.data = True
		self.FullyErrect_publisher.publish(a);
if __name__ == "__main__":
	
	node = UI_node()
	

