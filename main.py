import cv2
lena = cv2.imread('./design.png')
cv2.namedWindow('test')
cv2.imshow('test', lena)
cv2.waitKey()