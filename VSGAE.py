#VSGAH - Video Subtitle Generator And Hardcoder
import os
import tkinter as tk
from tkinter import filedialog




def subHardcode(vid,subtitle):
    root = tk.Tk()
    root.withdraw()
    print("Put both video and subtitle in same folder")

    path1 = filedialog.askopenfilename(initialdir = "/",title = "Select Video File")
    subtitle = path1.split('/')[-1].split('.')[0] + '.srt'
    vid = path1.split('/')[-1] 
    path1 = '/'.join(path1.split('/')[:-1])
    path1 = path1.replace('/','\\')
    
    s2 = "ffmpeg -i {} -vf subtitles={} result.mp4".format(vid,subtitle)
    s1 = "cd " + path1
    #print("cmd /k \"" + s1 + " & " + s2 + "\"")
    os.system("cmd /k \"" + s1 + " & " + s2 + "\"") 
    #os.system('cmd /k ' + "\"" + s + "\"")

subHardcode(vid,subtitle)
