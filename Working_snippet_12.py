# reference link - https://pythonhosted.org/watchdog/
import os
import shutil
import time
import random

#filesystemeventhandler observer class of watchdog module
# look for changes in the path mentioned, and call the specific event handler

from watchdog.observers import Observer
# event handler class that manages the file system events(eg. creation, movenment, renaming, deleting files)
from watchdog.events import FileSystemEventHandler

# paths

from_dir="C:/Users/bmsat/Downloads"
to_dir="C:/Hema/PythonForVS/TestmkDir/DownloadedFiles"

dir_tree={
    "Image_Files":[".jpeg",".jpg",".JPG",".JPEG",".png",".gif",".PNG"],
    "Video_Files":[".mp3",".mp4",".mov"],
    "Document Files":[".ppt",".csv",".doc",".pdf"]
}

# Creating class FileMovementHandler and pass FileSystemEventHandler as parameter to use all the attributes and methods from it
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self,event):
        name,extension=os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("Downloaded"+file_name)

                path1= from_dir+'/'+file_name
                path2= to_dir+'/'+key
                path3= to_dir+'/'+key +'/'+file_name 
                path4= to_dir+'/'+'/'+key +'/'+file_name +str(random.randint(0,999))

                if os.path.exists(path2):
                    if os.path.isfile(file_name):
                        shutil.move(path1, path4)
                        print("Directory Exists-Renaming")
                    else:
                        print("Directory Exists")
                        print("moving"+ file_name +"...")
                        shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("Making Directory..")
                    os.makedirs(path2)
                    print("Moving"+file_name+"...")
                    shutil.move(path1,path3)
                    time.sleep(1)

#initialize variable eventhandler class-creating objects
event_handler=FileMovementHandler()
observer=Observer()
#recursive=true - observes changes in sub folders as well
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()