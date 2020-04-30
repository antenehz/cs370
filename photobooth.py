import Tkinter as tk
import os
    

def play_music():
	os.system("python newdetector2.py")
def take_snapshot():
	os.system("fswebcam /home/pi/pi-detector/faces/image.jpg")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="SNAP", 
                   fg="red",
                   command=take_snapshot)
button.pack(side=tk.LEFT)
music = tk.Button(frame,
                   text="PLAY",
	           fg="blue",
                   command=play_music)
music.pack(side=tk.LEFT)

root.mainloop()
