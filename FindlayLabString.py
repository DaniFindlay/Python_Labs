#first define the functions, 3 different ones for ssn, phone numbers and zip codes.

# Defines de ssn and searchs for Social security pattern: 
def search_ssn(text):
    ssn_count = 0 #starts on zero
    for line in text.splitlines(): #splits the lines
        for word in line.split(): #splits the words
            if len(word) == 11 and (word[3] == '-' or word[3] == '.'): #leng is 11 and looks for those that have only 11 and devided by - or . (OR adds the ability to look for a different lay out such as:  DDD-DD-DDDD OR DDD.DD.DDDD
                ssn_count += 1#adds each match that has the pattern into the count
    return ssn_count #returns the ssn count total

# Defines the search for phone numbers
def search_phone(text):
    phone_count = 0#starts 0
    for line in text.splitlines(): #split lines
        for word in line.split(): #split words
            if len(word) == 12 and word[3] == '-' and word[7] == '-':#length of 12 as of DDD-DDD-DDDD. DIVIDED BY - ONLY.
                phone_count += 1#adds each to the count total
    return phone_count#returns the final

# Defines the functions and search for zip codes
def search_zip(text):
    zip_count = 0#starts on 0
    for line in text.splitlines():#splits for lines
        for word in line.split():#splits by words
            if len(word) == 5 or (len(word) == 10 and word[5] == '-'):#length of 5, which looks for the 5 digits first, and OR allows 10 diggits lookup. divided by '-'.
                zip_count += 1#Adds to the count every time the pattern is found
    return zip_count #returns the total coutn

#Defines the main, this is the one that runs the fucntions and file. 
def main():
    # Ask the user the name of th file
    file_name = input("File name: ")

    try:
        # Opens the file
        with open(file_name, 'r') as file:
            content = file.read()#reads the file and saves as content

            # Search for the patterns in the file for each fucntion. ssn, phone and zipcode
            ssn_count = search_ssn(content)
            phone_count = search_phone(content)
            zip_count = search_zip(content)

            # Print the results
            print(f"Total of Social Security Numbers found: {ssn_count}")
            print(f"Toral of phone numbers found: {phone_count}")
            print(f"Total of ZIP Codes found: {zip_count}")

    except FileNotFoundError:# except displayed if file not found.
        print(f"File '{file_name}' not found. ")
if __name__ == "__main__":#Executes 
    main()#closes the main
