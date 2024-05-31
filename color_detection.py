import cv2
import numpy as np

def detect_color(frame, color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    if color == "red":
        lower = np.array([0, 100, 100])
        upper = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower, upper)
        
        lower = np.array([160, 100, 100])
        upper = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower, upper)
        
        mask = cv2.bitwise_or(mask1, mask2)
        
    elif color == "green":
        lower = np.array([40, 100, 100])
        upper = np.array([80, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        
    elif color == "blue":
        lower = np.array([100, 100, 100])
        upper = np.array([140, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        
    return mask
