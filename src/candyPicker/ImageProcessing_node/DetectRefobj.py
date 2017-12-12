import urllib
import cv2
import numpy as np

class DetectRefobj():
    def getRef(self):
        img1 = self.get_from_webcam()
        
        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
 
        cv2.imshow("grey",gray)
         
         
        circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                      param1=50,
                      param2=25,
                      minRadius=15,
                      maxRadius=22)
        circles = np.uint32(np.around(circles))
        for i in circles[0,:]:
        #draw the outer circle
            cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)
        #draw the center of the circle
            cv2.circle(img1,(i[0],i[1]),2,(0,0,255),1)
        
            centerPointX = i[0]
            centerPointY = i[1]
        
        cv2.imshow('detected circles',img1)
        
        return centerPointX, centerPointY
    
    def get_from_webcam(self):
        """
        Fetches an image from the webcam
        """
        print "try fetch from webcam..."
        stream=urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
        bytes=''
        bytes+=stream.read(64500)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
    
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
            return i
        else:
            print "did not receive image, try increasing the buffer size in line 13:"