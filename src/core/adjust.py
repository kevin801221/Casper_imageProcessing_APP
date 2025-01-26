import cv2
import numpy as np
class ImageAdjuster:
   @staticmethod
   def adjust_brightness(image, value):
       if value > 0:
           return cv2.addWeighted(image, 1, np.zeros(image.shape, image.dtype), 0, value)
       return cv2.addWeighted(image, 1 + value/100, np.zeros(image.shape, image.dtype), 0, 0)

   @staticmethod 
   def adjust_contrast(image, value):
       alpha = float(131 * (value + 127)) / (127 * (131 - value))
       return cv2.addWeighted(image, alpha, image, 0, 127*(1-alpha))
   
   @staticmethod
   def adjust_saturation(image, value):
       hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
       hsv[..., 1] = hsv[..., 1] * (1 + value/100)
       return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
