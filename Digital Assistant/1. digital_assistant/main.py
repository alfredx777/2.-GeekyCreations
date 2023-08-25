import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes


#this version of assistant is limited in functionality. See description in README.md
def run_assistant():
    command = input("command: ")
    command = command.lower()
    if 'play' in command:
        song = command.replace('play', '')
        print("playing...")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
    elif 'are you single' in command:
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
    else:
        print("invalid command")

while True:
    run_assistant()
    
