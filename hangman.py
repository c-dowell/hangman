import random

print('H A N G M A N\n')

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    print('')
    if menu == 'play':
        choices = ['python', 'java', 'kotlin', 'javascript']
        letter_validation = 'abcdefghijklmnopqrstuvwxyz'
        word = random.choice(choices)
        guesses = set()

        tries = 8
        while tries > 0:
            hidden_word = ''.join([letter if letter in guesses else '-' for letter in word])
            print(hidden_word)
            if hidden_word == word:
                print("You guessed the word!")
                print("You survived!")
                break

            guess = input(f'Input a letter: ')

            if len(guess) != 1 or guess == '':
                print("You should input a single letter\n")
                continue
            elif guess not in letter_validation:
                print("Please enter a lowercase English letter\n")
                continue
            elif guess in guesses:
                print("You've already guessed this letter")
                if tries == 0:
                    print("You lost!")
                else:
                    print('')
            elif guess not in word:
                print("That letter doesn't appear in the word")
                tries -= 1
                if tries == 0:
                    print("You lost!")
                else:
                    print('')
            else:
                print('')
            guesses.add(guess)
    elif menu == 'exit':
        break
    else:
        continue
