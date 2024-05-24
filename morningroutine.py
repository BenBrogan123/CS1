while True: # infinte loop (while condition true is true)
    print("alarm") # displays the word alarm 

    snooze = input("Snooze? ")# prompts the user to answer the question of whether they want to snooze and stores that response in a variable, snooze 

    if snooze == "yes": # if the users input to the questions snooze is yes   
        print("back to sleep for 15 more minuets")# then display the message: back to sleep for 15 more minuets 
    elif snooze == "no": # otherwise if the user says no
      print("wake up and shower")# then display the message: wake up and shower 
      break # manual break to infinite loop

look_phone = input("Look at your phone? ")# prompts the user to answer the question wether or not they want to look at thier phone and stores that response in a variable, Look at your phone
if look_phone == "yes": # if the user input to the question look at your phone is yes 
     print ("look at phone for five minuets then go downstairs") # then display the message: Look at phone for five mineuts then go downstairs
elif look_phone == "no": # otherwise if the user says no 
    print ("go downstairs")# display the message: go downstairs 
breakfast = input("eat breakfast? ") # prompts the user to asnwer the question of wether they want to snooze and stores that repsonse in a variable, eat breakfast
if breakfast == "yes": # if the users input to the question is yes 
    choice = input("Do you want eggs or cereal?")# then display the choice Do you want eggs or cereal 
    if choice == "eggs": # if the user prompts eggs 
        print ("cook eggs and then go to schoool") # display the message: cook eggs and then go to school
    if choice == "cereal": # if the user prompts cereal 
        print ( "poor a bowl of cereal and then go to school") # then display the message: poor a bowl of cereal and then go to school 
elif breakfast == "no": # if the user prompts no 
    print("go to school without eating") # then display the message: go to school without eating




