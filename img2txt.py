# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:10:56 2020

@author: shrie
"""

import pytesseract
import cv2
import numpy as np
from PIL import Image

image = cv2.imread('test.png')
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(image, -1, sharpen_kernel)
cv2.imwrite('op.png',sharpen)
cv2.imshow('sharpen', sharpen)
cv2.waitKey()



pytesseract.pytesseract.tesseract_cmd = "D:/Assignments/Tesseract-OCR/tesseract.exe"
img = Image.open('op.png')
text = pytesseract.image_to_string(img)
print(text)