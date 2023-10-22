from pygame import mixer
import time
import random

alphabet = []
morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",  "X": "-..-", "Y": "-.--", "Z": "--.."}
mixer.init()
mixer.music.set_volume(2)

audio1 = "Morse Code/morseaudio/"
audio2 = ".mp3"
runaudio = False
runvisual = False
start = True

type = str.upper(input("Type \"A\" for the audio test and \"B\" for the visual."))
if type == "A":
    runaudio = True
    print("Listen to the sound, then type what letter you think it is. Type \"0\" to quit")
elif type == "B":
    runvisual = True
while runaudio:
    if len(alphabet) == 0:
        print("RESET")
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",  "X", "Y", "Z"]
    answer = alphabet[random.randrange(len(alphabet))]
    #print(audio1 + answer + audio2)
    mixer.music.load(audio1 + answer + audio2) 
    mixer.music.play()
    time.sleep(1)
    mixer.music.stop()
    guess = str.upper(input("Guess: "))
    if guess == "0":
        runaudio = False

    if guess != answer:
        print("WRONG: " + morse[answer] + "  " + answer)
        
    if guess == answer:
        print("Correct! " + morse[answer])
        alphabet.remove(answer)

while runvisual:
    if len(alphabet) == 0:
        print("RESET")
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",  "X", "Y", "Z"]
    answer = alphabet[random.randrange(len(alphabet))]
    guess = str.upper(input(morse[answer] + " : "))
    
    if guess == answer:
        print("Correct!")
        alphabet.remove(answer)
    if guess != answer:
        print("WRONG: " + answer)
    if guess == "0":
        runvisual = False
