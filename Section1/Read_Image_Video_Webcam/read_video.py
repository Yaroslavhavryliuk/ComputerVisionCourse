#Import All the Required Libraries
import cv2

#Create a Video Capture Object
cap = cv2.VideoCapture("Section1/Resources/Videos/video6.mp4")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#Release the Video Capture Object
cap.release()
#Close All the Frames
cv2.destroyAllWindows()