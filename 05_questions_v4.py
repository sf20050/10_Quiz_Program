def quiz(question):
    guesses = 3
    score = 0
    for x in range(1, max_value + 1):
        while guesses > 0:
            answer = int(x * times_table)
            question = ("{} times {} is ...".format(x, times_table,))
            response = int(input(question))
            if response != answer:
                print("incorrect!")
                print("the answer is {}".format(answer))
                guesses -= 1
                print("Number of guesses left:{}".format(guesses))
            else:
                print("correct")
                print("Number of guesses left:{}".format(guesses))
                score += 1
                break



times_table = int(input("What times table would you like to be tested on: "))
max_value = int(input("What is the maximum value you would like to go up to: "))

asked = quiz("{} times {} is ...".format(x, times_table,))
