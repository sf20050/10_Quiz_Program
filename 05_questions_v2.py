# this shows how much guesses user starts with
guesses = 3

#
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
            print("Number of guesses left:{}".format(guesses))
        else:
            print("correct")
            print("Number of guesses left:{}".format(guesses))
            break
