#Game with random numbers.

from random import randint #import randint

moves = ["rock", "paper", "sicssors", "lizard", "spock"]#these are the options

while True:
    computer = moves[randint(0,4)] #the options are assign an int
    player = input ('''
This is a game, you need to type the items you chose and the computer will choose a random item, type your option:
rock, paper, sicssors, lizard or spock
(if you are done playing type "done")
''').lower()
    if player == "done": #typing done will break the loop
        print ("Game Over. Thanks for playing")
        break
    elif player == computer:#confusing in this part, it should generate the tie in every time they get the same result howvere I was not sure if i should not type the other option below.
        print("Tie!")
        #each round has its own if statements that will run the loop and in each the random number is auto assign to a word. 
    elif player == "rock":
        if computer == "paper":
            print(computer, "covers", player, ", you lose.")
        if computer == "lizard":
            print(player, "crushes", computer, ", you win.")
        if computer == "spock":
            print (computer, "vaporizes", player, ", you lose.")
        if computer == "scissors":
            print(player, "destroys", computer, ", you win!")

    elif player == "paper":
      #  if computer == "paper":
       #     print("Tie!")
        if computer == "rock":
            print(player, "covers", computer, ", you win!")
        if computer == "sicssors":
            print(computer, "cuts", player, ", you lose!")
        if computer == "spock":
            print(player, "disproves", computer, 'you win')
        if computer == "lizard":
            print(computer, "eats", player, ", you lose!")

    elif player == "scissors": 
        #if computer == "scissors":
        #    print("Tie!")
        if computer == "paper":
            print(player, "cuts", computer, ", you win!")
        if computer == "rock":
            print(computer, "destroys", player, ", you lose!")
        if computer == "lizard":
            print(player, "decapitates", computer, ", you win!")
        if computer == "spock":
            print(computer, "smashes", player, ", you lose!")

    elif player == "lizard":
       # if computer == "lizard":
       #     print("Tie!")
        if computer == "rock":
            print(computer, "crushes", player, ", you lose!")
        if computer == "paper":
            print(player, "eats", computer, ", you win.")
        if computer == "sicssors":
            print(computer, "decapitates", player, ", you lose.")
        if computer == "spock":
            print(player, "poisons", computer, ", you win")

    elif player == "spock":
       # if computer == "spock":
        #    print("Tie!")
        if computer == "rock":
            print(player, "vaporizes", computer, ", you win")
        if computer == "paper":
            print(computer, "disproves", player, " you lose")
        if computer == "sicssors":
            print(player, "smashes", computer, ", you win")
        if computer == "lizard":
            print(computer, "poisons", player, ", you lose")
            
            
        
    
