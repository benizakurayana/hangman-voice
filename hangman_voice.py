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
        guess = get_voice_input()
    print(f'Your guess: {guess}')
    speak_output(f'Your guess is the letter "{guess}"')
    return guess


def main():
    """
    This program is a game of hangman, letting user enter desired answer and number of guesses allowed on console,
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
                print(f'You win! The word is: {"".join(bars)}')
                speak_output(f'You win! The word is {"".join(bars)}')

                break

            # Still letter(s) to guess
            else:
                print('You are correct!\n'
                      f'The word looks like {" ".join(bars)}\n'
                      f'You have {life} wrong guesses left.\n')

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
                print('You are completely hung : (\n'
                      'Let me give you one last chance!\n'
                      'Please spell the word on your paper, and ask Alicia to check it.')

                speak_output('You are completely hung....'
                             'Let me give you one last chance!'
                             'Please spell the word on your paper, and ask Alicia to check it.')
                for i in range(3):
                    speak_output(answer)

                break

            # Still alive
            else:
                print(f'There is no {input_ch}\'s in the word.\n'
                      f'The word looks like {" ".join(bars)}\n'
                      f'You have {life} wrong guesses left.\n')

                speak_output(f'There is no "{input_ch}" in the word.'
                             f'You have {life} wrong guesses left.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
