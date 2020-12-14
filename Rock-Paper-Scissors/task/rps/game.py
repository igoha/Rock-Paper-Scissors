import random


def foo_import_file():
    # import name and score from file and add to dict gamers
    file = open("rating.txt")
    for line in file:
        gamers[line.split()[0]] = line.split()[1]
    file.close()
    return


gamers = {}

foo_import_file()
name = input("Enter your name: ")
print(f"Hello, {name}")
# import rating from dict gamers, if no in dict rating = 0
rating = int(gamers.get(name, 0))

while True:
    lose_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    random.seed()
    random_word = random.choice(list(lose_dict.keys()))
    user_choise = input().lower()
    if user_choise == "!exit":
        print("Bye!")
        break
    elif user_choise == "!rating":
        print(rating)
    elif user_choise not in list(lose_dict.keys()):
        print("Invalid input")
    else:
        lose_word = lose_dict.get(random_word)
        if user_choise == random_word:
            rating += 50
            print(f"There is a draw {user_choise}")
        elif user_choise == lose_word:
            rating += 100
            print(f"Well done. The computer chose {random_word} and failed")
        else:
            print(f"Sorry, but the computer chose {random_word}")
