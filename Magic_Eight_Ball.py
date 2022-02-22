# Magic eight Ball
import random
# Call User Name
name = input("Whats your name?")  
# Get User Question
question = input("Tell me your Yes/No question.")
# possible answers
answers = ["Yes - definitely.",
             "It is decidedly so.", 
             "Without a doubt.", 
             "Reply hazy, try agai", 
             "Ask again later.", 
             "Better not tell you now.", 
             "My sources say no.", 
             "Outlook not so good.", 
             "Very doubtful."]
# build random number with .random.randint between 0 incl 9
random_number = random.randint(0,9)
# check if we have Username and question 
if name and question:
    print(f'{name} asks: {answers[random_number]}')
else:
    print("No question no answer!")

