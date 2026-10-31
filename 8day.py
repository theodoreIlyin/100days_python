# def  greet():
#     print("Hello")
#     print("how do you do?")
#     print("|Isn't the weather nice?")


# greet()
# greet( )

# # Functions that allows for inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Billie")


# def life_in_weeks(my_age):
#     weeks_left = (90 - my_age)*52
#     print(f"You have {weeks_left} weeks left.")
    
# life_in_weeks(20)


 #code 2
# def greet_with(name, location):
#     print(f"hello {name}")
#     print ("what is  it like  in {location}") 

# greet_with(name ="Jack Bawer", location= 'Nowthere')

# green_with(name="Angela", location="London")

# code 3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.

    # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# fruits = ["apple", "Pear", "Orange"]
# fruits.index("Pear")






def encrypt(original_text, shift_amout):
   cilher_text = ""
   
for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amout
        cipher_text  = alphabet[shifted_position]