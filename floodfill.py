import cv2
import numpy as np
img = cv2.imread('./photopea.png')
h, w = img.shape[:2]
filledColor = np.ones(img.shape, dtype=np.uint8)
filledColor[:] = [255, 85, 0]

mask = np.zeros((h + 2, w + 2), dtype=np.uint8)
flag = (4 | cv2.FLOODFILL_FIXED_RANGE | cv2.FLOODFILL_MASK_ONLY | 255 << 8)
cv2.floodFill(img, mask, (422, 796), 255, 20, 20, flag)

copyMask = mask[1:-1, 1:-1]

filledImage = cv2.bitwise_and(filledColor, filledColor, mask=copyMask)
hollowImage = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(copyMask))
finalImage = cv2.bitwise_or(hollowImage, filledImage)

contours, hierarchy = cv2.findContours(copyMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(finalImage, contours, -1, (0,0,255), 2)

print(contours)

cv2.imshow('test', finalImage)
cv2.waitKey()

print(cv2.FLOODFILL_MASK_ONLY)