
import random;

secret_number = random.randint(1, 100)
print(secret_number)

userInput = 0
while userInput != secret_number :
    userInput = (input("Guess the correct Number or Press (Q to Quit) : "));
    if userInput.lower() == "q":
        print("Quitting Game")
        break;
    userInput = int(userInput)
    difference = abs(userInput - secret_number)
    print(difference)
    if difference > 5:
        print ("The guess is high ")
    elif difference < 5:
        print ("The guess is low near to the correct number")
    elif userInput == "q":
        print ("Quit")
        break
if (userInput == secret_number):
    print ("The guess is correct")