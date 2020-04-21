from tkinter import *
window = Tk()
window.title("Rock, Paper, Scissors")
window.mainloop()
print("Made by Daman Rao")
loose = ("The computer wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
    print("To begin fill in the below information.")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    searchfile = open("accounts.csv", "r")
    for line in searchfile:
        if username and password in line:
            print("Access Granted")
            print("Live Rules")
            print("You start with",lives,"lives")
            print("If you lose you loose a live")
            print("If you draw the lives stay the same")
            print("----------------------------------------")
            print("DON'T USE CAPITALS")
            print("----------------------------------------")
            print("To see a list of rules type rules")
            print("------------------------------------------")
            print("At any point type exit to leave the game")
            print("----------------------------------------")
            print("The computer has lives as well")
            print("Can you beat the computer!")
            print("Good Luck!")
            print("----------------------------------------")
            while True:
                rps = input("Rock, Paper, Scissors?   ")
                import random
                computer = ("Rock", "Paper", "Scissors")
                computer = random.choice(computer)
               #rock if statements
                if rps == "Rock" and computer == "Paper":
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                if rps == "Rock" and computer == "Scissors":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    print("")
                    score+=1
                #paper if statements
                if rps == "Paper" and computer == "Rock":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                if rps == "Paper" and computer == "Scissors":
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                #scissor if statements
                if rps == "Scissors" and computer == "Paper":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    computer_lives-=1
                    print("")
                    print("")
                    score+=1
                if rps == "Scissors" and computer == "Rock":
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    print("")
                    lives-=1
                #duplicates
                if rps == "Rock" and computer == "Rock":
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew+=1
                if rps == "Paper" and computer == "Paper":
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew+=1
                if rps == "Scissors" and computer == "Scissors":
                    print("The computer choose",computer)
                    print("")
                    print("You Drew")
                    print("")
                    print("")
                    drew+=1
                #system
                if rps == "Rules":
                    print("****************************************")
                    print("Rules")
                    print("****************************************")
                    print("-Rock loses against Paper")
                    print("-Rocks beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper loses against Scissors")
                    print("-Scissors beats Papers")
                    print("Scissors loses against Rock")
                    print("****************************************")
                if rps == "Display Lives":
                    print(lives)
                if rps == "Display Score":
                    print(Score)
                if rps == "Display Draw":
                    print(drew)
                #lives
                if lives == 0 or rps == "test":
                    print("Thank for Playing my Game!")
                    print("You have run out of lives")
                    print("You got",score,"correct")
                    print("You drew",drew,"times")
                    stop = input("Press enter to exit.")
                    import time
                    time.sleep(900)
                if computer_lives == 0:
                    print("Thanks for Playing my Game!")
                    print("The computer lost all it's lives. You win.")
                    print("You got",score,"correct")
                    print("You drew",drew,"times")
                    stop = input("Press enter to exit.")
                    import time
                    time.sleep(900)
                #exit
                if rps == "Exit":
                    break
        else:
            print("Your username or password is incorrect.")
            print("--------------------------------------.")
