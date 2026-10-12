# # code 1
# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]

#code 2
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input('what do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: '))

computer_choice = random.randint(0,2)
print(f"Сomputer_choice{computer_choice}")

if user_choice == 0  and computer_choice == 2:
    print("User wins")
elif computer_choice == user_choice == 2:
    print("it is draw")
elif computer_choice > user_choice:
    print('computer wins')
else:
    print("you typed")