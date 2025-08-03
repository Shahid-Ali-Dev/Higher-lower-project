import art
import random
from game_data import data
def game():
    def pik():

        return random.randint(0, len(data)-1)
    score = 0
    data1 = data[pik()]

    def avoid_duplicate(exclude):
        choice = pik()
        while data[choice] == exclude:
            choice = pik()
        return choice

    data2 = data[avoid_duplicate(data1)]
    print(art.logo)

    def datas(a, b, guess1):
        return (a['follower_count'] > b['follower_count'] and guess1 == 'a') or \
            (b['follower_count'] > a['follower_count'] and guess1 == 'b')

    def acc(account):
        return f"{account['name']}, a {account['description']} from {account['country']}."
    while True:

        print(f"Compare A: {acc(data1)}")
        print(art.vs)
        print(f"Against B: {acc(data2)}")
        guess = input("Who got more followers, 'A' or 'B'? ").lower()
        correct = datas(data1, data2, guess)

        if correct:
            score += 1
            print("\n" * 5)
            print(art.logo)
            if guess == "a":
                print(
                    f"You are correct! {data1['name']}'s followers are indeed greater than {data2['name']}'s followers.\nYour current score is {score}")
            elif guess == "b":
                print(
                    f"You are correct! {data2['name']}'s followers are indeed greater than {data1['name']}'s followers.\nYour current score is {score}")
            data1 = data2
            data2 = data[avoid_duplicate(data1)]

        else:
            print("\n"*5)
            print(art.logo)
            print(f"Sorry you lost and your final score is {score}")
            ask = input("Would you like to play the game again? Type 'y' for yes or 'n' for no.\n").lower()
            if ask == "y":
                score = 0
                data1 = data[pik()]
                data2 = data[avoid_duplicate(data1)]
                print("\n" * 5)
                print(art.logo)
                continue
            print("Thank you for playing the game.")
            break

game()
