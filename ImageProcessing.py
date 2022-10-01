import numpy as np
import cv2

class Processing:
    
    def channel_correction(img, channel= (0, 1, 2), correction= (1, 1, 1)):
        img[:, :, channel] = img[:, :, channel] * correction
        return img