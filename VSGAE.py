#VSGAH - Video Subtitle Generator And Hardcoder
import os
import tkinter as tk
from tkinter import filedialog
import webbrowser

root = tk.Tk()
root.withdraw()
path1 = filedialog.askopenfilename(initialdir = "/",title = "Select Video File")
subtitleSBV = path1.split('/')[-1].split('.')[0] + '.sbv'
subtitleSRT = path1.split('/')[-1].split('.')[0] + '.srt'
vid = path1.split('/')[-1]
path1 = '/'.join(path1.split('/')[:-1])
path1 = path1.replace('/','\\')

def subHardcode(vid,subtitle):
    s2 = "ffmpeg -i {} -vf subtitles={} result.mp4".format(vid,subtitle)
    s1 = "cd " + path1
    os.system("cmd /k \"" + s1 + " & " + s2 + "\"")
    print("Result.mp4 is the final vid + subtitles!")

def youup():
    p1 = os.getcwd()
    y1 = "cd " + p1
    y2 = "python upload_video.py --file=\"" + path1 + "\\" + vid +"\"" + " --title=\"" + vid[:-4] + "\"" + " --privacyStatus=\"unlisted\""
    print("Close the CMD window when the process is done and make sure you note the video ID")
    os.system("cmd /k \"" + y1 + " & " + y2 + "\"")
    print("Now, on youtube studio, on your left panel go to videos>click on latest video>More Options>Under Video Language choose English.")
    print()
    print("Now wait for an hour or two so youtube can auto generate your subtitles. After that on your left hand panel click on subtitles and under the option English(Auto Generated), Download as .sbv")
    print()
    print("Proceed to answer the next question only after you download your subtitles. Even if you quit the program its fine, you can choose to hardcode subtitle later by running the program again.") 
    s = 'https://studio.youtube.com/'
    webbrowser.open(s)

x1 = int(input("Do you want to generate a subtitle for your video(1) or hardcode existing subtitle(2)?"))
if x1 == 1:
    youup()
    print("Move the .sbv file to the same folder as your video and rename it to the same name as that of the video.")
    print("Once you do that, you can open your .sbv file using a notepad and edit if you want")
    x2 = input("Do you want to hardcode the subtitles into the video? (y/n)")
    if x2 == 'y':
        subHardcode(vid,subtitleSBV)
    elif x2 == 'n':
        print("Alright bye")
    else:
        print("Error! Invalid Input. Run the program again")
elif x1 == 2:
    print("Move the subtitle file to the same folder as your video and rename it to the same name as that of the video.")
    x3 = int(input("Is your subtitle file .srt(1) or .sbv(2)?"))
    if x3 == 1:
        subHardcode(vid,subtitleSRT)
    elif x3 == 2:
        subHardcode(vid,subtitleSBV)
    else:
        print("Error! Invalid Input. Run the program again")
else:
    print("Error! Invalid Input. Run the program again")
    
