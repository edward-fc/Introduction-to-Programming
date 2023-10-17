import random

def GuessingGame():
    #choosing the number
    CorrectNumber=random.randint(1,100)
    winner=False
    for i in range(5):
        #User Guess
        User = input("The game will give the player a clue each time the player guesses the wrong number, either printing too high or too low. In the event if the player guessing the number correctly the number correctly the game will congratulate the player.")
        if int(User) > CorrectNumber:
            print("too High")
        elif int(User) < CorrectNumber:
            print("too Low")
        else:
            print("you have won")
            winner=True
    if not(winner):
        print("youhave exceded the number of authorised guess wich is 5. you have lost.The number was {}".format(CorrectNumber))
GuessingGame()