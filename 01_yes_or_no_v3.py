def yes_no(question):
    valid = False
    while not valid:
        # Asks user if they played game before
        response = input(question).lower()

        # if user says yes program continues
        if response == 'yes' or response == 'y':
           response = "yes"
           return response

        # if user says no display instructions
        elif response == 'no' or response == 'n':
            response = "no"
            return response

        # if user does not enter yes / no display error message
        else:
            print("Please enter yes / no")
            print()
        # Display users decision


# main route goes here
show_instructions = yes_no("Have you played this game before? ")
print("You have chosen {}".format(show_instructions))
having_fun = yes_no("Are you having fun? ")
print("You said {} to having fun".format(having_fun))
