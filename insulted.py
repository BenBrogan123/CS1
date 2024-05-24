import random # imports random library for all random functions
print("Hey what are you doing") # prompts code to print the question "Hey what are you doing"
insults1 = ["Thou pribbling fool-born pigeon-egg","Thou weedy ill-breeding codpiece,""Thou reek reeling-ripe minnow",] # list1 of insults 
insults2 = ["Thou wayward plume-plucked haggard", "Thou suacy sheep- bitting bum-baily","Thou bootles motley-minded minnow"]# list2 of insults 
insult_question = int(input("How many times would you like to be insulted?"))# Ask the user how many times they want to be insulted and stores the reponse as a intger 
for i in range(insult_question): # identifies loop connects the Varible to the list then identifies how many times it will run
    print(f'''{random.choice(insults1)} {random.choice(insults2)}''') # prompts code to print amount of insults the user chose / comes from the two lists 
