#Import All the Required Libraries
import cv2
import numpy as np
#Read the Input Image
image = cv2.imread("Section1/Resources/Images/image5.jpg")


#Edge Detection using the Canny Edge Detector
imageCanny = cv2.Canny(image, 100, 100)

#Dialation
kernel = np.ones((3,3), np.uint8)
imageDialation = cv2.dilate(imageCanny, kernel, iterations=1)

#Erosion
imageErosion = cv2.erode(imageDialation, kernel, iterations=1)


cv2.imshow("Image Dialation", imageDialation)

cv2.imshow("Image Erosion", imageErosion)

cv2.waitKey(0)

cv2.destroyAllWindows()
