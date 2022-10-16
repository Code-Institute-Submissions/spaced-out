"""
Print welcome message to the user.
"""
print("Welcome to Sapced out!")
playing = input("Press any key to start! ")
if playing == playing:
    print("Lets play!🚀")

def get_next_question():
    """

    Print question and options to the user.
    Increment question index by 1.
    The variable = guess, gives input to the user to enter correct answer.
    """
    guesses = []
    correct_guesses = 0
    question_index = 1

    for key in questions:
        print("-------")
        print(key)
        for i in options[question_index-1]:
            print(i)
        guess = input("Enter (A, B, or C):\n ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_index += 1
    display_result(correct_guesses, guesses)

def check_answer(answer, guesses):
    """
    Check users_answer from the
    check_answer function, called it in the
    get next_question function, with parameters (answer ,guess),
    getting the questions KEY, and guess
    if statement to comare if answer and are guees and equal
    if not "not correct!".
    """
    if answer == guesses:
        print("wrong")
        return True
    else:
        print("correct!")
        return False

def display_result(correct_guesses, guesses):
    """
    Takes value from correct guesses variable
    and guesses list as parameters.
    Displays guesses and answers to the
    user and the end of the game.
    """
    print("--------------")
    print("RESULT!")
    print("--------------")
    print("CORRECT ANSWERS:")
    for i in questions:
        print(questions.get(i))
    print("--------------")
    print("YOUR GUESSES:")
    for i in guesses:
        print(i)

def end_game():
    """
    End of game function
    """
    print("End of game!")

questions = {
    "How much do NASA space suits cost?": "A.",
    "How many moons are in our solar system?": "B.",
    "Which is the brightest planet in the night sky?": "C.",
    "How long is one year on Jupiter? ": "A.",
    "Which planet is closest in size to Earth?": "A."
}
options = [
        ["A. 12 million dollars?", "B. 20 million dollars?"],
        ["A. 100 moons?", "B. 181 mooons?"],
        ["A. Mars?", "B. Neptune?", "C.venus?"],
        ["A. 12 years?", "B. 6 years?", "C.8 years?"],
        ["A.Mars?", "B.Venus?"]
]
def main():
    get_next_question()
    check_answer()
    display_result()
    end_game()

if __name__ == '__main__':
    main()