    

print("\nWelcome to Rock, Paper, Scissors!\n")
while True:
    
    player1 = input("Player 1, enter R, P or S: ")
    if player1 not in ["R", "P", "S"]:
        print("Invalid input, please try again")
        continue
    player2 = input("Player 2, enter R, P or S: ")
    if player2 not in ["R", "P", "S"]:
        print("Invalid input, please try again")
        continue

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "R":
        if player2 == "S":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player1 == "P":
        if player2 == "R":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player1 == "S":
        if player2 == "P":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    else:
        print("Invalid input, please try again")
        