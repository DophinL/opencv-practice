import cv2
import numpy as np
blue = np.zeros((300,300,3), dtype=np.uint8)
blue[:, :, 0] = 255
cv2.imshow('test', blue)
cv2.waitKey()