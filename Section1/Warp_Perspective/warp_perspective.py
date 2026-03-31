#Import All the Required Libraries
import cv2
import numpy as np

#Read an Image using OpenCV
image = cv2.imread("Section1/Resources/Images/card2.jpg")

width, height = 250, 350
#Define 4 corner points
#For Card 1
#pts1 = np.float32([[112,223], [280, 192], [158,475], [348, 435]])
#For Card 2
pts1 = np.float32([[700, 156], [1122, 423], [290, 692], [727, 992]])
#Define which corner points we are referring to
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix =cv2.getPerspectiveTransform(pts1, pts2)

imageOutput = cv2.warpPerspective(image, matrix, (width, height))

#Display the Image
cv2.imshow("Image", image)
cv2.imshow("Output Image", imageOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()

