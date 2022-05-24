import cv2
import numpy as np
rdm = np.random.randint(0, 256, size=[300, 300], dtype=np.uint8)
cv2.imshow('test',rdm)
cv2.waitKey()