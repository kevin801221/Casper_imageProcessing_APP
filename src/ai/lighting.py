import cv2
class LightingAdjuster:
   @staticmethod
   def auto_lighting(image):
       lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
       l, a, b = cv2.split(lab)
       clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
       cl = clahe.apply(l)
       limg = cv2.merge((cl,a,b))
       return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)