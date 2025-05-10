#LAB 3, FILE I/O

import fileinput

str(input("Enter file name: " )) #asks for the name of file
poem = 'Poem.txt' #poem is selected and linked to the file


for line in fileinput.input (files=poem): #prints poem lines
    print (line)

str(input ( " Enter end file name: "))
poemend = 'PoemEnd.txt'

for line in fileinput.input (files=poemend):
    print (line)


