"""
File: hangman_voice.py
Name: Jane
-----------------------------
This program is an extension version of the hangman problem in one of my coding assignments,
which originally requires input and output on console and string manipulation only.
Also, this program is devoted to my sister, Alicia, and her sons, Ian and Josh,
who would really need this program.

The main changes made in this program are:
- The answer and the number of guesses allowed are entered on console by user
- Current game status outputted by both console text and text-to-speech
- Input user's guesses by voice recognition.
- Content of output is adjusted due to user requirements
- Turn the string of the guessed word into a list, for easier manipulation
  (I just learned the technique in JavaScript last week.)

The reason for choosing such input and output interfaces:
It's because we don't want kids to stare at monitors all day.
When using this program, kids only need to listen to the program and write down
their guesses and draw their own hangman on paper,
while the output on console is only for adults to check what is going on.
"""


import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound


def speak_output(text):
    """
    This function speaks out loud the given content.
    :param text: string, the content to be speak out loud by gTTS.
    """
    tts = gTTS(text=text, lang="en", slow=True)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")


def get_voice_input():
    """
    This function recognizes user's speech and gets the last alphabet of the sentence said by user.
    :return: string, the last character of the recognized string, in uppercase.
    """
    r = sr.Recognizer()
    print('Listening....')
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        content = r.recognize_google(audio, language='en')
        print(content)
        return content[-1].upper()
    except sr.UnknownValueError:
        print('Please say it again!')
        speak_output('Please say it again')
        return 'error'


def receive_guess():
    """
    This function invokes the get_voice_input function to receive user's guess,
    output the guess by text-to-speech and on console, and return the guess.
    :return: string, the last character of the recognized string, in uppercase.
    """
    guess = 'error'
    while guess == 'error':
        guess = get_voice_input()  # keep invoking get_voice_input() until a guess is returned
    print(f'Your guess: {guess}')
    speak_output(f'Your guess is the letter "{guess}"')
    return guess


def main():
    """
    This program is a game of hangman, letting user enter desired answer
    and number of guesses allowed on console,
    outputting current game status by both console text and text-to-speech,
    and receiving user's guesses by voice recognition.
    """
    # Game setup
    answer = input('Please set the answer: ').upper()
    life = int(input('Please set number of guesses allowed: '))
    ans_len = len(answer)
    bars = []
    for i in range(ans_len):
        bars += ['_']

    # Welcome message
    print('Welcome to the hangman game exclusively made for Ian and Josh.\n'
          'Please make your guess by speaking.\n'
          'To ensure I can get your guess, please say the letter at the end of your sentence.\n'
          'For example: "My guess is the alphabet P" or "Does it have the alphabet P"')
    speak_output('Welcome to the hangman game exclusively made for Ian and Josh.'
                 'Please make your guess by speaking.'
                 'To ensure I can get your guess, please say the letter at the end of your sentence.'
                 'For example: "My guess is the alphabet P" or "Does it have the alphabet P"'
                 "Now let's begin!")
    print(f'The word looks like {" ".join(bars)}\nYou have {life} wrong guesses left.')
    speak_output(f'The word has {ans_len} letters. You have {life} wrong guesses left.')

    # The game
    """
    When playing the hangman game, there are 4 types of situations:
    - User guessed the correct letter, and there are still letters to guess
    - User guessed the correct letter, and all the letters of the word are found out (end game)
    - User guessed the wrong letter, and there are still letters to guess
    - User guessed the wrong letter, and no lives left (end game)
    """
    while life > 0:
        input_ch = receive_guess()  # Get the letter guessed by user

        # Guess is correct
        if input_ch in answer:
            correct_letter_indices = []
            for i in range(ans_len):
                if input_ch == answer[i]:
                    bars[i] = input_ch
                    correct_letter_indices.append(i)

            # Already got all the letters right
            if ''.join(bars) == answer:
                # Console output
                print(f'You win! The word is: {"".join(bars)}')

                # Voice output
                speak_output(f'You win! The word is {"".join(bars)}')

                # End game
                break

            # Still letter(s) to guess
            else:
                # Console output
                print('You are correct!\n'
                      f'The word looks like {" ".join(bars)}\n'
                      f'You have {life} wrong guesses left.\n')

                # Voice output
                speak_output(f'You are correct! The letter "{input_ch}" is the')
                for i in range(len(correct_letter_indices)):
                    if i == 0:
                        speak_output(f'number {correct_letter_indices[i] + 1}')
                    else:  # When the word contains more than one of the current letter
                        speak_output(f'and number {correct_letter_indices[i] + 1}')
                speak_output('letter in the word')
                speak_output(f'You have {life} wrong guesses left.')

        # Guess is wrong
        else:
            life -= 1

            # Already hung
            if life == 0:
                # Console output
                print('You are completely hung : (\n'
                      'Let me give you one last chance!\n'
                      'Please spell the word on your paper, and ask Alicia to check it.')

                # Voice output
                speak_output('You are completely hung....'
                             'Let me give you one last chance!'
                             'Please spell the word on your paper, and ask Alicia to check it.')
                for i in range(3):
                    speak_output(answer)

                # End game
                break

            # Still alive
            else:
                # Console output
                print(f'There is no {input_ch}\'s in the word.\n'
                      f'The word looks like {" ".join(bars)}\n'
                      f'You have {life} wrong guesses left.\n')

                # Voice output
                speak_output(f'There is no "{input_ch}" in the word.'
                             f'You have {life} wrong guesses left.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
