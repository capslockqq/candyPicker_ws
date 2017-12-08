class inverseKinematic():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("sort_by_color", String, self.callback)
        rospy.spin()
