# Hangman With & Without Hints

from random import choice
from string import ascii_lowercase, ascii_letters


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist [list]: List of words (strings)

    Returns a word from wordlist at random
    """
    return choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word      [str]: The word the user is guessing; assumes all letters are lowercase
    letters_guessed [list]: Which letters have been guessed so far; assumes that all
    letters are lowercase

    Returns [boolean]: True if all the letters of secret_word are in letters_guessed;
    False otherwise
    """
    letters_guessed = ''.join(letters_guessed)
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word      [str]: The word the user is guessing
    letters_guessed [list]: Which letters have been guessed so far

    Returns [str]: Comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
    """
    guessed_word = list(secret_word)
    index = 0
    for word in secret_word:
        if word in letters_guessed:
            index += 1
        else:
            guessed_word.remove(word)
            guessed_word.insert(index, "_")
            index += 1
    return ''.join(guessed_word)


def get_available_letters(letters_guessed):
    """
    letters_guessed [list]: Which letters have been guessed so far

    Returns [str]: Comprised of letters that represents which letters have not
    yet been guessed.
    """
    available_letters = ""
    for i in ascii_lowercase:
    	if i not in letters_guessed:
            available_letters += i
    return available_letters


def hangman(secret_word):
    """
    secret_word [str]: The secret word to guess.
    """
    guesses_remaining = 6
    warning_remaining = 3
    letters_guessed = []
    print("="*30)
    print("Welcome to the Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warning_remaining, "warnings left.")
    while guesses_remaining > 0:
        print("-------------")
        print("You have", guesses_remaining ,"guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter:")
        if guessed_letter in ascii_letters and guessed_letter not in letters_guessed: # checking the input condition
            guessed_letter = guessed_letter.lower() # turning uppercase letters to lowercase
            letters_guessed.append(guessed_letter)
            if not is_word_guessed(secret_word, letters_guessed): # if the solution is not found
                if not guessed_letter in secret_word: # if the guessed word is not in the secret word
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -= 1
                else:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else: # correct guess
                score = guesses_remaining * len(set(secret_word))
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("-------------")
                print("Congratulations, you won!")
                print("Your total score for this game is:", score)
                break
        elif guessed_letter in letters_guessed: # if the guessed letter is already picked before
            if warning_remaining == 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                warning_remaining = 3
            else:
                warning_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warning_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        else: # if the guessed letter is an non-ascii lowercase/uppercase char
            if warning_remaining == 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                warning_remaining = 3
            else:
                warning_remaining -= 1
                print("Oops! That is not a valid letter. You have",warning_remaining,"warnings left:", get_guessed_word(secret_word, letters_guessed))

    else: # if no guesses left
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)


def match_with_gaps(my_word, other_word):
    """
    my_word    [str]: Current guess of secret word
    other_word [str]: Regular English word

    Returns [boolean]: True if all the actual letters of my_word match the corresponding
                    letters of other_word, or the letter is the special symbol "_",
                    and my_word and other_word are of the same length; False otherwise.
    """
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word.count(my_word[i]) < other_word.count(my_word[i]):
            return False
        elif my_word[i] in ascii_letters and my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    """
    my_word [str]: Current guess of secret word

    Returns: Nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_) cannot be one of the letters in the word
            that has already been revealed.
    """
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    if len(possible_matches) == 0:
        return "No matches found"
    else:
        return ' '.join(possible_matches)


def hangman_with_hints(secret_word):
    """
    secret_word [str]: The secret word to guess.
    """
    guesses_remaining = 6
    warning_remaining = 3
    letters_guessed = []
    ascii_letters_new = ascii_letters + "*"
    print("Welcome to the Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warning_remaining, "warnings left.")
    while guesses_remaining > 0:
        print("-------------")
        print("You have", guesses_remaining ,"guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guessed_letter = input("Please guess a letter:")
        if guessed_letter == "*":
            print("Possible word matches are: ")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

        elif guessed_letter in ascii_letters_new and guessed_letter not in letters_guessed: # checking the input condition
            guessed_letter = guessed_letter.lower() # turning uppercase letters to lowercase
            letters_guessed.append(guessed_letter)
            if not is_word_guessed(secret_word, letters_guessed): # if the solution is not found
                if not guessed_letter in secret_word: # if the guessed word is not in the secret word
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed) )
                    guesses_remaining -= 1
                else:
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else: # correct guess
                score = guesses_remaining * len(set(secret_word))
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("-------------")
                print("Congratulations, you won!")
                print("Your total score for this game is:", score)
                break

        elif guessed_letter in letters_guessed: # if the guessed letter is already picked before
            if warning_remaining == 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                warning_remaining = 3
            else:
                warning_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warning_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))

        else: # if the guessed letter is an non-ascii lowercase/uppercase char
            if warning_remaining == 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                warning_remaining = 3
            else:
                warning_remaining -= 1
                print("Oops! That is not a valid letter. You have",warning_remaining,"warnings left:", get_guessed_word(secret_word, letters_guessed))

    else: # if no guesses left
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)


# ========== Starting Game ==========
# Hangman without hints

# secret_word = choose_word(wordlist)
# hangman(secret_word)


# ====================================
# Hangman with hints (Type "*" to get the hints)

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
