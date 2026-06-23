import random

print ("=" * 50)
print("          --->  WELCOME TO QUIZ  <---           ")
print("=" * 50)

quiz_ques = {
    "ques1": {
        "question": "When was Python first released?",
        "options": ["A. 1990", "B. 1991", "C. 1995", "D. 2000"],
        "answer": "B"
    },

    "ques2": {
        "question": "Who created Python?",
        "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },

    "ques3": {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. fun", "D. def"],
        "answer": "D"
    },

    "ques4": {
        "question": "What is the output type of input()?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "C"
    },

    "ques5": {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },

    "ques6": {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },

    "ques7": {
        "question": "What is the result of 5 // 2?",
        "options": ["A. 2.5", "B. 3", "C. 2", "D. 1"],
        "answer": "C"
    },

    "ques8": {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["A. while", "B. for", "C. do-while", "D. repeat"],
        "answer": "B"
    },

    "ques9": {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },

    "ques10": {
        "question": "What keyword is used to create a class in Python?",
        "options": ["A. object", "B. class", "C. define", "D. new"],
        "answer": "B"
    }
}


while True:
    play_input = input("Do u want to play the Quiz (y/n) : ").lower();
    if play_input == 'y' :
        player_score = 0;
        questions = list(quiz_ques.items())
        random.shuffle(questions)

        for key, value in questions:
            
            print (value["question"]+ "\n")

            for option in value["options"]:
                print(option)
            
            while True:
                user_input = input("Your answer : ").upper()
                if not user_input in "ABCD":
                    print("Enter the available options only")
                else:
                    break
            if user_input == value["answer"]:
                player_score += 1
                print("The correct answer \n")
                print("-" * 40 +"\n")
            else:
                print("The answer is wrong \n")
        
        print ("The FInal Score : ", player_score)
        break


    elif play_input == 'n':
        print(".....Quitting Game");
        break
    else:
        print("Enter (y (yes) or n (no)) to start or quit the game.")
        play_input = input("Do u want to play the Quiz (y/n) : ").lower();
        
