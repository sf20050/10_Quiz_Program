import time

# functions go here

def countdown(time_min):
    while time_min:
        mint, sec = divmod(time_min, 60)
        time_format = '{:02d}:{:02d}'.format(mint, sec)
        print(time_format, end='\r')
        time.sleep(1)
        time_min -= 1

    print("stop")

def yes_no(question):
    valid = False
    while not valid:
        # ask user if they played before
        response = input(question).lower()
        # if yes output 'program continues'
        if response == 'yes' or response == 'y':
            response = "yes"
            return response
        # if no output 'display instructions'
        elif response == 'no' or response == 'n':
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    # shows the user the instructions on how to answer the quiz
    print("**** How to play ****")
    print()
    print(" choose the times-table which you are to be tested upon ")
    print(" choose the amount of questions you are going to do for the said times-table ")
    print(" You have 3 guesses and start with a score of zero")
    print(" All questions gotten correct gives you a +1 score")
    print(" All Questions gotten wrong takes away 1 guess and at 0 guesses the game stops ans also display score ")
    print()
    return ""


def statement_generator(statement, decoration):
    # this decorates text shown when program is run
    sides = decoration * 3

    statement = "{}  {}  {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# main route goes here
guesses = 3
score = 0
statement_generator("Welcome to your Quiz!", "@")
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

validated = False
while not validated:
    try:
        # asks user what times-table they want to answer
        times_table = int(input("What times table would you like to be tested on: "))
        # asks user up to what amount of questions they want to answer
        max_value = int(input("What is the maximum value you would like to go up to: "))
        validated = True
    except ValueError:
        print("Enter a whole number")
print("Here is the {} times table that you have chosen to be tested on".format(times_table))

# this changes the value of x meaning that the questions will increase with this
for x in range(1, max_value + 1):
    while guesses > 0:
        answer = int(x * times_table)
        question = ("{} times {} is ...".format(x, times_table,))
        quiz = int(input(question))
        # This checks if the answer is wrong and if wrong takes 1 guess
        if quiz != answer:
            print("incorrect!")
            print("the answer is {}".format(answer))
            guesses -= 1
            print("Guesses:{}".format(guesses))
            print("{}/{}".format(x, max_value))
        # This checks if the answer is correct and if correct gives +1 score
        else:
            print("correct")
            print("Guesses:{}".format(guesses))
            print("{}/{}".format(x, max_value))
            score += 1
        break
print()
print("You total score for the quiz is {}".format(score))

# This just is a simple timer after the quiz
print(" here is a 10 second timer after the quiz for you to see")
countdown(10)
