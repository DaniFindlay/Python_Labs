#IF statements fuctions.
#This Lab will have 5 option of functions.
#depending on the users election, the If statements will forward it-
#to a specific math equation.
#each if statement has its own formula and it will calculate each own problem,
#printing the answer at the end.



option= int(input('''There is 5 options for equations, 

1= find the area of a circle.
2= find the total miles per gallon.
3= find the total hours you work in the week.
4= what is the total cost of a product with 6.5% taxes.
5= fin the area of a triangle.

choose a number to select the function you wish to do:
                   '''))



if option == 1:
    d = int(input("what is the diameter of the circle?")) #asks for the users input d= diameter

    A=3.1416 * d **2 /4  #the formula uses the input to adjust the response. A= Area
    print ("The area of the circle is: ", A) #prints the response.

elif option == 2:
    D = int(input("What is the distance traveled?")) #D=distance
    g = int(input("Hoe many gallons of fuel were used?"))#g=gas
    m=D/g
    print("The Miles per gallon were:", m)
            
elif option == 3:
    h= int(input("how many hours did you work everyday?"))#h=hours
    d= int(input("how many days a week did you work?"))#d=days
    totalhours=h*d
    print("Congrats! you worked", totalhours, "hours this week!")

elif option == 4: #this has two equations to calculate the final cost.
    p=int(input("What is the price of the item?")) #p= price
    t=p*0.0625
    total= p+t
    print("The taxes on the item are:", t) #prints the taxes amount
    print("with a tax percetange of 6.5%, the total cost is:", total) #prints the total of the cost.

elif option == 5:
    b=int(input("What is the base of the triangle?")) #b=base
    H=int(input("What is the height of the triangle?"))#H=height
    at=1/2*b*H
    print("The area of the triangle is:", at)

else: 
  print("I'm sorry you need to select One of the Five options.")#when a wrong answer is enter, it tells the user to choose only one of the 5 options.
