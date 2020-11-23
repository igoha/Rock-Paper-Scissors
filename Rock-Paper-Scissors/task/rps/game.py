import random

while True:
    lose_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    random.seed()
    random_word = random.choice(list(lose_dict.keys()))
    user_choise = input().lower()
    if user_choise == "!exit":
        break
    elif user_choise not in list(lose_dict.keys()):
        print("Invalid input")
    else:
        lose_word = lose_dict.get(random_word)
        if user_choise == random_word:
            print(f"There is a draw {user_choise}")
        elif user_choise == lose_word:
            print(f"Well done. The computer chose {random_word} and failed")
        else:
            print(f"Sorry, but the computer chose {random_word}")
