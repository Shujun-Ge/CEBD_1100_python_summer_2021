#  “HangMan Game” program that realize the classic word-guessing game.

# Display the status of the person, the letters chosen, the letters available
# and the current sentence being guessed.

# Generate random integer point values
import string
from random import randint

# Build the Hangman Figure
hangman = []  # Generate the Hangman list
# Describe different status of stick guy in the Hangman list in sequence
hangman.insert(0, """   

  """)
hangman.insert(1, """   O

  """)
hangman.insert(2, """   O
   |
  """)
hangman.insert(3, """   O
   |\\
  """)
hangman.insert(4, """   O
  /|\\
  """)
hangman.insert(5, """   O
  /|\\
    \\""")
hangman.insert(6, """   O
  /|\\
  / \\""")

# Set Delimiter
num_stars = 65  # The length of the Delimiter
bar_of_stars = "*" * num_stars

# Set a Question Bank
game_list = ["A FISH CALLED WANDA", "LIFE OF BRIAN", "THE MEANING OF LIFE", "HANG IN THERE"]

print("Welcome to HangMan Game!")
print(bar_of_stars)  # Delimiter

# Mode Selection
print("Mode 1 : Use the question bank that comes with the game")
print("Mode 2 : Use your own question")
mode_control = 1
while mode_control:
    mode = input("Please enter 1 or 2 to select the mode.\n")
    if mode.strip() == "1":
        phrase = game_list[randint(0, len(game_list)-1)]  # Choose one phrase from the question bank randomly
        mode_control = 0
    elif mode.strip() == "2":
        print(bar_of_stars)  # Delimiter
        phrase = input("Please Enter your question : \n")   # Enter you own phrase
        mode_control = 0
    else:
        print("No this mode. Please re-enter.")

guessed_phrase = []         # Generate the guessed phrase
num_correct = 0     # Generate a counter for correct guesses
for i in range(len(phrase)):
    if phrase[i] == " ":
        guessed_phrase.append(" ")
        num_correct += 1        # Count the spaces in the phrase
    else:
        guessed_phrase.append("_")

# Set Up Tips About Letters and Initialization
letters_available = list(string.ascii_uppercase)     # Generate the letters available list
letters_chosen = []         # Generate the letters chosen list
num_available = 26      # Initialize the number of available letters
num_chosen = 0          # Initialize the number of chosen letters
state = 6       # Initialize the status of Hangman


while state:
    print(bar_of_stars)  # Delimiter
    # Display the status of the person
    print(hangman[state])
    # Display the current sentence being guessed
    print("Phrase : ", end=" ")
    print(*guessed_phrase, sep="")
    # Display Letters Available
    print("\nLetters Available \t({:2}): ".format(num_available), end=" ")
    for j in range(num_available):
        print(letters_available[j], end=" ")
    # Display Letters Chosen
    print("\nLetters Chosen \t\t({:2}): ".format(num_chosen), end=" ")
    for k in range(num_chosen):
        print(letters_chosen[k], end=" ")

    # Start Process
    print("\n\nPlease choose a letter or write “solve” to solve the puzzle.")
    letter_guess = input()  # Enter the guessed content

    # "solve" Keyword Function
    if letter_guess.lower() == "solve":
        state = 0
        answer_solve = input("What is the phrase?\n")
        if answer_solve.upper() == phrase:
            print(bar_of_stars)  # Delimiter
            print("Correct, you win.")
        else:
            print(bar_of_stars)  # Delimiter
            print("Sorry, you lose.")

    # Single Letter Comparison
    elif letter_guess.upper() in letters_available:
        # The Change of Letters Available and Letters Chosen
        num_available -= 1
        num_chosen += 1
        letters_available.remove(letter_guess.upper())
        letters_chosen.append(letter_guess.upper())

        # Judge the input letter
        # Right Letter
        if letter_guess.upper() in phrase:
            for i in range(len(phrase)):
                if letter_guess.upper() == phrase[i]:
                    num_correct += 1
                    guessed_phrase[i] = phrase[i]
                else:
                    pass
        # Wrong Letter
        else:
            state -= 1
            if state == 0:
                print(bar_of_stars)  # Delimiter
                print("Sorry, you lose. You have no chance")
                print("Correct Phrase is", phrase)
            else:
                pass

        # Judge if the phrase being guessed is correct completely
        if num_correct == len(phrase):
            print(bar_of_stars)  # Delimiter
            print("Correct, you win.")
            print("Correct Phrase is", phrase)
            state = 0
        else:
            pass
    else:
        print(bar_of_stars)  # Delimiter
        print("Sorry, invalid input! Please re-enter.")
        print("Please enter a letter shown in Letters Available or enter the phrase \"solve\" to "
              "guess the phrase directly.")

print(bar_of_stars)  # Delimiter
print("Thank you for playing the game!")