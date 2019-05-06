import numpy as np
import cv2

video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(1)
video_capture_2 = cv2.VideoCapture(2)
video_capture_3 = cv2.VideoCapture(3)

while True:
    # Capture frame-by-frame
    ret0, frame0 = video_capture_0.read()
    ret1, frame1 = video_capture_1.read()
    ret2, frame2 = video_capture_2.read()
    ret3, frame3 = video_capture_3.read()

    if (ret0):
        # Display the resulting frame
        cv2.imshow('Cam 1', frame0)

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 2', frame1)

    if (ret2):
        # Display the resulting frame
        cv2.imshow('Cam 3', frame2)
    if (ret3):
        # Display the resulting frame
        cv2.imshow('Cam 4', frame3)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture_0.release()
video_capture_1.release()
video_capture_2.release()
video_capture_3.release()
cv2.destroyAllWindows()
