#Import All the Required Libraries
import cv2

#Read Image using OpenCV
image = cv2.imread("Section1/Resources/Images/image1.jpg")

#Display the Image
cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()