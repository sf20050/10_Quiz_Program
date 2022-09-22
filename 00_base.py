# functions go here

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
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def statement_generator(statement, decoration):

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
        times_table = int(input("What times table would you like to be tested on: "))
        max_value = int(input("What is the maximum value you would like to go up to: "))
        validated = True
    except ValueError:
        print("Enter a whole number")
print("Here is the {} times table that you have chosen to be tested on".format(times_table))

for x in range(1, max_value + 1):
    while guesses > 0:
        answer = int(x * times_table)
        question = ("{} times {} is ...".format(x, times_table,))
        quiz = int(input(question))
        if quiz != answer:
            print("incorrect!")
            print("the answer is {}".format(answer))
            guesses -= 1
            print("Guesses:{}".format(guesses))
            print("{}/{}".format(x, max_value))
        else:
            print("correct")
            print("Guesses:{}".format(guesses))
            print("{}/{}".format(x, max_value))
            score += 1
        break
print()
print("You total score for the quiz is {}".format(score))
