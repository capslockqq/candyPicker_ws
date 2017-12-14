#!/usr/bin/env python
import rospy
import time
import os
import tty
import sys
import termios
class UI():
    def __init__(self, UI_node_obj):
        time.sleep(1)
        self.UINode = UI_node_obj
        self.UIHasBeenCreated = False
        
    def printUI(self):
        
        self.clearScreen()
        self.printWelcomeText()
        self.printOptions()
        if (self.UIHasBeenCreated == False):
            self.waitForInput()
            
    def clearScreen(self):
        os.system('clear')
        
    def printWelcomeText(self):
        print "Welcome to Candy picker 1.0! \r"
        print "You now have the follwoing options: \r"
            
    def printOptions(self):
        print "Press 1 for sorting all green pieces of candy \r"
        print "Press 2 for sorting all blue pieces of candy \r"
        print "Press 3 for sorting all red pieces of candy \r"
        print "Press 4 for sorting all pieces of candy \r"
        print "Press 5 for refreshing the UI \r"
        print "Press 9 for calibrating the camera \r"
        print "Press ESC for closing the application \r"
        
    def waitForInput(self):  
        self.UIHasBeenCreated = True  
        orig_settings = termios.tcgetattr(sys.stdin)   
        tty.setraw(sys.stdin)
        input = 0
        while input != chr(27): # ESC
            input=sys.stdin.read(1)[0]
            if (input == '1'):
                print ("Sorting all green pieces of candy!  \r")
                self.UINode.sort("Green")
            if (input == '2'):
                print ("Sorting all blue pieces of candy!  \r")
                self.UINode.sort("Blue")
            
            if (input == '3'):
                print ("Sorting all red pieces of candy!  \r")
                self.UINode.sort("Red")
                
            if (input == '4'):
                print ("Sorting all pieces of candy!  \r")
                self.UINode.sort("All")
                
            if (input == '5'):
                self.printUI()
                
            if (input == '8'):
                self.UINode.sort("Yellow")
                
            if (input == '9'):
                print ("Calibrating camera...  \r")
                self.UINode.fullyErrect()
                self.UINode.refSetup()
                
            if (input == '\x1b'):
                print ("Terminating program...  \r")
                time.sleep(1)
                rospy.loginfo("Shutting down ROS node...")
                rospy.signal_shutdown("User exited MORSE simulation")
            
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)   
        
    def PrintMessageFromNode(self, message):
        print message, "\r"
        

