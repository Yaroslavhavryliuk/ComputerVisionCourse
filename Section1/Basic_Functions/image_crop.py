#Import All the Required Libraries
import cv2

#Read the Input Image
image = cv2.imread("../Resources/Images/image1.jpg")

print(image.shape)

#Crop Image
imageCropped = image[332:664, 500:1000]

#Display the Image
cv2.imshow("Image", image)
cv2.imshow("Crop Image", imageCropped)

cv2.waitKey(0)