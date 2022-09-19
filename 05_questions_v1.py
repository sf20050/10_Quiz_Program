guessess = 3


while guessess > 0:
    answer = "2"
    quiz = input("what is 1 + 1? ")

    if quiz != answer:
        print("incorrect!")
        guessess -= 1
        print("Number of guesses left:{}".format(guessess))
    elif quiz == answer:
        print("correct")
        print("Number of guesses left:{}".format(guessess))
        break
