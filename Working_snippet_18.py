import cv2

full_cascade=cv2.CascadeClassifier(r'C:\Users\bmsat\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_fullbody.xml')

vid=cv2.VideoCapture("walking.avi")

while(True):
    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body=full_cascade.detectMultiScale(gray,1.1,8)
    for x,y,w,h in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,150,255),2)
    cv2.imshow("Fullbody Detection", frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows