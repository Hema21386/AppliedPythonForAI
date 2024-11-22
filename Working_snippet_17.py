import cv2

#img=cv2.imread("4f.jpg")

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(r'C:\Users\bmsat\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml')
vid=cv2.VideoCapture(0)

while(True):
    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,5) 
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        eye_gray= gray[y:y+h, x:x+w]
        eye_color=frame[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(eye_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(eye_color, (ex,ey), (ex+ew, ey+eh), (255,0,0), 5)

    cv2.imshow("webcam", frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows