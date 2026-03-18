#Import All the Required Libraries
import cv2

#Read the Image
image = cv2.imread("../Resources/Images/image1.jpg")

print(image.shape)

#Height --> 664, Width --> 1000  No. of Channels -->3
#Image Resize
imageResize = cv2.resize(image, (500, 332))
print(imageResize.shape)

imageResize_ = cv2.resize(image, (1200, 800))

print(imageResize_.shape)

#Display the Image
cv2.imshow("Input Image", image)

cv2.imshow("Image Resize", imageResize)

cv2.imshow("Image Resize Increase", imageResize_)

cv2.waitKey(0)
cv2.destroyAllWindows()