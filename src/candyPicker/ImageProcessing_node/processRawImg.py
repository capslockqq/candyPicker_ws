import cv2
import urllib
import numpy as np
import math

lower_blue = np.array([100,50,50])
upper_blue = np.array([130,255,255])

lower_green = np.array([35,50,50])
upper_green = np.array([90,255,255])

lower_yellow = np.array([20,50,50])
upper_yellow = np.array([30,255,255])

lower_red1 = np.array([0,50,50])
upper_red1 = np.array([20,255,255])

lower_red2 = np.array([155,50,50])
upper_red2 = np.array([179,255,255])



class processRawImg():
    def getFromWebcam(self):
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
            return 0
      
    def getProcessedImg(self, color):
        rawImg = self.getFromWebcam()
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/rawSaved.jpg',rawImg)
        if (color == "blue"):
            upper = upper_blue
            lower = lower_blue
        elif (color == "green"):
            upper = upper_green
            lower = lower_green
        elif (color == "yellow"):
            upper = upper_yellow
            lower = lower_yellow 
        else:
            lower = lower_blue
            upper = upper_blue
           

        singleColorImg = self.extract_single_color_range(rawImg, lower, upper)
        
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/singleColor.jpg',singleColorImg)
        
        croppedImg = self.cropPic(singleColorImg)
        
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/cropped.jpg',croppedImg)
        
        processedImg = self.optimizePic(croppedImg)
        
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/processed.jpg',processedImg)
        
        
        
        return processedImg
    
    def optimizePic(self, image):
        refGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("refGray",refGray)
        
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/gray.jpg',refGray)
        
        #edges = cv2.Canny(refGray,100,140)
        #cv2.imshow('Canny',edges)
    
        ret,refTh1 = cv2.threshold(refGray,100,255,cv2.THRESH_BINARY)
        cv2.imshow('RefThresholded',refTh1)
        
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/thresholded.jpg',refTh1)
    
        refDilated = cv2.dilate(refTh1,np.ones((2,2),np.uint8))
        cv2.imshow('RefDilated',refDilated)
    
        refClosed = cv2.morphologyEx(refDilated, cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
        cv2.imshow('RefCload',refClosed)
        return refClosed
    
    def extract_single_color_range(self, image,lower,upper):
        """
        Calculates a mask for which all pixels within the specified range is set to 1
        the ands this mask with the provided image such that color information is
        still present, but only for the specified range
        """
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        img = cv2.bitwise_and(image,image, mask= mask)
        return img

    def cropPic(self, image):
        croppedImage = image[100:300, 100:600]
        return croppedImage
           
