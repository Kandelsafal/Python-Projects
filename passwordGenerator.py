import random

print ("WELCOME TO THE PASSWORD GENERATOR.\n LETS GENERATE THE PASSWORD")

user_input = (input("ENTER THE LENGTH OF THE PASSWORD : "))

while not user_input.isdigit():
    print("You Should enter an integer.")
    user_input = input("Enter the length of the password again : ")

user_input = int(user_input)

letters = 'abcdefghijklmnopqrstuvwxyz'
number = '1234567890'
symbol = '!@#$%^&*'
password_condition1 = input ("Do u want atleast one number to be included (y/n)")
password_condition2 = input ("Do u want atleast one special to be included (y/n)")
all_char = letters+letters.upper() + (number if password_condition1 == 'y' else "") + (symbol if password_condition2 == 'y' else "")

password = ""
if password_condition1 == 'y' :
        password += random.choice(number)
        user_input -= 1
if password_condition2 == 'y' :
        password += random.choice(symbol)
        user_input -= 1

for pw_length in range(user_input):
    
    password += random.choice(all_char)
password_list = list(password)
random.shuffle(password_list)
final_pw = "".join(password_list)
print (f"PASSWORD GENERATED : {final_pw}")