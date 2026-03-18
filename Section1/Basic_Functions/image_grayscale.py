#Import All the Required Libraries
import cv2

#Read an Image using OpenCV
image = cv2.imread("../Resources/Images/image1.jpg")

#Convert the Image to Gray Scale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Display the Image
cv2.imshow("Image", image)
cv2.imshow("Gray Scale Image", imageGray)

cv2.waitKey(0)

cv2.destroyAllWindows()