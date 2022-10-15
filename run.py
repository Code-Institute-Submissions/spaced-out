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
        ["A. 12 years?", "B. 6 years?", "C. 8 years?"]
]
"""
show user next question from dictionary of 
questions.
Question index incremented by one.
"""
def get_next_question():

    guesses = []
    correct_guesses = 0
    question_index = 1

    for key in questions:
        print("-------")
        print(key)
        for i in options[question_index-1]: 
            print(i)
        guess = input("Enter (A, B, or C): ")
        guess = guess.lower()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_index += 1    

"""

Check users answer from the 
check answer function, call it in the
get next question function. with parameters (answer ,guess),
getting the questions KEY, and guess
if statement to comare if answer and are guees and equal
if not "not correct!"
"""

def user_input():
    pass

def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def get_users_score():
    pass

"""

Calls all game functions in main function
"""
if __name__ == '__main__':
    get_next_question()