import random

world_list = ["addvark", "baboon", "camel"]

chosen_world = random.choice(world_list)
print(chosen_world)

placeholder = ""
world_lenght = len(chosen_world)
for position in range(world_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    quess = input("Guess a letter:").lower()

    display = ""

    
    for letter in chosen_world:
        if letter == quess:
            display += letter
            correct_letters.append(quess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")
