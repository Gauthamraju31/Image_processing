import cv2
import numpy as np

def nothing(x):
    pass

class color_match:
    
    def __init__(self,img,colorspace):
        self.img=img
        self.colorspace=colorspace
            
    def trackbar(self):
        cv2.namedWindow(self.colorspace)
        if self.colorspace=="rgb_n":
            pass
        if self.colorspace=="hsv":
            self.img=cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
                          
        cv2.createTrackbar(self.colorspace[0]+'min', self.colorspace,0,255,nothing)
        cv2.createTrackbar(self.colorspace[0]+'max', self.colorspace,0,255,nothing)
        cv2.createTrackbar(self.colorspace[1]+'min', self.colorspace,0,255,nothing)
        cv2.createTrackbar(self.colorspace[1]+'max', self.colorspace,0,255,nothing)
        cv2.createTrackbar(self.colorspace[2]+'min', self.colorspace,0,255,nothing)
        cv2.createTrackbar(self.colorspace[2]+'max', self.colorspace,0,255,nothing)

        while(1):
            
            cmn_0 = cv2.getTrackbarPos(self.colorspace[0]+'min',self.colorspace)
            cmx_0 = cv2.getTrackbarPos(self.colorspace[0]+'max',self.colorspace)
            cmn_1 = cv2.getTrackbarPos(self.colorspace[1]+'min',self.colorspace)
            cmx_1 = cv2.getTrackbarPos(self.colorspace[1]+'max',self.colorspace)
            cmn_2 = cv2.getTrackbarPos(self.colorspace[2]+'min',self.colorspace)
            cmx_2 = cv2.getTrackbarPos(self.colorspace[2]+'max',self.colorspace)

            lower = np.array([cmn_0,cmn_1,cmn_2])
            higher = np.array([cmx_0,cmx_1,cmx_2])

            mask = cv2.inRange(self.img, lower, higher)
            cv2.imshow('image',self.img)
            cv2.imshow('mask',mask)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()
        return (lower,higher)    



            
