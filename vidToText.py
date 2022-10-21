from turtle import color
import cv2
from pathlib import Path
from termcolor import colored
import time
import os




colorEnabled = True
lines = 60
chars = 60
fps = 60

def move (y, x):
    print("\033[%d;%dH" % (y, x))
    
def startScreen():
    temp = "<"

    for i in range((chars - 3 - len(str(chars)))//2):
        temp = temp + "-"
    temp = temp + str(chars)

    for i in range((chars - 2 - len(str(chars)))//2):
        temp = temp + "-"
    temp = temp + ">"
    print(temp)
    print("^                   Please adjust terminal to this size                        ")
    for i in range(lines - 3):
        print("|")
    input("\/")



def clear():
    for i in range(lines):
        print("\n")

def printFrame(frame):
    #os.system('cls' if os.name == 'nt' else 'clear')
    #clear()
    move(0,0)
    out = ""
    vals = [0,0,0]
    for i in range(lines):
        out = out + "\n"
        for x in range(chars):
            for y in range(2):
                vals[y] = frame[i,x,y]
                if(colorEnabled == True):
                    if(vals[0] == 0 and vals[1] == 0 and vals[2] == 0):
                        out = out + colored('▓', 'grey')
                    elif(vals[0] > 85):
                        if(vals[1] > 85):
                            out = out + colored('▓', 'yellow')
                        elif(vals[2] > 85):
                            out = out + colored('▓', 'magenta')
                        else:
                            out = out + colored('▓', 'red')

                    elif(vals[1] > 85):
                        if(vals[2] > 85):
                            out = out + colored('▓', 'cyan')
                        else:
                            out = out + colored('▓', 'green')
                    elif(vals[2] > 85):
                            out = out + colored('▓', 'blue')
                    else:
                        out = out + (" ")
                else:
                    if(vals[0] < 127 and vals[1] < 127 and vals[2] < 127):
                        out = out + colored('▓', 'grey')
                    else:
                        out = out + colored('▓', 'white')
    print(out)


    







#startScreen()
vidName = input("Please enter the name of the video:\n--> ")


my_file = Path("./" and vidName)
if not my_file.is_file():
    print("Error. Enter a valid file name. The file may be located in any sub directory of the current directory.")
    vidName = input("Please enter the name of the video:\n--> ")
    my_file = Path("./" and vidName)

yn = input("Do you want to disable the color? (Y/N): ")
while(yn != "y" and yn != "n" and yn != "Y" and yn != "N"):
    print("Error. Please enter 'Y' for yes and 'N' for no")
    yn = input("Do you want to disable the color? (Y/N): ")
print("yn:", yn)
    
if(yn == "N" or yn == "n"):
    print("Color enabled.")
    colorEnabled = True
else:
    print("Color disabled")
    colorEnabled = False
print(str(colorEnabled))


print("Please wait, loading video.")
vidcap = cv2.VideoCapture(vidName)
dir = os.getcwd()

print("Loading complete.")

input("Press any key to start...")

success,image = vidcap.read()
count = 0

os.system('cls' if os.name == 'nt' else 'clear')
while success:
    frame = cv2.resize(image,(chars,lines),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    printFrame(frame)
    success,image = vidcap.read()
    count += 1
    #time.sleep(1/fps)