# src/core/denoise.py
import cv2
import numpy as np

class DenoiseProcessor:
   @staticmethod
   def apply_denoise(image, strength=10):
       return cv2.fastNlMeansDenoisingColored(
           image, 
           None,
           strength,
           strength,
           7,
           21
       )
   
   @staticmethod
   def bilateral_filter(image, d=9):
       return cv2.bilateralFilter(image, d, 75, 75)