#Import All the Required Libraries
import cv2

#Read the Input Image
image = cv2.imread("../Resources/Images/image5.jpg")

#Detect Edges in the Image using Canny Edge Detector
imageCanny = cv2.Canny(image, 100, 100)
imageCanny2 = cv2.Canny(image, 150, 200)

#Display the Image
cv2.imshow("Input Image", image)

cv2.imshow("Edge Detector", imageCanny)

cv2.imshow("Reduce Edges", imageCanny2)
cv2.waitKey(0)
cv2.destroyAllWindows()
