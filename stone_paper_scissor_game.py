# stone paper scissor game
import random
print("|---------------------------|")
print("  STONE, PAPER AND SCISSOR  ")
print("|---------------------------|")
name = str(input("Enter your name\n"))
print("Write stone,paper and scissor for play the game\n")
ready = str(input("Are you ready to play the game (yes/no)?\n"))
if ready == "yes" :
    print("Ok!! Good luck")
    print("Your Turn",name)
    user = str(input())
    print("Computer Turn")
    list1 = ["stone","paper","scissor"]
    computer = random.choice(list1)
    print(computer)
    if user == "stone" and computer == "stone" :
        print("Match Draw")
    elif user == "paper" and computer == "paper" :
        print("Match Draw")
    elif user == "scissor" and computer == "scissor" :
        print("Match Draw")
    elif user == "stone" and computer == "paper" :
        print("Computer Won")
    elif user == "stone" and computer == "scissor" :
        print(name,"won")
    elif user == "paper" and computer == "stone" :
        print(user,"won")
    elif user == "paper" and computer == "scissor" :
        print("computer won")
    elif user == "scissor" and computer == "stone" :
        print("computer won")
    elif user == "scissor" and computer == "paper" :
        print(user,"won")
    else :
        print("you Entered the wrong keyword")

elif ready == "no" :
    print("OK!! you doesn't want to play")
    exit()