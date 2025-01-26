import cv2
import numpy as np
class ImageEnhancer:
   @staticmethod
   def sharpen(image, amount):
       kernel = np.array([[-1,-1,-1], 
                        [-1,9,-1],
                        [-1,-1,-1]]) * (amount/100)
       return cv2.filter2D(image, -1, kernel)
   
   @staticmethod
   def denoise(image, strength):
       return cv2.fastNlMeansDenoisingColored(image, None, strength, strength, 7, 21)