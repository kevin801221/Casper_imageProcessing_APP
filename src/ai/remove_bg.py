import cv2
import numpy as np
class BackgroundRemover:
   @staticmethod
   def remove_background(image):
       mask = np.zeros(image.shape[:2], np.uint8)
       bgdModel = np.zeros((1,65), np.float64)
       fgdModel = np.zeros((1,65), np.float64)
       rect = (50,50,image.shape[1]-100,image.shape[0]-100)
       cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
       mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
       return image * mask2[:,:,np.newaxis]
