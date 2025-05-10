import datetime

# Get the current date from the user
current_day = int(input("Enter the current day: "))
current_month = int(input("Enter the current month: "))
current_year = int(input("Enter the current year: "))

# Create a datetime object for the current date
current_date = datetime.date(current_year, current_month, current_day)

# Define the event dates
napoleon_birthdate = datetime.date(1769, 8, 15)
pearl_harbor_bombing = datetime.date(1941, 12, 7)
wright_brothers_flight = datetime.date(1903, 12, 17)

# Calculate time differences
napoleon_difference = current_date - napoleon_birthdate
pearl_harbor_difference = current_date - pearl_harbor_bombing
wright_brothers_difference = current_date - wright_brothers_flight

# Print the results
print(f"Time difference with Napoleon Bonaparte's birthdate: {napoleon_difference.days} days")
print(f"Time difference with Pearl Harbor bombing: {pearl_harbor_difference.days} days")
print(f"Time difference with Wright Brothers' 1st Flight: {wright_brothers_difference.days} days")



******************************************


harbor = input("When was the Pearl Harbor bombed?(Please enter date in the following format, m-dd-yyyy")
time=datetime.datetime.strptime(harbor, "%m-%d-%Y")

wright = input("What date was the Wright Brother's First flight? (Please enter date in the following format, m-dd-yyyy")
time=datetime.datetime.strptime(wright, "%m-%d-%Y")
wright = datetime.date (12, 17, 1903)

napoleon_difference = current_date-napoleon
harbor_difference = current_date-harbor
wright_difference = current_date-wright

print(f"Time difference with Napoleon Bonaparte's birthdate: {napoleon_difference.days} days")
print(f"Time difference with Pearl Harbor bombing: {harbor_difference.days} days")
print(f"Time difference with Wright Brothers' 1st Flight: {wright_difference.days} days")


************************************************


def launch_image(image_path):
    # Open the image file using Paint (or a similar program)
    paint_path = "C:\\Windows\\System32\\mspaint.exe"  # Path to Paint executable
    subprocess.Popen([paint_path, image_path])
    print(f"Image file '{os.path.basename(image_path)}' opened in Paint.")
    time.sleep(5)  # Delay of 5 seconds

def launch_sound(sound_path):
    # Open the sound file using Media Player (or a similar program)
    media_player_path = "C:\\Program Files\\Windows Media Player\\wmplayer.exe"  # Path to Media Player executable
    subprocess.Popen([media_player_path, sound_path])
    print(f"Sound file '{os.path.basename(sound_path)}' opened in Media Player.")
    time.sleep(3)  # Delay of 3 seconds

# Example usage:
image_file_path = "path/to/your/image.png"
sound_file_path = "path/to/your/sound.mp3"

launch_image(image_file_path)
launch_sound(sound_file_path)
