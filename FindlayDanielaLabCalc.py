#LAB CALCULATIONS BY DANIELA FINDLAY


#This will calculate the compoud Interest earned.

#equation:  A= P (1+ r/n)^nt



P = int(input("Enter original amount: ")) # P is the original amount
r = float(input("Enter rate of interest: " ))# r is the interest rate since the input is in decimals I will use float for the input
n = int(input("Enter number of times a year, 12 for monthly, 4 for quartly or 1 for yearly: "))# n is the number of times a year interest is compounded.
t = int(input("Enter the number of years: "))# t is the number of years.

A=P*(1+(r/n))**(n*t) #A represents the money earned + the original amount.

ci=A-P  #ci will represent the compound intereset earned.

print("Your Compound interest is", ci) #displays the calculation of the compound interest earned. 
    
