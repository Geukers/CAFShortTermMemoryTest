# Author: Philippe Geukers

# To play this game, go to CAFShortTermMemoryTest/dist/Main/Main.exe
# The file "Main.exe" was created using pyinstaller

# If you want to modify this script,
# install PyCharm Community on your computer,
# and watch a video on youtube of how to setup it

import random
import time
import os

number_of_rounds = 5  # Number of rounds the user will play
time_displayed = 5  # Number of seconds each series will be displayed
length_of_series = 10  # Number of digits that will be in each series


def display_home_screen():
    print("Welcome to the CAF short term memory test\n"
          "Instructions:\n"
          "1 - You will be shown a series of " + str(length_of_series) + " numbers for " + str(time_displayed) +" seconds\n"
          "2 - You will then be asked a question about the numbers\n"
          "3 - There will be " + str(number_of_rounds) + " rounds\n")
    input("Press Enter to continue")

    # Begins running the code written in start_test()
    start_test()


def start_test():
    score = 0

    # Replays the game for the number of rounds that were given above
    for i in range(number_of_rounds):
        # If the user got the correct answer,
        # ask_a_question will return true and therefore will increment the score by 1
        if ask_a_question():
            score += 1
    # Once all the rounds have been played the score is displayed
    print("Your score is " + str(score) + "/" + str(number_of_rounds))

    # The user can decide if he wants to play again or leave
    if input("Do you want to play again? (y/n)") == "y":
        start_test()
    else:
        print("Goodbye!")
        exit()


def ask_a_question():

    # Removes whatever is on the screen at the moment
    clear_screen()
    # Determines what digit is going to be asked
    question = random.randint(0, 9)
    # Number of occurrences of the digit in the series
    answer = 0
    # The series itself
    number_list = ""

    # Adds digits to the series at random and
    # if it's the same digit as the question, the answer gets incremented by one
    for i in range(length_of_series):
        random_number = random.randint(0, 9)
        if random_number == question:
            answer += 1
        number_list += str(random_number) + " "

    # Displays the series and waits for the amount of time established
    print(number_list)
    time.sleep(time_displayed)

    # Removes the series from the screen in order to ask the question,
    # the game would be way too easy otherwise
    clear_screen()

    user_answer = input("How many " + str(question) + "s were there?")
    print(number_list)
    if str(answer) == user_answer:
        print("Correct!")
        input("Press Enter to continue")
        return True
    else:
        print("Wrong - Correct Answer : " + str(answer))
        input("Press Enter to continue")
        return False


def clear_screen():
    os.system("cls")  # Clears the screen in the windows console, but did not work when I was testing it in PyCharm

    # If you want to test the program in pycharm, uncomment the following line by removing the "#"
    # print('\n'*1000)


# The game starts here
if __name__ == "__main__":
    display_home_screen()


