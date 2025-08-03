logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


# import random
# from game_data import data
#
#
# def pick_random():
#     return random.choice(data)
#
#
# def get_unique_choice(exclude):
#     choice = pick_random()
#     while choice == exclude:
#         choice = pick_random()
#     return choice
#
#
# def format_account(account):
#     return f"{account['name']}, a {account['description']} from {account['country']}"
#
#
# def compare_followers(a, b, guess):
#     return (a['follower_count'] > b['follower_count'] and guess == 'a') or \
#         (b['follower_count'] > a['follower_count'] and guess == 'b')
#
#
# def game():
#     score = 0
#     account_a = pick_random()
#     account_b = get_unique_choice(account_a)
#
#     print(logo)
#
#     while True:
#         print(f"Compare A: {format_account(account_a)}")
#         print(vs)
#         print(f"Against B: {format_account(account_b)}")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         correct = compare_followers(account_a, account_b, guess)
#
#         if correct:
#             score += 1
#             print("\n" * 5)
#             print(logo)
#             print(f"You're right! Current score: {score}.\n")
#             account_a = account_b
#             account_b = get_unique_choice(account_a)
#         else:
#             print("\n" * 5)
#             print(logo)
#             print(f"Sorry, that's wrong. Final score: {score}")
#             again = input("Play again? (y/n): ").lower()
#             if again == 'y':
#                 print("\n" * 5)
#                 game()  # restart fresh
#             else:
#                 break
#
# game()
