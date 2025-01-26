import cv2
import numpy as np

class ImageResizer:
   @staticmethod
   def resize_image(image, width=None, height=None, aspect_ratio=True):
       if width and height and not aspect_ratio:
           return cv2.resize(image, (width, height))
       
       h, w = image.shape[:2]
       if width:
           r = width / w
           dim = (width, int(h * r))
       else:
           r = height / h
           dim = (int(w * r), height)
       return cv2.resize(image, dim)

   @staticmethod
   def crop_image(image, aspect_ratio="1:1"):
       h, w = image.shape[:2]
       ratios = {"1:1": 1, "4:3": 4/3, "16:9": 16/9}
       target_ratio = ratios.get(aspect_ratio, 1)
       
       if w/h > target_ratio:
           new_w = int(h * target_ratio)
           start = (w - new_w) // 2
           return image[:, start:start+new_w]
       else:
           new_h = int(w / target_ratio)
           start = (h - new_h) // 2
           return image[start:start+new_h, :]