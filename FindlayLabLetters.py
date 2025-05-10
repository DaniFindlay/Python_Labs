
#functions to count vowels
def count_vowels(s):#defines the function
    vowels = "AEIOUYaeiouy"#states the vowels that will be counted
    vowel_count= 0
    for char in s:
        if char in vowels:#condition, if vowels, count.
            vowel_count +=1
    return vowel_count#returns the total of vowels.

def consonant_count(s):#defines the fuction
    consonants =" BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"#states the consonants to be count
    consonant_count = 0
    for char in s:#create the conditions
        if char in consonants:
            consonant_count +=1#counts the consonants by adding each witha +1
    return consonant_count#retursn the total of consonants
        
def main():#defines the main fucntion, this takes the top fuctions and defines the outcome
    user_string = input("Enter a string:")#takes the users input
    vowels_total = count_vowels(user_string)#counts the vowels in the string, and and creates a total
    consonant_total = consonant_count (user_string)#counts the consonants from the input and creates the total


    print(" Vowel total in input is: ", vowels_total)#prints the total of vowels
    print("There is total of", consonant_total, "consonants")#prints the total of consonants

if __name__=="__main__":#executes the code
    main()#closes the main
