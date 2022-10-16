"""
Print welcome message to the user.
User To enter name.
"""
import time
count = "5 4 3 2 1"
for i in count:
    print(i)
    time.sleep(0.5)
welcome = input("PLEASE ENTER YOUR NAME! :")
print("-----------------------------------")
print(f"HELLO {welcome}")
print("-----------------------------------")
print("WELCOME TO SPACED OUT!👽 ")
print("-----------------------------------")
print(f"{welcome} COMPARE YOUR KNOWLEDGE TO THE 10 QUESTIONS, GOOD LUCK!👾 ")
playing = input("PRESS ANY KEY TO START! ")
def get_next_question():
    """

    Print question and options to the user.
    Increment question index by 1.
    The variable = user_guess, gives input to the user to enter correct answer.
    user_guess to give user input, Enter A,B or C.
    """
    guesses = []
    correct_guesses = 0
    options_index = 1
    for key in questions:
        print("-------")
        print(key)
        for i in options[options_index-1]:
            print(i)
        user_guess = input("Enter (A, B, or C):\n ")
        user_guess = user_guess.upper()
        guesses.append(user_guess)

        correct_guesses += check_answer(questions.get(key), user_guess)
        options_index += 1

    display_result(correct_guesses, guesses)
def check_answer(answer, user_guess):
    """
    Check users_answer from the
    check_answer function, called it in the
    get next_question function, with parameters (answer ,guess),
    getting the questions KEY, and guess
    if statement to comare if answer and are guees and equal
    if not "not correct!".
    """
    
    if answer == user_guess:
        user_guess += 1
        print("")
        return True
    else:
        print("")
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
    "Which planet is closest in size to Earth?": "A.",
    "Which planet is named after the Roman god of war?": "C.",
    "How many engines are on a space shuttle?": "B.",
    "What country put a man intp sapce first?": "A.",
    "What colour is the heat sheild facing the sun?": "C.",
    "What contributes towards space being so dark?": "C."
}
options = [
        ["A. 12 million dollars?", "B. 20 million dollars?"],
        ["A. 100 moons?", "B. 181 mooons?"],
        ["A. Mars?", "B. Neptune?", "C.venus?"],
        ["A. 12 years?", "B. 6 years?", "C.8 years?"],
        ["A. Mars?", "B.Venus?"],
        ["A. Saturn?", "B.venmus?", "C. Mars?"],
        ["A. Three?", "B. Two", "C. One?"],
        ["A. Russia?", "B. USA?", "C. China?"],
        ["A. black?", "B. Grey?", "C. White?"],
        ["A. Not enough light?", "B. to big?", "C. It's a vacuum?"]
]
def main():
    get_next_question()
    check_answer()
    display_result()
    end_game()
if __name__ == '__main__':
    main()