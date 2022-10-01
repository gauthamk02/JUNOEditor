import numpy as np
import cv2

class Processing:
    
    def channel_correction(img, channel, correction):
        img[:, :, channel] = img[:, :, channel] * correction
        return img