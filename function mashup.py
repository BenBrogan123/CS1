import random # imports random from library 
def chorus(): # defines a function named chorus
    print("Twinkle, twinkle, little star,")# prompts code to print the first line of the song 
    print("How I wonder what you are!")  # prompts code to print second line of the song 
def sing(): # defines a function named sing 
    chorus()# used the chorus function to print the two lines of the song 
    print("up above the world so high,") # prompts code to prints third line of the song 
    print("like a diamond in the sky.") # prompts code to print foruth line of song 
#function 2 
def add(number1,number2): # defines the function named add and then assings number1 and number2 
    print(number1, number2) # prompts code to print number1 and number2
#function 3
def print_elements(my_list):# defines the function named print_elments 
    for element in my_list: # creates a loop to check each item in list 
        print(element)# pirnts each element in the list 
#function 4
def element(my_list, check): # defines function named element and checks the function 
    if check in my_list: # checks if the paramters exist 
        return True # returns true if the paramters are found in the list 
    else: # tells code what to do if the pafameters are not met 
        return False # returns false if the code does not work 
    
def are_numbers_positive(numbers):# defiens the fucntion are_numbers_positive 
    for number in numbers: # creates a loop to check each 
        if number.isnumeric():# checks if number is numeric 
            return True # retuns true if the parameters exist 
        else: # tells code what to do if the parameters are not met 
            return False # returns false if the code does not work 
def is_int(number):# defines the function that checks if intger is a number 
    if "-" in number: # this is an empty string is asking it is a negative 
        number = number[1:] # asking if the number is numeric 
    if number.isnumeric():# checks isf the number is numeric 
        return True # returns true if the parameters exist 
    else: # tells code what to do if parameters dont work 
        return False # returns false if the code doesnt work 

def get_random():# defines get random 
    num1 = int(input("enter number 1")) # prompts user to input first number 
    num2  = int(input("enter nuber 2"))# prompts user to input second number 
    
    while True: # if user inputs two numbers runs code bellow 
        if is_int(number) and is_int(number2): # if the intger is a number and intiger two is a number prompts code to run line below 
            print(random.randint(number, number2)) # has code print the random number1 and number2
            break # ends code 
        else: # if the user repsonse if not a number it prints line below 
            print("Not an integer!") # promts code to print the message 

def replace_charcter(word, old_letter, new_letter):# defines function named replace charcter that takes a word string a new letter and a new letter as an input 
    new_word="" # empty string is set equal to new_word 
    
    for letter in word: # starts a loop that check each letter in the word 
        if letter == old_letter: # checks if the old letter is equal to the new letter 
            new_word += new_letter # if the current letter is equal to the new letter 
        else: # tells code to run below if new letter is not equal to old letter 
            new_word += letter # if new letter is equal to lettr 
    return new_word # retuns new word 

def main(): # defines main function 
    sing() #calls the sing fucntion to print the letters of the song 
    my_list = ["a", "b", "c"] # creates my list elements 
    print_elements(my_list) # prints the elements in the list 
    check = input("Whats your number") # asks user to enter a number 
    print (element(my_list,check)) # calls the element function 
    num1 = input("Pick your first number") # asks user to pick their first number 
    num2 = input("Pick your second number")# ask user to print their second number 
    print(replace_charcter("hello", "l", "a")) #prints this list 
main () # executes program 
