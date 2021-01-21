import random

print("Welcome to Hangman for Python! A word will be chosen randomly. You will have to guess it!\n")

HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

life = len(HANGMAN) - 1
words = ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo", "chemistry", "sololearn", "bottle", "physics"]
word = words[random.randint(0, len(words) - 1)]
guess = list(len(word) * '*')

letters_guessed = []

print(HANGMAN[0])

while list.count(guess, "*") > 0 and life != 0:
    guess_joined = "".join(guess)
    print("You have {0} lives left. The word so far is {1}.".format(life, guess_joined))
    try:
        char = input("\nEnter a letter: ")
    except:
        print("This is not a valid input")
    else:
        if len(char) > 1 or len(char) == 0:
            print("This has more than one letter or none. Try again!")
            continue
        elif char.isalpha() == False:
            print("I need a letter from a to z.")
            continue
        else:
            if char in letters_guessed:
                print("You already entered that letter!")
                continue
            else:
                char = char.lower()
                letters_guessed.append(char)
        
                for letter in range(len(word)):
                    if char == word[letter]:
                        guess[letter] = char
        
                if char not in word:
                    life -= 1
                    print(HANGMAN[(len(HANGMAN) - 1) - life])
    
                if '*' not in guess:
                    print("Congratulations! {} was the word!".format(word))
                    break
                if life == 0:
                    print("Unlucky, the word was {}. Try next time".format(word))
                    break
        
    