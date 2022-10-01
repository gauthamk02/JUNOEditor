from skimage import img_as_ubyte
# from skimage.color import rgb2gray
from skimage.exposure import histogram, cumulative_distribution
import numpy as np
import cv2

class Processing:
    
    def channel_correction(img, channel= (0, 1, 2), correction= (1, 1, 1)):
        img[:, :, channel] = img[:, :, channel] * correction
        return img

    def __linear_distribution(image, channel):
        image_intensity = img_as_ubyte(image[:,:,channel])
        freq, bins = cumulative_distribution(image_intensity)
        target_bins = np.arange(255)
        target_freq = np.linspace(0, 1, len(target_bins))
        new_vals = np.interp(freq, target_freq, target_bins)
        return new_vals[image_intensity].astype(np.uint8)

    def auto_enhance(image):
        img = image.copy()
        for channel in range(3):
            img[:,:,channel] = Processing.__linear_distribution(img, channel)
        img = Processing.changeBrightness(img, 50)
        img = Processing.changeContrast(img, 50)

        return img

    def changeBrightness(img,value):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - value
        v[v>lim] = 255
        v[v<=lim] += value
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
        
    def changeBlur(img,value):
        kernel_size = (value+1,value+1) 
        img = cv2.blur(img,kernel_size)
        return img

    def changeContrast(img,value):
        lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=((value/100)+1))
        cl = clahe.apply(l_channel)
        limg = cv2.merge((cl,a,b))
        img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        return img

    