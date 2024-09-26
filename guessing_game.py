import random

hangman_stages = [
     '''
        ----
       |   |
           |
           |
           |
           |
    --------
     ''',
     '''
        ----
       |   |
       O   |
           |
           |
           |
    --------
     ''',
      '''
        ----
       |   |
       O   |
       |   |
           |
           |
    --------
     ''',
     '''
        ----
       |   |
       O   |
      /|   |
           |
           |
    --------
     ''',
    '''
        ----
       |   |
       O   |
      /|\  |
           |
           |
    --------
     ''',
     '''
        ----
       |   |
       O   |
      /|\  |
      /    |
           |
    --------
     ''',
     '''
        ----
       |   |
       O   |
      /|\  |
      / \  |
           |
    --------
     '''
]

word_bank = ['apple', 'book', 'milk', 'guitar', 'tiger', 'bicycle', 'pizza', 'mountain', 'castle', 'elephant', 'ocean', 'universe', 'atmosphere', 'astronomy', 'crocodile', 'rainforest', 'waterfall', 'dolphin', 'octopus', 'flamingo', 'platypus', 'basketball']
word = random.choice(word_bank)
guessed_word = ['_'] * len(word)
attempts = 7

while attempts > 0:
    print('\nWord: ' +  ' '.join(guessed_word))
    print(hangman_stages[len(hangman_stages) - attempts])
    guess = input('Guess a letter: ')

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attemps left: ' + str(attempts))

    if '_' not in guessed_word:
        print('\nCongratulations!! You guessed the word: ' + word)
        break


if '_' in guessed_word:
    print('\nYou\'ve run out of attempts! The word was: ' + word)