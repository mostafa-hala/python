# Ahmed Ashraf : word_is_found_dictionary, validate_letter_found, validate_letters, validate_win
# Ahmed Dusuki : list_of_words, random word picked, first name try except validation, input_letter validation, show_progress
# Mostafa Mohamed : main function, connect all function together and validation the input user data

from random import randint

list_of_words = [
    "apple",
    "banana",
    "grape",
    "guava",
    "pineapple",
    "watermelon",
    "melon",
    "orange",
]

rand_idx = randint(0, len(list_of_words) - 1)
chosen_word = list_of_words[rand_idx]

# creates a dictionary with initial value = False for all index of characters. This dictionary's indices are then
# set to true for each found character
def word_is_found_dictionary():
    word_found = {}
    for i in range(len(chosen_word)):
        word_found.update({str(i): False})
    return word_found


# Changes indices of each found letter to True
def validate_letters(letter, dictionary):
    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            dictionary[str(i)] = True


# checks if letter input by user is correct
def validate_letter_found(letter):
    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            return True
    return False


# take valid letter input from user
def input_letter():
    letter = " "
    while not letter.isalpha() or len(letter) != 1:  # must be alpha and of length 1
        letter = input("Enter your guess letter: ")
    letter = letter.lower()  # change letter to lowercase
    return letter


# Show progress of current word
def show_progress(dictionary):
    for i in range(len(chosen_word)):
        if dictionary[str(i)]:
            print(chosen_word[i], end="")
        else:
            print("_", end="")
    print()


# Checks if the all the letters are found then returns true meaning user has won
def validate_win(dictionary):
    for i in range(len(chosen_word)):
        if not dictionary[str(i)]:
            return False
    return True


# main function
while True:
    print(
        "\n\t\t\t********************************************HangMan********************************************\n"
    )
    # debug: print(chosen_word)
    guessed = []
    letter = ""
    dictionary = word_is_found_dictionary()
    while True:
        try:
            name = input("\nEnter your first name: ")
            if not name.isalpha():
                raise Exception("Use only letters!")
            break
        except Exception as e:
            print(e)

    print("\nWelcome " + name + " \U0001F600!")
    print("\nAre you ready you have only 8 chances to guess the correct word!\n")
    guess_count = 0
    guess_limit = 8
    won = False
    while not won:
        if guess_count < guess_limit:
            # print word places
            show_progress(dictionary)

            letter = input_letter()

            # this if condition make check if user input same letter twice
            if letter in guessed:
                print("\nYou already guessed this letter before!")
                continue
            guessed.append(letter)

            check_letter = validate_letter_found(letter)
            # this if condition make check if user input right letter then know the index of this letter
            if check_letter == True:
                validate_letters(letter, dictionary)

            # this function if user input a wrong guess it will return a warning message
            else:
                x = (guess_limit) - int(guess_count)
                print("Take care! \n" + str(x - 1) + " guesses left.")
                guess_count = guess_count + 1
                if x - 1 == 0:
                    break

            check_word = validate_win(dictionary)
            # this condition check if the gussed word is the right word
            if check_word == True:
                won = True
                break
    if won == True:
        show_progress(dictionary)
        print("\nCongratulations " + name + "\U0001F600 \nYou WON!!")
    else:
        print(f"\nUnfortunately you lost! The word was {chosen_word}.")

    rand_idx = randint(0, len(list_of_words) - 1)
    chosen_word = list_of_words[rand_idx]
