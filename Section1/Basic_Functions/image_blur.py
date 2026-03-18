#Import All the Required Libraries
import cv2

#Read an Image
image = cv2.imread("../Resources/Images/image1.jpg")

#Blur the input image
imageBlur = cv2.GaussianBlur(image, (7,7), 0)

#Display the Image
cv2.imshow("Image", image)

cv2.imshow("Blur Image", imageBlur)

cv2.waitKey(0)

cv2.destroyAllWindows()