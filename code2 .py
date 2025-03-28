import random

respons=["yes,definitey!"
        "No,not now.","Ask again later.",
        "It is certain.",
        "Very doubtful.",
        "Outlook is good.",
        "Better not tell you now.",
        "Concenttrate and ask again."]
def get_user_guess():
    while True:
        try:
            guess=int(input("Enter your guess(1-100):"))
            if 1<=guess<=100:
                return guess
            else:
        
                print("pleasa enter a number between 1 and 100.")
        except ValueError:
            print("invalid input")        
def get_random_response():

       return random.choice(respons)

def display_respons(response) :
    print("\n the magic 8 ball says :",response, "\n")      

