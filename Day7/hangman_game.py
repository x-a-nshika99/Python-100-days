import random
stage = '''
 
    +---+
    |   |
    O   |   
   /|\\ |
   / \\ | 
        |
===========
''','''
    +---+
    |   |
    O   |   
   /|\\ |
   /    | 
        |
============
''','''
    +---+
    |   |
    O   |
   /|\\ |
        |
        |
============
''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
============
''','''
    +---+
    |   |
    O   | 
    |   |
        |   
        |
        |
============
''','''
    +---+
    |   |
    O   |
        |
        |
        |
===========
''','''

    +---+
    |   |
        |
        |
        |
        |
============
'''









word =["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

live = -1

# to do 1 = randomly select a word from the list , print the word to the console for testing purposes

# create placeholder for the randomly selected word
placeholder = ""
# create underscores for each letter in the randomly selected word
word_length = len(word)
for letter in range(word_length):
    placeholder += "_"
print(placeholder)


 
random_word = random.choice(word)
print(random_word)
# to do 2 = take user input for the guessed letter

game_over = False
correct_guesses = []

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    display =""


    for letter in random_word:
        if letter == guessed_letter:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter

        else:
            display += "_"
    print(display)

    if guessed_letter not in random_word:
        live -= 1
        print(stage[live])
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        print(f"You have {6 - live} lives left.")
        if live == 6:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")
