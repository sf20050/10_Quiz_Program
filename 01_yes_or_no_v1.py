# Asks user if they played game before
yes_no = input("Have you played this game before? ").lower()
# if user says yes program continues
if yes_no == 'yes':
    print("program continues")

elif yes_no == 'y':
    print("program continues")
# if user says no display instructions
elif yes_no == 'no':
    print("display instructions")

elif yes_no == 'n':
    print("display instructions")
# if user does not enter yes / no display error message
else:
    print("Enter yes / no")
print()
# Display users decision
print("You have chosen {}".format(yes_no))


