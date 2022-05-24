import cv2
import numpy as np
original = cv2.imread('./cat.jpeg')
rdm = np.random.randint(0, 256, (120, 120, 3))
original[91:(91+120), 55: (55+120)]=rdm
cv2.imshow('test',original)
cv2.waitKey()