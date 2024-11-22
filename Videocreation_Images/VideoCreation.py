import cv2
import os

path ="C:/Hema/PythonForVS/Assignments/ImageProcessing/Videocreation"
video_name="Sunset.avi"
video_secs=1

images=[]

for file in os.listdir(path):
    #seperate the name and extension
    name,extension=os.path.splitext(file)
    if extension in ['.JPG','.jpeg','.jpg']:
        file_name=path+ '/'+file
        images.append(file_name)
        #print("File Names : ", images)
    frame=cv2.imread(os.path.join(path, images[0]))
    height, width, layers = frame.shape
    print(height, width, layers )

#img_count=len(images)
#print("Images count: ",img_count )
print("Images", images)


video=cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 1.0, (width,height))

for img in images:
    for _ in range(video_secs):
        video.write(cv2.imread(os.path.join(path,img)))
        #if cv2.waitKey(20)==32:
            #break

cv2.destroyAllWindows()
video.release()
    



#read the images, write the images, 
#using video writer create a video using the images, use - shape properties
#use a for loop and conver all the images and create a video.