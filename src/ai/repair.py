# src/ai/repair.py
import cv2
import numpy as np

class ImageRepairer:
   @staticmethod
   def remove_spots(image, kernel_size=3):
       kernel = np.ones((kernel_size,kernel_size),np.uint8)
       return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
   
   @staticmethod
   def inpaint_defects(image, mask, radius=3):
       return cv2.inpaint(image, mask, radius, cv2.INPAINT_TELEA)