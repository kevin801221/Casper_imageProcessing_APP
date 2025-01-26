class ImageCropper:
   @staticmethod
   def crop_to_ratio(image, aspect_ratio="1:1"):
       h, w = image.shape[:2]
       ratios = {
           "1:1": 1, 
           "4:3": 4/3,
           "16:9": 16/9
       }
       target_ratio = ratios.get(aspect_ratio, 1)
       
       if w/h > target_ratio:
           new_w = int(h * target_ratio)
           start = (w - new_w) // 2
           return image[:, start:start+new_w]
       else:
           new_h = int(w / target_ratio)
           start = (h - new_h) // 2
           return image[start:start+new_h, :]