questions = {
    "How much do NASA space suits cost?: ": "A.",
    "How many moons are in our solar system?: ": "B.",
    "Which is the brightest planet in the night sky?: ": "C.",
    "How long is one year on Jupiter?: ": "A."
}

options = [
        ["A. 12 million dollars?", "B. 20 million dollars?"],
        ["A. 100 moons?", "B. 181 mooons?", "C. 300 moons?"],
        ["A. Mars?", "B. Neptune?", "C. venus?"],
        ["A. 12 years?", "6 years?", "C. 8 years?"]
]
"""
show user next question from dictionary of 
questions.
Question index incremented by one.


"""

def getnextQuestion():

    user_guesses = []
    correct_guesses = 0
    question_index = 0

    for key in questions:
        print("-------")
        print(key)
        for i in options[question_index]: 
            print(i)
            
        question_index += 1






"""

Calls all game functions in main function
"""
if __name__ == '__main__':
    getnextQuestion()
    takeUserGuess()