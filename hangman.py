from ctypes.wintypes import WORD
from itertools import count
from operator import length_hint
import random
import time

print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("Hello " + name + "!Best of Luck")
time.sleep(2)
print("The game is about to start!\n Let's play Hangamn!")
time.sleep(3)



def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","file","promise","kids","lungs","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count(0)
    display = '_' +length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes ,n = no \n")
    while play_game not in ["y","n","Y","N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if  play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We except you back again!")
        exit()

    
    def hangman():

     global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    limit = 5
    guess = input("This is the Hangman word:" + display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <="9": 
        print("Invalid Input,Try a letter\n")
        hangman()
    elif guess in word 
    already_guessed
    index = word.find(guess)
    word = word.find[:index] + "-" + word[index +1:] 
    display = display[:index]+guess+display[index +1:]
    print(display +"\n")

    elif guess in . already_guessed
    print("Try another letter \n")
    else:
    count +=1
    if count == 1:
        time.sleep(1)
    
    print         (" _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
                 