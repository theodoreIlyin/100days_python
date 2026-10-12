#code 1
# fruits = ["Apple", "Peach",  "Pear"]
# for fruits in fruits:
#     print(fruits)
#     print(fruits + 'pie')

#code 2
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# max_score = 0
# for scores in student_scores:
#     if scores> max_score:
#        max_score = scores

# print(max_score)

#code 3 
# for number in range(1, 11, 3):
#  print(number)

#code 4
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

#code 5
# for number in range(1, 101):
#     if 0 == number % 15:
#         print("FizzBuzz")
#     elif 0 == number % 5:
#         print("Buzz")
#     elif 0 == number % 3:
#         print("Fizz")
#     else:
#         print(number)

#code 6
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Добро пожаловать в генератор паролей в Генератор паролей!") 

# rn_letters = int(input("Сколько букв ты хочешь в своём пароле?\n"))
# rn_symbols = int(input(f"Сколько символов ты хочешь?\n"))  
# rn_numbers = int(input(f"Сколько цифр ты хочешь?\n")) 
# #легкий вариант
# password = ""

# for char in range(1, rn_letters + 1):
#     random_char=random.choice(letters)  
#     password = password + random_char
#     password  += random_char
#     print(password)

#code 6 verision 2.0
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Добро пожаловать в генератор паролей в Генератор паролей!") 

rn_letters = int(input("Сколько букв ты хочешь в своём пароле?\n"))
rn_symbols = int(input(f"Сколько символов ты хочешь?\n"))  
rn_numbers = int(input(f"Сколько цифр ты хочешь?\n")) 
#легкий вариант
password = ""

for char in range(1, rn_letters + 1):
    password += random.choice(letters)


for char in range(1, rn_symbols + 1):
    password += random.choice(symbols)


for char in range(1, rn_numbers + 1):
    password += random.choice(numbers)

print(password)