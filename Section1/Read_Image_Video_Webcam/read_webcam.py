#Import All the Required Libraries
import cv2

#Create a Live Webcam Feed Capture Object
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()