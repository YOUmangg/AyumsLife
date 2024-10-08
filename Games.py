import numpy as np
import time
import random
from playsound import playsound
import winsound
import Human
from colorama import Fore, Back, Style

class Game: 

    def Number_guessing(Ayum):
        def calc(a, b):
            return np.log2(b - a) + 1 
            # +1 because a and b are also included in the list of possible selections.

        def ask():
            print(Fore.YELLOW + "Do you want to play another game? Enter Yes or No")
            decision = input()
            return decision

        def check_for_valid_input(a, b):  #considering only one edge case as of now, where a == b
            if(a == b):
                return False
            else:
                return True

        decision = "Yes"
        while(decision == "Yes"):
            # Description of the game:
            start_time = time.time()
            print(Fore.CYAN + "Give me 2 numbers (enter separated). I will select a number from between these 2 numbers, inclusive of the numbers. I will give you some amount of chances to guess the number I have selected. For each number you guess, I will tell you if the number you have guessed is greater than or less than the number I have selected.")

            time.sleep(0.5)

            print(Fore.GREEN + "Welcome to the game of guessing the number! Please enter the numbers range in which you want me to guess a number: ")

            while(True):
                a = int(input())
                b = int(input())
                if(check_for_valid_input(a, b) == True):
                    break
                else: 
                    print(Fore.RED + "Enter valid numbers, please. Input again")

            print(Fore.CYAN + f'Thank you for the giving me the range of the numbers. I have selected \n a number between {a} and {b}.')
            d = calc(a, b)
            print(Fore.YELLOW + f"According to my calculations, you can guess the number in {int(d)} times if you play optimally.")
            time.sleep(2)
            print(Fore.GREEN + "It's your turn now! Try guessing the number: ")

            num_to_guess = random.randint(a, b)

            chances = int(d)

            guesses_made = 0

            while(guesses_made < chances):
                guess = int(input())
                guesses_made += 1
                if(guess == num_to_guess):
                    end_time = time.time()
                    print(Fore.GREEN + f"Congratulations! You guessed the number in {guesses_made} tries")
                    print(Fore.CYAN + f"You took {round((end_time - start_time), 2)} seconds to complete the game.")
                    Ayum.increase_health(random.randint(40, 100))
                    Ayum.increase_hunger(random.randint(1, 2))
                    Ayum.health_limit += random.randint(20, 50)
                    Ayum.sleep_limit += random.randint(0, 1)
                    Ayum.sleep -= random.randint(1, 2*(max(int(Ayum.age / 2), 1)))
                    try:
                        playsound(r'Projects\Number-Guessing-Game\sounds\WinSound.wav')
                    except:
                        print(Fore.RED + "Unable to play audio at the moment. Sorry!")
                    decision = ask()
                    break  
                else:
                    if(guesses_made == chances):
                        end_time = time.time()
                        print(Fore.RED + f"Sorry, you lost the game. The number I had chosen was: {num_to_guess}")
                        print(Fore.CYAN + f"You took {round((end_time - start_time), 2)} seconds to complete the game.")
                        Ayum.health_limit += random.randint(20, 50)
                        Ayum.increase_hunger(random.randint(3, 4))
                        Ayum.sleep_limit += random.randint(0, 2)
                        Ayum.sleep -= random.randint(1, 2*(max(int(Ayum.age / 2), 1)))
                        Ayum.increase_health(random.randint(20, 40))
                        try:
                            playsound(r'Projects\Number-Guessing-Game\sounds\LossSound.wav')
                        except:
                            print(Fore.RED + "Unable to play audio at the moment. Sorry!")
                        print(Fore.YELLOW + "Better luck next time!")
                        decision = ask()
                        break
                    elif(guess > num_to_guess):
                        winsound.MessageBeep(winsound.MB_ICONQUESTION)
                        print(Fore.YELLOW + f"Your guess is greater than the number. You have {chances - guesses_made} chances remaining.")
                    else:
                        winsound.MessageBeep(winsound.MB_ICONASTERISK)
                        print(Fore.YELLOW + f"Your guess is less than the number. You have {chances - guesses_made} chances remaining.")

        print(Fore.GREEN + "Thank you for playing the game. See you next time!")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    def SevenUp(Ayum):

        def roll_die():
            print(Fore.CYAN + "Rolling the die..")
            time.sleep(0.8)
            print(Fore.CYAN + "Rolling the die.")
            time.sleep(0.8)
            print(Fore.GREEN + "ROLLED! ")
            a = random.randint(1, 6)
            b = random.randint(1, 6)

            return [a, b]
        
        def print_die(ab):
            print(Fore.YELLOW + "DICE 1: ", end="")
            for i in range(ab[0]):
                print(Fore.YELLOW + "*", end = "")
                time.sleep(0.4)
            
            print("")

            print(Fore.YELLOW + "DICE 2: ", end="")
            for i in range(ab[1]):
                print(Fore.YELLOW + "*", end = "")
                time.sleep(0.4)
            
            print("")

        print(Fore.GREEN + "Welcome to the game of 7 up 7 down! I am Kuppu, your opponent for today. I will roll 2 die, ")
        time.sleep(2)
        print(Fore.CYAN + "and you have to predict if the sum of the numbers present on the die is greater than, equal to or less than 7.")
        time.sleep(2)
        output = roll_die()

        print(Fore.YELLOW + "Enter your guess! -1 for less than 7, 0 for equal to 7, and 1 for greater than 7")

        x = int(input())

        sum = output[0] + output[1]

        print_die(output)

        win = False
        if(sum < 7):
            if(x == -1):
                win = True
                print(Fore.GREEN + f"You won! The die had a sum of {sum} which is less than 7!")

        if(sum == 7):
            if(x == 0):
                win = True
                print(Fore.GREEN + f"You won! The die had a sum of {sum} which is equal to your guess!")

        if(sum > 7):
            if(x == 1):
                win = True
                print(Fore.GREEN + f"You won! The die had a sum of {sum} which is greater than 7!")

        if(win == True):
            Ayum.increase_health(random.randint(40, 80))
            Ayum.increase_hunger(random.randint(1, 2))
            Ayum.health_limit += random.randint(20, 50)
            Ayum.sleep_limit += random.randint(0, 1)
            Ayum.sleep -= random.randint(1, 2*(max(int(Ayum.age / 2), 1)))
        if(win == False):
            print(Fore.RED + f"Sorry! The die had a sum of {sum}. Better luck next time!")
            Ayum.increase_health(random.randint(20, 40))
            Ayum.increase_hunger(random.randint(3, 4))
            Ayum.health_limit += random.randint(10, 50)
            Ayum.sleep_limit += random.randint(0, 2)
            Ayum.sleep -= random.randint(1, 2*(max(int(Ayum.age / 2), 1)))
