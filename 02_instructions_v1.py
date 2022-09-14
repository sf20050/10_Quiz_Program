# functions go here
def yes_no(question):
    valid =False
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


# main route
played_before = yes_no("Have you play this game before? ")

if played_before == "no":
    instructions()

print("program continues")

