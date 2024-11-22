# Video: FPS:Frames Per Second - measure of how fast the images are transitioning (40 fps: 40 images)

import cv2

#vid=cv2.VideoCapture(0)

vid=cv2.VideoCapture("VID_20210630_112419.mp4")

if (vid.isOpened()==False):
    print("Unable to read the feed")

height= int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Height: ",height)

width= int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Width: ",width)

fps=int(vid.get(cv2.CAP_PROP_FPS))
print("FPS: ",fps)

out=cv2.VideoWriter("Videoname.mp4",cv2.VideoWriter_fourcc(*"XVID"),30,(width,height))
while(True):
    ret,frame=vid.read()
    cv2.imshow("video display", frame)
    out.write(frame)
    if cv2.waitKey(20)==32:
        break
vid.release()
out.release()
cv2.destroyAllWindows()