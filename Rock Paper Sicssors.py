import random # brings in random functions from the library 
import sys # brings in the sys library for use of the exit() function 

comp_wins = 0 # sets the score at the begining of the game to zero
player_wins = 0 # sets the score at the begining of the game to zero 

rps = ['rock', 'paper', 'scissors'] # creates a list rps with the possible options for playing
rps_short = ["r", "p", "s"] # list of abbreviated options 

while True: # runs the following code in a loop until a break occurs 
    print("") # prints an empty line
    user_choice = str.lower(input("Choose Rock, paper or scissors: "))# prompts user to choose rock paper scissors and stores their response, in lowercase, in a varaible user_choice
    
    if user_choice not in rps and user_choice not in rps_short: # the user does not enter a valid option from the two lists above 
        print("invalid") # prints invalid 
    else: #otherwise
        comp_choice = random.choice(rps) # sets a variable equal to a random choice from the list 'rps' 

        if user_choice in rps_short: # if the user repsonse is contained within the list rps short 
            user_choice = rps[rps_short.index(user_choice)] # finds the coresponding item in rps and converts the user choice to that item
        if user_choice == comp_choice: # if the user choice is equal to the comp choice  
            print("You tied") # prompts code to print "you tied"
        elif user_choice == "rock": # otherwise, if user choice is rock 
            if comp_choice == "scissors": # and the computer choice is scissors  
                print("You win!") # prompts code to print "You win!"
                player_wins += 1 # score board player +1
            elif comp_choice == "paper": # otherwise the computer chooses paper 
                print("you lost") # prompts code to print "you lost"
                comp_wins += 1 # score board computer wins +1
        elif user_choice == "scissors": # otherwise the user choice is scissors 
             if comp_choice == "rock": # and the computer choice is rock
                print("you lost") # prompts code to print "you lost"
                comp_wins += 1 # score board computer wins +1
             elif comp_choice == "paper": # otherwise computer choice is paper 
                print("You win!") # prompts code to print "You win!"
                user_wins += 1 # score board user wins + 1 
        elif user_choice == "paper": # otherwise user choice is paper 
            if comp_choice == "scissors": # and the computer choice is sicssors 
                print("you lost") # prompts code to print "you lost"
                comp_wins += 1 # score board computer wins +1
            elif comp_choice == "rock": # otherwise the computer choice is rock 
                print("You win!") # prompts code to print "You win!"
                user_wins += 1 # score board user wins +1

        print("")# prints a blank line 
        print(f"You chose {user_choice}, the bot chose {comp_choice}") # prints an f string, which is a type of string that concacentates strings with different variable data types, combining it into one final string
        print(f"player wins: {player_wins}; computer wins: {comp_wins}") # uses an f string to combine the player/computer with their scores
        
        while True: # runs following code in loop until breake occurs 
            play = str.lower(input ("Do you want to play again? (y/n)"))# prompts code to ask the question "Do you want to play again?" with the reposne being y or n
            if play in ["y", "yes"]: # if the repsonse is y or yes 
                break # breakes while true loop 
            elif play in ["n","no"]: # otherwise play repons is n or no 
                print("Done") # prompts code to print "Done"
                sys.exit() # exits the code 
            else: # otherwise 
                print("Invalid") # prompts code to print "Invalid"



