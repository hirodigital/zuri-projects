
import random

while True:

    aleatory = random.randrange(0, 3) 

    cpu = ""
    print("1.rock")
    print("2.paper")
    print("3.scissors")
    option = int(input("choose your option"))

    if option == 1:
        player = "rock"
    elif option == 2:
        player = "paper"
    elif option == 3:
        player = "scissors" 

        print("yourchoose:",player)  

    if aleatory == 0:
         cpu = "rock"
    elif aleatory == 1:
         cpu == "paper" 
    elif aleatory == 2:
         cpu == "scissors" 

    print("thePcchoose:",cpu) 
    print("...") 
 
    if cpu == "rock" and player == "paper":
        print("you win, paper beats rock")
    elif cpu == "paper" and player == "scissors":
         print("you win, scissors beats paper")
    elif cpu == "scissors" and player == "rock":
         print("you win, rock beats scissors")
    elif cpu == "paper" and player == "rock":
         print("you lost, paper beats rock")
    elif cpu == "scissors" and player == "paper":
         print("you lost, scissors beats paper")
    elif cpu == "rock" and player == "scissors":
         print("you lost, rock beats scissors")
    elif cpu == player :
         print("tie")


    play_again= input("do you want to play again? (s/n)")
    if play_again.lower() != "s":
       break
