import random

def theResult(player,cpu):
    if(player=="S"):
        player="Scissor"
    elif(player=="P"):
        player="Paper"
    else:
        player="Rock"
    
    if(cpu=="S"):
        cpu="Scissor"
    elif(cpu=="P"):
        cpu="Paper"
    else:
        cpu="Rock"
    
    print("Player - "+player+" vs CPU - "+cpu)


play=True
while(play):
    print("the game is starting")
    print("Usage: Input  P for Paper, R for Rock or S for Scissor, let the game begin!")
    playerChoice=input("Please, Introduce your choice:[P,R or S]:")

    if playerChoice == "S" or playerChoice == "R" or playerChoice == "P":
        
        myChoices=["R","P","S"]
        pcChoice=random.choice(myChoices)

        if pcChoice == playerChoice:
            print("it's a tie, no one wins, no one loses!!")
        else:
            if (playerChoice=="P" and pcChoice=="R") or (playerChoice=="S" and pcChoice=="R") or (playerChoice=="P" and pcChoice=="S"):
                print("The PC is the winner!")
                theResult(playerChoice,pcChoice)
                play=False
            else:
                print("You are the winner!")
                theResult(playerChoice,pcChoice)
                play=False

    else:
        print("Wrong entry, please Try again!")