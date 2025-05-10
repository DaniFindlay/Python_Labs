import random

#def ranges
lengthupper = 5
lengthlower = 3
 
#funtion 1, create Uppercase Random, 5 only defined by the ranges
def generate_random_uppercase():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(lengthupper))
#needs to add ABC manually in order to work, "string.ascii_uppercase" doesnt work 


#funtion 2, create random interger
def generate_random_interger(): 
    return random.randint(0,999)#creates de start and limit

#funtion 3, create 3 lower case letters
def generate_random_lowercase():    
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range (lengthlower))

#funtion 4,  create float number with a range and only 2 decimal place print.
def generate_random_float():
    return round(random.uniform(0, 9999.99),2)#creates the limit, plus ",2" defines the decimals
    

#defining the main

def final():
    try:
        #ask users for name, creates file, writes in file and prints
        fileName= input("Enter the file name:")
        with open (fileName, 'w') as file:
            for i in range (20):#runs ones, so you get a final once only
                upper= generate_random_uppercase()
                intnum= generate_random_interger()
                lower= generate_random_lowercase()
                floatnum= generate_random_float()
                finalresult = f"{upper} {intnum} {lower} {floatnum}\n" #pulls all the def together.
                file.write(finalresult)#writes the file
                print(finalresult.strip()) #prints the final def together

        print(f"{fileName} FILE CREATED") #prints file name
    except FileNotFoundError: #except needed in order to have the def main to work.
        print("File not found")
if __name__ == "__main__": #if the statement is not imported, it needs to execite to be able to initiate 
    final()
