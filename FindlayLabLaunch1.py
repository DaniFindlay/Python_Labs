import time
import subprocess


image_file = input("The image file name: ")#asks inout and later is used for the subprocess Popen
subprocess.Popen (["mspaint.exe ", image_file ])#displays the file.
time.sleep(5)#schedules the program

sound_file = input("Enter the sound file name: ")#ask for input and sets the sound_file for the popen process
subprocess.Popen (["wmplayer.exe", sound_file])#plays the sound with program
time.sleep(3)#schedules the program

