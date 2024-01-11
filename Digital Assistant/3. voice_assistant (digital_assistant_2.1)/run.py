from __future__ import print_function
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import time
import openai
import webbrowser
import calendar
import pyttsx3
import random
import wikipedia
import wolframalpha
import requests
import winshell
import subprocess
import ctypes
import os.path
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

#API_KEYS
#openai
openai.api_key = "enter API KEY"
#News_API
newsapi = "enter API KEY"
 #Enter your Wolfram Alpha App ID here
APP_ID = 'enter API KEY'


flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning, how may I help you today?")
    elif hour>=12 and hour<18:
        speak("Good day, hope you're having a great day? \n How may I help you? ")
    else:
        speak("Welcome back sir, what is up for the evening? ")
                        
def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

messages=[]
 
class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.assistant()
    
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...")
            audio = R.listen(source)
        try:
            print("Recog...")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text
       
    def assistant(self):
        wish()
        while True:
            self.query = self.STT()
            try:
                if "day" in self.query or "month" in self.query:
                    get_today = today_date()
                    speak(" " + get_today)

                elif "time" in self.query:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    speak('Current time is ' + time)

                elif "where is" in self.query:
                    place = self.query.lower().split().index("is")
                    location = self.query.split()[place + 1:]
                    url = "https://www.google.com/maps/place/" + "".join(location)
                    print("showing location...")
                    speak("This is where " + str(location) + " is.")
                    webbrowser.open(url)

                elif "where am I" in self.query or "my location" in self.query:
                    place = self.query.lower().split().index("is")
                    location = "my location"[place + 1:]
                    url = "https://www.google.com/maps/place/" + "".join(location)
                    print("showing location...")
                    speak("This is where your location")
                    webbrowser.open(url)        
        

                elif "weather update" in self.query.lower() or "is the weather" in self.query.lower() or "weather" in self.query.lower():
                    api_key = 'enter openweather api key'
                    user_input = input("Enter city: ")
                    try:
                        weather_data = requests.get(
                            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

                        if weather_data.json()['cod'] == '404':
                            print("city not found")
                        else:
                            weather = weather_data.json()['weather'][0]['main']
                            temp = round(weather_data.json()['main']['temp'])

                            print(f"The weather in {user_input} is: {weather}")
                            speak(f"The weather is: {weather}")
                            print(f"The temperature in {user_input} is: {temp}ºF")
                            speak(f"The temperature is: {temp}ºF")

                    except Exception as e:
                        reply = "please check your internet connection"
                        print(reply)
                        speak(reply)

                elif "change background" in self.query or "change wallpaper" in self.query:
                    img = r"C:\Users\alfred\Pictures\img"
                    list_img = os.listdir(img)
                    imgChoice = random.choice(list_img)
                    randomImg = os.path.join(img, imgChoice)
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                    print("changing wallpaper")
                    speak("changing wallpaper...")
                    speak("wallpaper changed successfully.")

                elif "open" in self.query:
                    try:
                        if "chrome" in self.query.lower():
                            speak("Opening Google Chrome")
                            os.startfile(
                                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                            )

                        elif "word" in self.query.lower():
                            speak("Opening Microsoft Word")
                            os.startfile(
                                r"WINWORD.EXE"
                            )

                        elif "excel" in self.query.lower():
                            speak("Opening Microsoft Excel")
                            os.startfile(
                                r"EXCEL.EXE"
                            )

                        elif "vs code" in self.query.lower():
                            speak("Opening Visual Studio Code")
                            os.startfile(
                                r"C:\Users\alfred\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                            )
                        elif "pycharm" in self.query.lower():
                            speak("Opening py charm")
                            os.startfile(
                                r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.1.2\bin\pycharm64.exe"
                            )

                        elif "youtube" in self.query.lower():
                            speak("Opening Youtube\n")
                            webbrowser.open("https://youtube.com/")

                        elif "google" in self.query.lower():
                            speak("Opening Google\n")
                            webbrowser.open("https://google.com/")

                        elif "stackoverflow" in self.query.lower():
                            speak("Opening StackOverFlow")
                            webbrowser.open("https://stackoverflow.com/")

                        else:
                            print("Application not recognised")
                            speak("Application not recognised")
                    except Exception as e:
                        print(e)
                        speak("Sorry, an error occured")

                elif "youtube" in self.query.lower():
                    ind = self.query.lower().split().index("youtube")
                    search = self.query.split()[ind + 1:]
                    webbrowser.open(
                        "http://www.youtube.com/results?search_query=" +
                        "+".join(search)
                    )
                    speak("Opening " + str(search) + " on youtube")

                elif "search" in self.query.lower():
                    ind = self.query.lower().split().index("search")
                    search = self.query.split()[ind + 1:]
                    webbrowser.open(
                        "https://www.google.com/search?q=" + "+".join(search))
                    speak("Searching on google...")

                elif "google" in self.query.lower():
                    ind = self.query.lower().split().index("google")
                    search = self.query.split()[ind + 1:]
                    webbrowser.open(
                        "https://www.google.com/search?q=" + "+".join(search))
                    speak("Searching " + str(search) + " on google")

                elif "empty bin" in self.query:
                    winshell.recycle_bin().empty(
                        confirm=True, show_progress=False, sound=True
                    )
                    speak("Recycle Bin Emptied")

                elif "make a note" in self.query or "take note" in self.query or "remember this" in self.query or "write note" in self.query or "write this" in self.query:
                    speak("What would you like me to write down?")
                    note_text = self.STT()
                    note(note_text)
                    speak("I have made a note of that.")

                elif 'music' in self.query:
                    speak("playing music from pc")
                    self.music_dir ="./music"
                    self.musics = os.listdir(self.music_dir)
                    os.startfile(os.path.join(self.music_dir,self.musics[0]))


                elif "news" in self.query or "update news" in self.query:
                    try:
                        print("What category would you like to hear? \n")
                        news_req = self.STT()
                        main_url = (f"https://newsapi.org/v2/everything?{news_req}&sortBy=publishedAt&apiKey={newsapi}")
                        web_app = requests.get(main_url).json()

                        articles = web_app["articles"]

                        i = 1
                        for news in articles:
                            print(str(i) + '.', 'Title:', news["title"])
                            print()
                            print('Description:')
                            print(news["description"])
                            speak(news["description"])
                            print()
                            i = i + 1
                            print('Check for full news at:')
                            print(news['url'])
                            print()
                    except Exception as e:
                        print(e)
                        
                elif "generate image" in self.query:
                    try:
                        print("what image would you like to generate?")
                        image_gen = self.STT()
                        response = openai.Image.create(
                        prompt=image_gen,
                        n=1,
                        size="1024x1024"
                        )
                        image_url = response['data'][0]['url']
                        print(image_gen)
                        print(image_url)
                        webbrowser.open(image_url)
                    except Exception:
                        print("Sorry, I cannot generate that")
                        speak("Sorry, I cannot generate that")
                
                elif "record screen" in self.query or "screen record" in self.query or "screenrecord" in self.query:
                    def record_screen():
                        """
                        Record the screen and save it as an MP4 file.
                        """

                        # Get the width and height of the screen.
                        width = GetSystemMetrics(0)
                        height = GetSystemMetrics(1)

                        # Create a timestamp.
                        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

                        # Create a filename for the MP4 file.
                        file_name = f'{time_stamp}.mp4'

                        # Create a VideoWriter object.
                        fourcc = cv2.VideoWriter_fourcc('m', 'p', "4", 'v')
                        captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

                                # Start recording.
                        while True:
                            # Get a screenshot of the screen.
                            img = ImageGrab.grab(bbox=(0, 0, width, height))

                            # Convert the screenshot to a NumPy array.
                            img_np = np.array(img)

                            # Convert the NumPy array to an RGB image.
                            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

                            # Display the image on the screen.
                            cv2.imshow('Secret Capture', img_final)

                                    # Write the image to the MP4 file.
                            captured_video.write(img_final)

                                    # Check if the user wants to stop recording.
                            if cv2.waitKey(10) == ord('q'):
                                break

                                # Stop recording and close the VideoWriter object.
                        captured_video.release()

                    if __name__ == '__main__':
                        record_screen()
                elif "don't listen" in self.query or "stop listening" in self.query or "do not listen" in self.query:
                    while True:
                        wake_word = self.STT()
                        if wake_word.lower != "assistant":
                            print("\n please say 'assistant'\n")
                        else:
                            speak("welcome back")
                            main()

                else:
                    try:
                        client = wolframalpha.Client(APP_ID)
                        res = client.query(self.query)
                        output = next(res.results).text
                        print("\n" + output)
                        speak(output)
                    except Exception:
                        try:
                            info = wikipedia.summary(self.query, 1)
                            print(info)
                            speak(info)
                        except Exception:
                            try:
                                messages.append({"role": "user", "content": self.query})
                                response = openai.ChatCompletion.create(
                                    model="gpt-3.5-turbo",
                                    messages=messages,
                                )
                                reply = response["choices"][0]["message"]["content"]
                                messages.append({"role": "assistant", "content": reply})
                                print("\n" + reply + "\n")
                                speak(reply)
                            except Exception:
                                print("please check your internet connection")                  
                            
            except Exception as e:
                print(e)
                speak("sorry, I could not process that")
            
            




FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        #self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n")
        #"border: ")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
