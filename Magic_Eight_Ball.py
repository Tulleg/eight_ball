# Magic eight Ball
import random
name = input("Whats your name?")
question = input("Tell me your Yes/No question.")
answers = ["Yes - definitely.",
             "It is decidedly so.", 
             "Without a doubt.", 
             "Reply hazy, try agai", 
             "Ask again later.", 
             "Better not tell you now.", 
             "My sources say no.", 
             "Outlook not so good.", 
             "Very doubtful."]
random_number = random.randint(0,9)
print(random_number)
if name and question:
    print(f'{name} asks: {answers[random_number]}')

