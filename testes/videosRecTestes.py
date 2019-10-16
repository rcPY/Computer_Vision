import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print (cap.get(3))
print (cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('teste.avi',fourcc,20.0,(640,480))


while (cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('cena',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release
cv2.destroyAllWindows()