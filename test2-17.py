import cv2
import numpy as np
original = cv2.imread('./cat.jpeg')
b, g, r = cv2.split(original)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
print('shape:', b.shape)
print('size:', b.size)
print('o shape:', type(original.shape))
print('o size:', original.size)
cv2.waitKey()