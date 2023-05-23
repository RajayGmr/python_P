import random
while True:
    choice = ["rock","papper","scissors"]
    computer = random.choice(choice)
    player = None
    while player not in choice:
        player = input("Rock, Papper, or Scissors?: ").lower()

    if player == computer:
        print("Player :", player)
        print("Computer :", computer)
        print("Draw")
    elif player == "rock":
        if computer == "paper":
            print("Player :", player)
            print("Computer :", computer)
            print("You Lose")
        elif computer == "scissors":
            print("Player :", player)
            print("Computer :", computer)
            print("You win")
    elif player == "papper":
        if computer == "rock":
            print("Player :", player)
            print("Computer :", computer)
            print("You win")
        elif computer == "scissors":
            print("Player :", player)
            print("Computer :", computer)
            print("You lose")
    elif player == "scissors":
        if computer == "paper":
            print("Player :", player)
            print("Computer :", computer)
            print("You win")
        elif computer == "rock":
            print("Player :", player)
            print("Computer :", computer)
            print("You lose")

    play_again = input("Wanna Play again?(yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")



