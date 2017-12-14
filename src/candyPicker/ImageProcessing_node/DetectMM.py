import cv2
import numpy as np
import math


class DetectMM():
    def getMMs(self, img):
        
        refMMs = self.findRefMMs()
        
        cv2.imwrite('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/BGcopy.jpg',img)
        BGcopy = cv2.imread('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/BGcopy.jpg')
        
        Cnt, refHierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
   
        for b in Cnt:
            cv2.drawContours(BGcopy,[b],0,(255,0,0),2)
   
        cv2.imshow('allContours',BGcopy)
        
        contoursSortedList = []
   
        contoursSorted = self.sortContourSize(*Cnt)
        print "Legnth of countour ", len(contoursSorted), "\r"
   
        imageCopyNew = cv2.imread('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/BGcopy.jpg')
       
        for b in contoursSorted:
            cv2.drawContours(imageCopyNew,[b],0,(255,0,0),2)
   
        cv2.imshow('Found MMs by size',imageCopyNew)
        
        imageCopyNew1 = cv2.imread('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/BGcopy.jpg')
        
        matchResult = self.shapeMatchingContour(*contoursSorted)
        
        MMsFoundCnt = []
        
        
        for i, cnt in enumerate(matchResult):
            print "Matchersult", matchResult[i]
            if matchResult[i] < 0.15:
                
                MMsFoundCnt.append(contoursSorted[i])
        
        print "MMfoundLengt"    
        print len(MMsFoundCnt)
        
        M = cv2.moments(MMsFoundCnt[0])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])  
        print "X: ", cX, "Y: ", cY, "\r"
        return cX,cY
         
    
    def shapeMatchingContour(self, *contourList):
        result = []
        for i,cnt in enumerate(contourList):
            result.append(cv2.matchShapes(self.MMcntRef[0],cnt,1,0.0)) 
            result[i] += cv2.matchShapes(self.MMcntRef[1],cnt,1,0.0)
            result[i] += cv2.matchShapes(self.MMcntRef[2],cnt,1,0.0)
            result[i] = result[i]/3
    
        return result    
    
    def optimizePic(self, image):
        refGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("refGray",refGray)
        
        #edges = cv2.Canny(refGray,100,140)
        #cv2.imshow('Canny',edges)
    
        ret,refTh1 = cv2.threshold(refGray,150,255,cv2.THRESH_BINARY_INV)
        cv2.imshow('RefThresholded',refTh1)
    
        refDilated = cv2.dilate(refTh1,np.ones((1,1),np.uint8))
        cv2.imshow('RefDilated',refDilated)
    
        refClosed = cv2.morphologyEx(refDilated, cv2.MORPH_CLOSE,np.ones((3,3),np.uint8))
        cv2.imshow('RefCload',refClosed)
        return refClosed
        
    def sortContourSize(self, *contourList):
        MMlist = []
        for i,cnt in enumerate(contourList):
            area = cv2.contourArea(cnt)
            if area > 130 and area < 350:
                MMlist.append(contourList[i])
        return MMlist
    
    def sortContourSizeRef(self, *contourList):
        MMlist = []
        for i,cnt in enumerate(contourList):
            area = cv2.contourArea(cnt)
            if area > 180 and area < 350:
                MMlist.append(contourList[i])
        return MMlist
    
    def findRefMMs(self):
        refImage = cv2.imread('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/originalRef.jpg')
        
        optimizedRef = self.optimizePic(refImage)
        
        refCnt, refHierarchy = cv2.findContours(optimizedRef,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        
        sortContour = []

        sortContour = self.sortContourSizeRef(*refCnt)
        
        self.MMcntRef = []
        
        self.MMcntRef.append(sortContour[0]) #Area = 284
        self.MMcntRef.append(sortContour[1]) #Area = 218
        self.MMcntRef.append(sortContour[2]) #Area = 243
        
        newRefImage = cv2.imread('/home/ubuntu/candyPicker_ws/src/candyPicker/ImageProcessing_node/originalRef.jpg')

        for b in self.MMcntRef:
            cv2.drawContours(newRefImage,[b],0,(255,0,0),2)

        cv2.imshow('MMs detected',newRefImage)
        
        return self.MMcntRef
    
    def getDesCoord(self,color):
        if (color == "Blue"):
            x = 600
            y = 180
            return x,y
            
        elif (color == "Green"):
            x = 40
            y = 380
            return x,y
            
        elif (color == "Red"):
            x = 600
            y = 380
            return x,y
            
        elif (color == "Brown"):
            x = -84.827
            y = 212.345
            return x,y
            
        else:
            return 0

    
    
        
    
        