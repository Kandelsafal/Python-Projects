import random

choices = ['rock', 'scissor', 'paper']



total_rounds = int(input("Enter the total round u wish to play: "))
player_score = 0;
computer_score = 0;
for round_num in range(total_rounds):
    print(f"Round : {round_num + 1}")
    user_Input = input("Rock, Paper, Scissor . Choose any One : ").lower();
    if user_Input not in choices :
        print ("Invalid Choice")
        user_Input = input("Rock, Paper, Scissor . Choose any One : ").lower();
    
    computer_choice = random.choice(choices)
        
    if user_Input ==  computer_choice :
        print (f" Computer's Choice : {computer_choice} \n IT's a TIE.")

    elif  user_Input == 'rock' and computer_choice == 'scissor':
        player_score += 1;
        print (f" Computer's Choice : {computer_choice} \n You WIN.")
    elif user_Input == 'scissor' and computer_choice == 'paper':
        player_score += 1;
        print (f"Computer's Choice : {computer_choice} \n You WIN.")
    elif user_Input == 'paper' and computer_choice == 'rock':
        player_score += 1;
        print (f"Computer's Choice : {computer_choice} \n You WIN.")
    else :
        computer_score +=1; 
        print (f"Computer's Choice : {computer_choice} \n COMPUTER WIN.")

if player_score > computer_score :
    print (f"""FINAL SCORE : \n 
       
       Total Rounds {total_rounds}\n 
       Player_Score : {player_score}\n
       Computer_Score : {computer_score}\n YOU WIN !!!
       """)
elif player_score == computer_score : 
    print (f"""FINAL SCORE : \n 
       
       Total Rounds {total_rounds}\n 
       Player_Score : {player_score}\n
       Computer_Score : {computer_score}\n 
       IT's a TIE !!!
       """)
else :
    print (f"""FINAL SCORE : \n 
       
       Total Rounds {total_rounds}\n 
       Player_Score : {player_score}\n
       Computer_Score : {computer_score}\n COMPUTER WIN !!!
       """)
