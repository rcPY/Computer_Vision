import cv2

cap = cv2.VideoCapture('ball_tracking_example.mp4')
print (cap.get(3))
print (cap.get(4))

while (cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('cena',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()