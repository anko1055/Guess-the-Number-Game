import random

def guesstheNumberGame():
    min= int(input("min number:"))
    max=int(input("max number:"))
    if(min>max):
        return false
    randomNumber=int(random.randint(min,max))
    number=int(input("answer:"))
    while(number!=randomNumber):
        if(number<randomNumber):
            print("correct answer is larger")
        else:
            print("correct answer is smaller")
        number=int(input("answer:"))
    return print("Congratulations!!")

guesstheNumberGame()