class DetectRefobj():
    def getRef(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
        cv2.imshow("grey",gray)
         
         
        circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                      param1=50,
                      param2=25,
                      minRadius=15,
                      maxRadius=22)
        circles = np.uint32(np.around(circles))
        for i in circles[0,:]:
        #draw the outer circle
            cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)
        #draw the center of the circle
            cv2.circle(image,(i[0],i[1]),2,(0,0,255),1)
        
            centerPointX = i[0]
            centerPointY = i[1]
        
        cv2.imshow('detected circles',image)
        
        return centerPointX, centerPointY