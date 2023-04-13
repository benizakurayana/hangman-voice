# hangman-voice
I designed a hangman game with voice recognition and speech-to-text input/output
# Introduction
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
# Design concept
The reason for choosing such input and output interfaces:
It's because we don't want kids to stare at monitors all day.
When using this program, kids only need to listen to the program and write down
their guesses and draw their own hangman on paper,
while the output on console is only for adults to check what is going on.
