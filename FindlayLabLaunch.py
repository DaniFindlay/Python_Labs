import os
import time
import subprocess



def launch_program(program_path, delay_seconds):#creates the launch def, 
    time.sleep(delay_seconds)#defines de delay of secons and it is place in the main
    subprocess.Popen(program_path, shell=True)

def main():
    # Specify the file paths and delays
    file= input("Enter Name of Image:")
    file2= input("Enter Name of audio")
    file1 = (r"C:\Users\danif\OneDrive\Desktop\zophie.jpg") #gets the file but does not link with the input, it only gets it becasue I traced the path.
    file2 = r"C:\Users\danif\OneDrive\Desktop\ScotsWhaHae.mp3"
    image_delay = 5  # 5 seconds
    sound_delay = 3  # 3 seconds

    # Launch Paint (or a similar program) with the image file
    launch_program("mspaint.exe " + file1, image_delay)

    # Launch Media Player (or a similar program) with the sound file
    launch_program("wmplayer.exe " + file2, sound_delay)

if __name__ == "__main__":
    main()
#This was very difficult for me, and I was not able to succesfull accomplish. I have requested help from the tutoring services and I am waiting for answer back. Meanwhile-
#if there is a way I could get an example of how this was supposed to be done, that would be wonderful so I can see where and how I failed and learn from it. Thank you.
    
