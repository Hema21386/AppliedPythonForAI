#CV: help the computer to identify and understand the digital content [computer vision]

# pixels: digital image stored as a set of numbers// tiny dots on computer display arranged in rows and columns 

# Binary images: black and white images (0:black, 1:white)
# Gray scale images: Monochrome (one coloured[0-255])
# coloured images: 3 bands/channels - red band[0-255], green band[0-255], blue band[0-255]


# openCV
#pip install opencv-python

#cv2

import cv2

img=cv2.imread("C:\Hema\PythonForVS\TestmkDir\imagefiles\IMG-20180412-WA0023.jpg")

cv2.imshow("Display image",img)
#converting the actual image to a gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Display image",gray_img)
print(gray_img)
cv2.waitKey(0)

# in opencv coloured images are represented as BGR band