import cv2
face=cv2.CascadeClassifier('C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.1\HaarCascade.xml')
eye=cv2.CascadeClassifier('C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.1\Eye.xml')
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=eye.detectMultiScale(gray,1.03,4)
    faces=face.detectMultiScale(gray,1.03,4)
    for i,j,k,l in eyes:
        cv2.rectangle(frame,(i,j),(i+k,j+l),(0,255,0),3)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('Name',frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
cap.release()