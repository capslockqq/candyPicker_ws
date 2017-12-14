#!/usr/bin/env python
from std_msgs.msg import Bool, String, Int32MultiArray
import rospy
import UI
class UI_node():
	def __init__(self):
		rospy.init_node("UI_node")
		self.Sort_publisher = rospy.Publisher("sort", String)
		self.FullyErrect_publisher = rospy.Publisher("fullyErrect", Bool)
		self.RefSetup_publisher = rospy.Publisher("refSetup", Bool)
		self.MessageHandling_FromNodes = rospy.Subscriber("messageHandling", String, self.callbackMessageHandling)
		self.UI_obj = UI.UI(self)
		self.UI_obj.printUI()
		rospy.spin()
		
	def sort(self, color):
		self.Sort_publisher.publish(color);

		
	def fullyErrect(self):
		a = Bool()
		a.data = True
		self.FullyErrect_publisher.publish(a);
		
	def refSetup(self):
		a = Bool()
		a.data = True
		self.RefSetup_publisher.publish(a)
		
	def callbackMessageHandling(self, message):
		self.UI_obj.PrintMessageFromNode(message.data)
		
		
if __name__ == "__main__":
	
	node = UI_node()
	

