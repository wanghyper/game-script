import cv2
import numpy as np

lower_blue=np.array([100,43,46])
upper_blue=np.array([124,255,255])

cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)#翻转Y
    cv2.imshow('capture', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # get mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # ret, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
    cv2.imshow('Mask', mask)  # detect blue
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Result', res)

    if cv2.waitKey(1) & 0xFF == ord('`') or ret == False:
        break
cv2.imwrite('capture.jpg', frame)
cap.release()
cv2.destroyAllWindows()