import random

def magic_8_ball():
    responses = {
        "affirmative": [
            "Yes, definitely!",
            "It is certain.",
            "Without a doubt."
        ],
        "non-committal": [
            "Ask again later.",
            "Cannot predict now.",
            "Better not tell you now."
        ],
        "negative": [
            "Don't count on it.",
            "My sources say no.",
            "Very doubtful."
        ]
    }
    
    all_responses = responses["affirmative"] + responses["non-committal"] + responses["negative"]
    
    input("Ask the Magic 8 Ball a yes/no question: ")
    print("The Magic 8 Ball says:", random.choice(all_responses))

# Run the Magic 8 Ball
magic_8_ball()
