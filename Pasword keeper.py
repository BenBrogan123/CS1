def print_entry(websites, usernames, passwords, i): # defines the function print entry which uses four parameters, websites, usernames, passwords, and i 
    '''
    description

    Args:
        websites (list): Websites entered by the user
        usernames (list): Usernames entered by the user '
        passwrods (list): asks users for passwrods
        i (int): decides which index to print
    Prints:
        prints one entry given by the user
    '''
    
    print(f'''websites: {websites[i]} 
    usernames: {usernames[i]}
    passwords: {passwords[i]}''')
    
def add_entry(websites, usernames, passwords): # Defines the function named add entry which uses the three parameters, websites, usernames, and passwords 
    while True: # starts an infinte loop 
        web = input("what website do you want to add?('stop' to end)") # prompts user to input a website name or type stop to end 
        
        if web == ("stop"): # Checks if the user input was stop and if it was brakes the code 
            break # breakes the code if the user input was stop 
        websites.append(web)# Appends the website
        usernames.append(input("what is your username?"))# changes the username with user input 
        passwords.append(input("what is your password?"))# changes the password with user input 
def main(): # defines main function 
    websites = [] # creates an empty list equal to websites 
    usernames = [] # creates an empty list equal to usernames 
    passwords = [] # creates an empty list equal to passwords 

    add_entry(websites, usernames, passwords) # calls add entry fucntion to add the user input to list 
    
    while True: # starts another ifninte loop 
        mode = input("Which would you like: 1. Add another entry, 2. Print all, 3. Print specific 4. Change entry 5. End") # this line prompts the user to choose one of the five options 

        if mode == "5": # if the user selects mode 5 it ends program 
            break # ends program if user selcted mode 5 
        elif mode == "1": # if the user selects mode 1 the add entry function is used 
            add_entry(websites, usernames, passwords) # ads the new entries the user provided 
        elif mode == "2": # if the user selects mode 2 it prints the code below 
            for i in range(len(websites)): # promtp code to print the three items from list in order 
                print_entry(websites, usernames, passwords, i) # prints the user items 
        elif mode == "3": # if the user selctes mode 3 prompts user for a website name 
            name = input("Enter website to print: ") # asks user what website it wants to print 

            if name in websites: # prompts code to do line below 
                print_entry(websites, usernames, passwords, websites.index(name))# prints the items in the list 
        elif mode == "4": # if the user selctes mode 4 
            ask_website = input("what do you want to change?") # asks user what they want to change 

            if ask_website in websites: # if the user asked to change pre exsiting website prompts user to do the below lines 
                i = websites.index(ask_website) # asks for below 
                usernames[i] = input("Enter new username: ") # asks user for user to enter new username 
                passwords[i] = input("Enter new password: ") # asks user for new password

main() # main fucntion 
