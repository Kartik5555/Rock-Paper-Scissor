# Rock Paper Scissor
# From random function choose randint as it will helps us to select random number by a computer
from random import randint
moves = ["rock","paper","scissors"]

# We will set True so that the loop continues
while True:

    # It generates random integer from moves
    computer = moves[randint(0, 2)]

    # Lower makes the input in lower case
    player = input("Choose one from below : \n1.Rock\n2.Paper\n3.Scissors\n4.End game ? \n").lower()
    print("You choose -->> ",player)
    print("Computer choose -->> ",computer)
    if player == "end game":
        print("The game has ended.... :)\nHope you enjoyed the game....... :)")
        break
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!, ",computer," covers ",player)
        else:
            print("You win! ",computer, " smashes ",player)
    elif player == "paper":
        if computer == "scissors":
            print("You lose! ",computer," cut ", player)
        else:
            print("You win! ",computer, " covers ",player)
    elif player == "scissors":
        if computer == "rock":
            print("You lose! ",computer, " smashes ",player)
        else:
            print("You win! ",player," cut ",computer)
    else:
        print("That's not a valid play. Check your spelling....")