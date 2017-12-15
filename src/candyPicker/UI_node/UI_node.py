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
		self.topicColor = color
		if (color == "All"):
			self.color = "Green"
			self.Sort_publisher.publish(self.color)
		else:
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
		
		
		if (message.data == "No more mms to be found"):
			if (self.topicColor == "All"):
				if (self.color == "Green"):
					self.color = "Blue"
					self.Sort_publisher.publish(self.color)
				
				elif (self.color == "Blue"):
					self.color = "Red"
					self.Sort_publisher.publish(self.color)
				
				elif (self.color == "Red"):
					self.color = "Yellow"
					self.Sort_publisher.publish(self.color)
					
				elif (self.color == "Yellow"):
					self.UI_obj.PrintMessageFromNode(message.data)
					self.fullyErrect()
					
			else:
				self.UI_obj.PrintMessageFromNode(message.data)
				self.fullyErrect()
					
		else:
			self.UI_obj.PrintMessageFromNode(message.data)
				
		
			
		
		
		
if __name__ == "__main__":
	
	node = UI_node()
	

