#Import All the Required Libraries
import cv2
import numpy as np

#Read an Image
image = cv2.imread("Section1/Resources/Images/image2.jpg")
print(image.shape)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(imageGray.shape)
#We will stack the images with itself, first i will use the horizontal stack function
imageHor = np.hstack((image, image, image, image))

#Vertical Stack
imageVert = np.vstack((imageHor, imageHor, imageHor))
cv2.imshow("Vertical Stack", imageVert)

cv2.waitKey(0)
cv2.destroyAllWindows()