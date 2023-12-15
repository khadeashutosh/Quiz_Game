import random
user_choice=int(input("Enter any choice number:- 0 for Rock ,1 for Paper , 2 for Scissors:-"))
if user_choice >=3 and user_choice <0:
    print("You have entered invalid number, You lose")
else:    
    computer_choice=random.randint(0,2)
    print("Computer choice number:-")
    print(computer_choice)                       #Rock wins againts Scissors 
    if computer_choice ==user_choice:            #Scissors wins againts Paper
        print("This is draw")                    #Paper wins againts Rock
    elif computer_choice==0 and user_choice==2:
        print("you lose")   
    elif user_choice==0 and computer_choice==2:
        print("you win ")     
    elif computer_choice > user_choice:
        print("you lose")    
    elif user_choice> computer_choice:
        print("you win")    