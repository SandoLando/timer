import time
import winsound
import os
import datetime
import sys
from pynput import *


# A countdown style timer that you can you pick how many minutes to set for
def timer():
    minutes = 0
    seconds = 60  
    while True:
        try:
            length = int(input("How many minutes would you like to set the timer for?\n"))
        except ValueError:
            print("Please enter numbes only.")
            time.sleep(1)
            continue
        break
    print("Timer has begun")
    
    if length > 1:
        minutes = length
    minutes -= 1
    while True:
        time.sleep(1)
        seconds -= 1
        print("Time reamaining:", minutes ,":", seconds , end="\r")
        if seconds == 0:
            minutes -= 1
            seconds = 60       
        if minutes == -1:
            winsound.Beep(2500,2000)
            print("\n")
            print("Timer Done! \n")
            break

            
def stop_watch():
    seconds = 0
    minutes = 0
    hours = 0
    while True:
        time.sleep(1)
        seconds += 1
        print("{}m {}s".format(minutes,seconds), end='\r')
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes >= 60:
            minutes = 0
            hours += 1
            print("{}h {}m {}s".format(hours,minutes,seconds), end='\r')
    
                
def clock_app():
    check = bool()
    while check != True:
        select = input("Would you like to use the 'timer' or the 'stopwatch'? ")
        if "timer" in select:
            timer()
            check == True
        elif "stopwatch" in select:
            stop_watch()
            check == True
        else:
            print("That is not a valid selection! Please try again.")
            time.sleep(1.5)
            os.system('cls')
            select == False
            
            
if __name__ == "__main__":
    clock_app()
    
