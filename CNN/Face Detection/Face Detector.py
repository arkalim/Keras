import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(r"C:\Users\arkha\OneDrive\Desktop\ML\Deep Learning\Face Detection\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while(True):
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(155,200,0),2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
