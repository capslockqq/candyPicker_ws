#!/usr/bin/env python
from std_msgs.msg import String
import rospy

class UI():
	def __init__(self):
		self.sort_string_puplisher = rospy.Publisher("sort_by_color", String)
		self.my_timer = rospy.Timer(rospy.Duration(0.1), self.on_timer) 
		print "hej"
		
	def on_timer(self, event): 
		message = String("hello_world")  
		self.sort_string_puplisher.publish(message) 

if __name__ == "__main__":
	rospy.init_node("UI_node")
	node = UI()
	rospy.spin()

