import cv2

class DetectMM():
    def getMMs(self, img):
        
        refMMs = self.findRefMMs()
        
        cv2.imwrite('BGcopy.jpg',img)
        
        Cnt, refHierarchy = cv2.findContours(imgClosed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
   
        for b in Cnt:
            cv2.drawContours(imageCopy,[b],0,(255,0,0),2)
   
        cv2.imshow('allContours',imageCopy)
        
        contoursSortedList = []
   
        contoursSorted = sortContourSize(*Cnt)
   
   
        imageCopyNew = cv2.imread('BGcopy.jpg')
       
        for b in contoursSorted:
            cv2.drawContours(imageCopyNew,[b],0,(255,0,0),2)
   
        cv2.imshow('Found MMs by size',imageCopyNew)
        
        imageCopyNew1 = cv2.imread('imageCopy.jpg')
        
        matchResult = shapeMatchingContour(*contoursSorted)
        
        MMsFoundCnt = []
        
        for i, cnt in enumerate(matchResult):
            if matchResult[i] < 0.13:
                MMsFoundCnt.append(contoursSorted[i])
        
        M = cv2.moments(contoursSorted[0])
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])  
        
        return cX,cY
         
    
    def shapeMatchingContour(self, *contourList):
        result = []
        for i,cnt in enumerate(contourList):
            result.append(cv2.matchShapes(MMcntRef[0],cnt,1,0.0)) 
            result[i] += cv2.matchShapes(MMcntRef[1],cnt,1,0.0)
            result[i] += cv2.matchShapes(MMcntRef[2],cnt,1,0.0)
            result[i] = result[i]/3
    
        return result    
    
    def optimizePic(self, image):
        refGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("refGray",refGray)
        
        #edges = cv2.Canny(refGray,100,140)
        #cv2.imshow('Canny',edges)
    
        ret,refTh1 = cv2.threshold(refGray,150,255,cv2.THRESH_BINARY_INV)
        cv2.imshow('RefThresholded',refTh1)
    
        refDilated = cv2.dilate(refTh1,np.ones((2,2),np.uint8))
        cv2.imshow('RefDilated',refDilated)
    
        refClosed = cv2.morphologyEx(refDilated, cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
        cv2.imshow('RefCload',refClosed)
        return refClosed
        
    def sortContourSize(self, *contourList):
        MMlist = []
        for i,cnt in enumerate(contourList):
            area = cv2.contourArea(cnt)
            if area > 140 and area < 350:
                MMlist.append(contourList[i])
        return MMlist
    
    def findRefMMs(self):
        refImage = cv2.imread('originalRef.jpg')
        
        optimizedRef = self.optimizePic(refImage)
        
        refCnt, refHierarchy = cv2.findContours(optimizedRef,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        
        sortContour = []

        sortContour = self.sortContourSize(*refCnt)
        
        MMcntRef = []
        
        MMcntRef.append(sortContour[0]) #Area = 284
        MMcntRef.append(sortContour[1]) #Area = 218
        MMcntRef.append(sortContour[2]) #Area = 243
        
        newRefImage = cv2.imread('originalRef.jpg')

        for b in MMcntRef:
            cv2.drawContours(newRefImage,[b],0,(255,0,0),2)

        cv2.imshow('MMs detected',newRefImage)
        
        return MMcntRef

    
    
        
    
        