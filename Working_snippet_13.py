import time
import winsound

#function definition
def countdown_timer(seconds):
    while seconds > 0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        # 1:15 if total seconds are 75
        print(timer)
        time.sleep(1)
        seconds -=1 # or seconds=seconds-1
    print("time up!")

    file="C:\\Hema\\PythonForVS\\1secondton_87a501f05076308.mp3"
    winsound.PlaySound(file, winsound.SND_FILENAME)

#input time in seconds
seconds=input("Enter the time in seconds: ")

#function call
countdown_timer(int(seconds))