#Import All the Requried Libraries
import cv2
import numpy as np
#Read the Input Image
image = cv2.imread("../Resources/Images/image5.jpg")

#Detect Edges in the Image using Canny Edge Detector
imageCanny = cv2.Canny(image, 100, 100)

#Dialation: To increase the thickness of our edges
kernel = np.ones((5,5), np.uint8)

#print(kernel)

imageDialation = cv2.dilate(imageCanny, kernel, iterations=1)

#Iterations - 02
imageDialation_ = cv2.dilate(imageCanny, kernel, iterations=2)

cv2.imshow("Canny Edge Detector", imageCanny)

cv2.imshow("Image Dialation", imageDialation)

cv2.imshow("Image Dilation with Iterations 02", imageDialation_)
cv2.waitKey(0)
cv2.destroyAllWindows()