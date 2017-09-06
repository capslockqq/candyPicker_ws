#!/usr/bin/env python
from std_msgs.msg import String
import rospy

class UI():
	def __init__(self):
		self.sort_string_puplisher = rospy.Publisher("sort_by_color", String)
		print "hej"

if __name__ == "__main__":
	rospy.init_node("UI_node")
	node = UI()
	rospy.spin()

