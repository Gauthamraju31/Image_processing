import cv2
import numpy as np

def nothing(x):
    pass

class color_module:
    def __init__(self,image,colorspace):
        self.img=image
        self.colorspace=colorspace
        self.x1, self.y1 = [0,0]
        self.x2, self.y2 ,self.z = self.img.shape
        self.cropping = False
        self.img_bck=self.img.copy()
        self.refPt=[]
        self.border=(0,255,0)

    def ROI(self,event,x,y,flags,param):
        
        if event == cv2.EVENT_LBUTTONDOWN:
            self.refPt = [(x,y)]
            self.cropping = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.refPt.append((x,y))
            self.cropping = False
            cv2.rectangle(self.img, self.refPt[0], self.refPt[1], self.border, 1)
            
    def Track(self):

        cv2.namedWindow("image")
        cv2.setMouseCallback("image",self.ROI)

        while(1):
        
            cv2.imshow("image",self.img)
            key = cv2.waitKey(1)&0xFF

            if key == ord("r"):
                self.img = self.img_bck.copy()
                print ("Reset")
                
            elif key == ord("c"):
                print ("Select")
                blank=np.zeros((self.x2,self.y2,self.z),dtype=np.uint8)
                cv2.rectangle(blank, self.refPt[0], self.refPt[1], (255, 255, 255), -1)
                self.img=np.bitwise_and(self.img_bck,blank)
                cv2.imshow("image",self.img)
                break

        print("Cropping Done")
        
        img_bck2=self.img    
        cv2.namedWindow("mask")
        cv2.createTrackbar("mask", self.colorspace,0,40,nothing)
        min_range=(0,0,0)
        max_range=(255,255,255)
        self.border=(0,0,0)

        Selected=self.img[self.refPt[0][0]:self.refPt[1][0],self.refPt[0][1]:self.refPt[1][1]]
        
        while(1):
            cv2.imshow("image",self.img)
            key = cv2.waitKey(1)&0xFF
            
            if key == ord("r"):
                self.img = img_bck2
                print ("Reset")
                
            elif key == ord("c"):
                colrs=self.img[self.refPt[0][0]:self.refPt[1][0],self.refPt[0][1]:self.refPt[1][1]]
                print ("Select")
                min_range=np.array([np.amin(colrs[:,:,0]),np.amin(colrs[:,:,1]),np.amin(colrs[:,:,2])])
                max_range=np.array([np.amax(colrs[:,:,0]),np.amax(colrs[:,:,1]),np.amax(colrs[:,:,2])])
                print(min_range,max_range)
                
            mask=cv2.inRange(selected,min_range,max_range)
            cv2.imshow("mask",mask)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        print("Done")
        cv2.destroyAllWindows()              
