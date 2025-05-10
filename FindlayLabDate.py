import datetime

print("Hello! today we are going to calculate dates!")
year = 365

#Get current date from user.
current_day = int(input("Enter the current day(type 1-12): "))
current_month = int(input("Enter the current month (type 1-31): "))
current_year = int(input("Enter the current year(four digits): "))

# Create a datetime object for the current date
current_date = datetime.date(current_year, current_month, current_day)
print("Today is ", current_date, "\n ")


print("Great! now, let's go to the next step.\n")
#I am pretty sure I could have use def here, but I was not able to make it work
napoleon_day = int(input("What day was Napoleon Bonaparte born? (type 1-31)"))#asks for day
napoleon_month = int(input("What month was Napoleon Bonaparte born? (type 1-12)"))#asks for month
napoleon_year = int(input("What year was Napoleon Bonaparte born?(four digits) "))#asks for year

napoleon_birthdate = datetime.date(napoleon_year, napoleon_month, napoleon_day)#takes de day, month and year into one
print("While today is", current_date, " Napoleon's birth was:", napoleon_birthdate)

napoleon_difference = (current_date - napoleon_birthdate)#make the calculation, birthdate minus today

print("Napoleon Bonaparte was born: ", napoleon_difference, "ago ")#prints the result in days
inyearsNapo =(napoleon_difference / 365)#divides the result in 365, to find years

print("Which makes it", inyearsNapo, "years ago\n")#prints how many years, however I was not able to either removed the days count word nor the time. 




harbor_day = int(input("What day was the Pearl Harbor attacked? (type 1-31)"))  
harbor_month = int(input("What month was the Pearl Harbor attacked? (type 1-12)"))
harbor_year = int(input("What year was the Pearl Harbor attacked? (four digits) "))

harbor_date = datetime.date(harbor_year, harbor_month, harbor_day)
harbor_difference = (current_date - harbor_date)
print("While today is", current_date, " The pealr Harbor was bombed on:", harbor_date)

print("The Pearl Harbor was bombed ", harbor_difference, "ago")
inyearsHarbor = (harbor_difference / 365)
print("Which make it", inyearsHarbor, "years ago\n")



wright_day = int(input("What day did the Wright Brothers flight the first time? (type 1-31)"))
wright_month = int(input("What month did the Wright Brothers flight the first time? (type 1-12)"))
wright_year = int(input("What year did the Wright Brothers flight the first time??(four digits) "))

wright_date = datetime.date(wright_year, wright_month, wright_day)
wright_difference = (current_date - wright_date)
print("While today is", current_date, " The Wright Brothers event was on:", wright_date)

print("The Wright Brothers made their first flight ", wright_difference, "ago")
inyearsBrothers = (wright_difference /365)
print(" Which makes it" , inyearsBrtohers, "years ago\n")




