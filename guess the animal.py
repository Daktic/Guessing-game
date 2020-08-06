#guess the cat 
import sys
from time import sleep
print("Welcome to the Guessing Game!")
while True:
    while True:
        
        print("Would you like to play again?")
        play_game = input('Type "Yes" or "No" : ')
        if play_game.lower() == "yes":
            break
        elif play_game.lower() == "no":
            sys.exit()
        else:
            continue
    while True:
        print('Is it the primary Color Black?')
        color = input("Yes or No: ")
        print('Is it smol?')
        size = input("Yes or No: ")
        print('Is it a cat?')
        species = input("Yes or No: ")
        break
    print()
    print('thinking...')
    sleep(1)

    if color.lower() == "yes":
        q1 = "black"
    else:
        q1 = "not_black"
    
    if size.lower() == "yes":
        q2 = "smol"
    else:
        q2 = "beeg"
    
    if species.lower() == "yes":
        q3 = "cat"
    else:
        q3 = "dog"
    
    
    if q1 == "black" and q2 == "beeg" and q3 == "cat":
        print("Is is Vanta?")
    elif q1 == "not_black" and q2 == "beeg" and q3 == "cat":
        print("is it Mittens?")
    elif q1 == "not_black" and q2 == "smol" and q3 == "cat":
        print("is it Princess?")
    elif q1 == "not_black" and q2 == "smol" and q3 == "dog":
        print("is it Krystal?")
    elif q1 == "black" and q2 == "beeg" and q3 == "dog":
        print("is it Karma?")
    else:
        print("I'm Stumped!")
        sleep(1.5)
        print("play again?")
    
    while True:
        restart = input(":) ")
        if restart.lower() == "yes":
            print("I Win!")
            sleep(1)
            break
        else:
            print("oh well...Maybe next time!")
            sleep(3)
            sys.exit()

            
            






