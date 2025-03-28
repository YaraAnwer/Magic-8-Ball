import random

respons=["yes,definitey!"
        "No,not now.","Ask again later.",
        "It is certain.",
        "Very doubtful.",
        "Outlook is good.",
        "Better not tell you now.",
        "Concenttrate and ask again."]

def get_random_response():

       return random.choice(respons)

