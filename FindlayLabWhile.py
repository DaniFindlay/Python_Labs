#Constant for an elliptical.



m= "Minutes"
c= "Total calories"


calories = 4.8
start = 1 #the starting point is 1 minute
end =  int(input('''How many minutes will you use the elliptical? Enter a number.
  ''')) #the end is determined by the user, this will dictated how long the loop needs to run. If end is not placed, the loop will contniue forever.


print ("%-8s %-8s" %(m, c)) #Prints the minutes, and calories, titles. the 8's establish the character wide.
    

while start <= end: #where the loop starts and where it ends.
   
    
    
    burned = start * calories #the formula to find the total of calories

    
    print( f"{start:4}  {burned:12.2f} ") #printing the results. the 4 and 12 determined the character wide in order to match the example. .2f helps to show only 2 decimals.
    
    start +=1 
   
