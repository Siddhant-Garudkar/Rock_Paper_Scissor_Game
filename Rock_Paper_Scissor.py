import random
list = ["Rock","Paper","Scissor"]
com = random.choice(list)
player = input("Enter your Move[Rock,Paper,Scissor]:")
if(player not in list):
    print("Your Move is Invalid")
# tie
if (com == "Scissor") and (player == "Scissor"):
    print("Computer Move is",com,"Tie")
if (com == "Paper") and (player == "Paper"):
    print("Computer Move is",com,"Tie")
if (com == "Rock") and (player == "Rock"):
    print("Computer Move is",com,"Tie")
#   Win
if (com == "Rock") and (player == "Paper"):
    print("Computer Move is",com,"You Win")
if (com == "Scissor") and (player == "Rock"):
    print("Computer Move is",com,"You Win")
if (com == "Paper") and (player == "Scissor"):
    print("Computer Move is",com,"You Win")
# Lose
if (com == "Paper") and (player == "Rock"):
    print("Computer Move is",com,"You Lose")
if (com == "Scissor") and (player == "Paper"):
    print("Computer Move is",com,"You Lose")
if (com == "Rock") and (player == "Scissor"):
    print("Computer Move is",com,"You Lose")