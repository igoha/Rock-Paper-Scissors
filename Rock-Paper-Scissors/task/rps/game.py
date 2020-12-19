import random


def foo_import_rating():
    # import name and score from file and add to dict gamers
    gamers = {}
    file = open("rating.txt")
    for line in file:
        gamers[line.split()[0]] = line.split()[1]
    file.close()
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    # return rating from dict gamers, if name not in dict, rating = 0
    return int(gamers.get(name, 0))


def foo_input_options():
    # options from user input
    user_input = input()
    if len(user_input) != 0:
        # import user input to options list
        options_list = user_input.split(sep=",")
    else:
        # if no input use standard options list
        options_list = ["rock", "paper", "scissors"]
    print("Okay, let's start")
    return options_list


# import rating from file
rating = foo_import_rating()
# options from user input
options = foo_input_options()

while True:
    random_word = random.choice(options)
    user_word = input().lower()
    if user_word == "!exit":
        print("Bye!")
        break
    elif user_word == "!rating":
        print(rating)
    elif user_word not in options:
        print("Invalid input")
    else:
        user_word_index = options.index(user_word)
        random_word_index = options.index(random_word)
        if user_word_index < (len(options) - 1) / 2:
            user_slice = options[user_word_index + 1:user_word_index + 8]
            print((len(options) - 1) / 2)
        else:
            user_slice = options[user_word_index - 7:user_word_index]
            print((len(options) - 1) / 2)
        if user_word == random_word:
            rating += 50
            print(f"There is a draw {user_word}")
        elif user_word == random_word:
            rating += 100
            print(f"Well done. The computer chose {random_word} and failed")
        else:
            print(f"Sorry, but the computer chose {random_word}")
