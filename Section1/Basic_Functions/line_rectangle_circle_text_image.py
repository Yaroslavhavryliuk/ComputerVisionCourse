#Import All the Required Libraries
import cv2
import numpy as np

#image = np.zeros((512, 512))

#To add color function we will give it 3 channels
image = np.zeros((512, 512, 3), np.uint8)
image[256:512, 0:512] = 255,0,0
print(image.shape)

#Line
cv2.line(image, (100, 300), (500, 300), (0,255,0), 3)
#Rectangle
cv2.rectangle(image, (0,0), (300, 250), (0,0,255), -1)
#Draw a Circle
cv2.circle(image, (250,250), 40, (255,255,0), -1)
#Text on Image
cv2.putText(image, "OpenCV", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,155,0), 2)

#Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)