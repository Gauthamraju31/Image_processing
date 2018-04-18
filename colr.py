import cv2
from color_module import *

img=cv2.imread("rick.png")

rick=color_match(img,"hsv")
up, low = rick.trackbar()
print up
print low
