from __future__ import print_function
import datetime
import openai
import warnings
import webbrowser
import calendar
import random
import smtplib
import wikipedia
import wolframalpha
import requests
import winshell
import subprocess
import ctypes
import os.path
import smtplib
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

openai.api_key = ""

warnings.filterwarnings("ignore")


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


messages = []
system_msg = input("How would you like to call me?\n ")
print("I am " + system_msg + ", what can I do for you?")


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


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("email", "pass")
    server.sendmail("email", to, content)
    server.close()


def note(text):
    date = datetime.datetime.now()
    
    #str(date).replace(":", "-") + "-note.txt"
     
def file_name(): 
    all_notes = os.listdir()
    file = input("file name: ")
    for note_check in all_notes:
        if file == note_check:
            print("file name already exist")
            return file_name()
        else:
            file = open(file, "w")
    subprocess.Popen(["notepad.exe", file_name])
    
    
def main():
    while True:
        command = input("command: ")
        command = command.lower()
        try:
            if "day" in command or "month" in command:
                get_today = today_date()
                print(" " + get_today)

            elif "time" in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)

            elif "wikipedia" in command or "wiki" in command:
                print("What do you want to know?")
                info_pedia = input("What would you like to learn?\n ")
                info_pedia = info_pedia.lower()
                if "who is" in info_pedia:
                    subject = info_pedia.replace('who is', '')
                    info = wikipedia.summary(subject, 1)
                    print(info)
                elif "what is" in info_pedia:
                    subject = info_pedia.replace('what is', '')
                    info = wikipedia.summary(subject, 1)
                    print(info)
                else:
                    print("Sorry, please check spelling and try again")

            elif "where is" in command:
                place = command.lower().split().index("is")
                location = command.split()[place + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                print("showing location...")
                webbrowser.open(url)

            elif 'you single' in command:
                print('I am in a relationship with WiFi')

            elif "weather update" in command.lower() or "is the weather" in command.lower() or "weather" in command.lower():
                api_key = '30d4741c779ba94c470ca1f63045390a'
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
                        print(f"The temperature in {user_input} is: {temp}ºF")

                except Exception as e:
                    print("I am sorry, please check your internet connection")

            elif "who are you" in command or "define yourself" in command:
                response = ("Hello, I am your Assistant, here to make your life easier.\n  You can command me to "
                            "perform various tasks such as asking questions or opening applications amongst others ")
                print(response)

            elif "made you" in command or "created you" in command:
                print("While I can't give details, let me assure you, humans are involved")

            elif "your name" in command or "call you" in command or "you called" in command:
                print("I don't have one yet")

            elif "who am I" in command:
                print("You must probably be a human")

            elif "why do you exist" in command or "why did you come to this word" in command:
                print("It is a secret")

            elif "sleep" in command:
                print("how many seconds do you want me to sleep")
                sleep_time = input("timer: ")
                a = int(sleep_time)
                print("Sleeping...")
                time.sleep(a)
                print(str(a) + " seconds completed. Now you can ask me anything")

            elif "change background" in command or "change wallpaper" in command:
                img = r"C:\Users\alfred\Pictures\img"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                print("changing wallpaper...")
                print("wallpaper changed successfully.")

            elif "exit" in command or "quit" in command:
                print("exiting...")
                exit()

            elif "open" in command:
                try:
                    if "chrome" in command.lower():
                        print("Opening Google Chrome")
                        os.startfile(
                            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                        )

                    elif "word" in command.lower():
                        print("Opening Microsoft Word")
                        os.startfile(
                            r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                        )

                    elif "excel" in command.lower():
                        print("Opening Microsoft Excel")
                        os.startfile(
                            r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                        )

                    elif "vs code" in command.lower():
                        print("Opening Visual Studio Code")
                        os.startfile(
                            r"C:\Users\alfred\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                        )
                    elif "pycharm" in command.lower():
                        print("Opening py charm")
                        os.startfile(
                            r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.1.2\bin\pycharm64.exe"
                        )

                    elif "youtube" in command.lower():
                        print("Opening Youtube\n")
                        webbrowser.open("https://youtube.com/")

                    elif "google" in command.lower():
                        print("Opening Google\n")
                        webbrowser.open("https://google.com/")

                    elif "stackoverflow" in command.lower():
                        print("Opening StackOverFlow")
                        webbrowser.open("https://stackoverflow.com/")

                    else:
                        print("Application not available")
                        print("Application not available")
                except Exception as e:
                    print("Sorry, an error occured")

            elif "youtube" in command.lower():
                ind = command.lower().split().index("youtube")
                search = command.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                print("Opening " + str(search) + " on youtube")
                

            elif "search" in command.lower():
                ind = command.lower().split().index("search")
                search = command.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                print("Searching on google...")

            elif "google" in command.lower():
                ind = command.lower().split().index("google")
                search = command.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                print("Searching " + str(search) + " on google")

            elif "empty bin" in command:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                print("Recycle Bin Emptied")

            elif "make a note" in command or "take note" in command or "remember this" in command:
                print("What would you like me to write down?")
                note_text = input(">> ")
                note(note_text)
                print("I have made a note of that.")
                
            elif "don't listen" in command or "stop listening" in command or "do not listen" in command:
                while True:
                    wake_word = input(">> ")
                    if wake_word.lower != "assistant" or "Assistant":
                        print("please type 'assistant'")
                    else:
                        main()
            
            elif "wolframalpha" in command.lower():
                print("What can I help you with?")
                wolf_info = input("ask wolframalpha: ")
                if "calculate" in wolf_info:
                    app_id = "YTUJ85-8AG4V9YJ7K"
                    client = wolframalpha.Client(app_id)
                    ind = wolf_info.lower().split().index("calculate")
                    wolf_info = wolf_info.split()[ind + 1:]
                    res = client.query(" ".join(wolf_info))
                    answer = next(res.results).command
                    print("The answer is " + answer)

                elif "what is" in wolf_info or "who is" in wolf_info:
                    app_id = "YTUJ85-8AG4V9YJ7K"
                    client = wolframalpha.Client(app_id)
                    ind = wolf_info.lower().split().index("is")
                    wolf_info = wolf_info.split()[ind + 1:]
                    res = client.query(" ".join(wolf_info))
                    answer = next(res.results).wolf_info
                    print(answer)
                    print(answer)

            elif "record screen" in command or "screen record" in command or "screenrecord" in command:
                try:
                    width = GetSystemMetrics(0)
                    height = GetSystemMetrics(1)
                    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                    file_name = f'{time_stamp}.mp4'
                    fourcc = cv2.VideoWriter_fourcc('m', 'p', "4", 'v')
                    captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

                    print("recording screen...")
                    img = ImageGrab.grab(bbox=(0, 0, width, height))
                    img_np = np.array(img)
                    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                    # _, frame = webcam.read()
                    # fr_height, fr_width, _ = frame.shape
                    # img_final[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]
                    cv2.imshow('Secret Capture', img_final)

                    # cv2.imshow('webcam', frame)

                    captured_video.write(img_final)
                    if cv2.waitKey(10) == ord('q'):
                        break
                except Exception as e:
                    print(e)
                    print("sorry, an error occurred")

            else:
                messages.append({"role": "user", "content": command})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages)
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                print("\n" + reply + "\n")
                print("\n" + reply + "\n")
        except Exception as e:
            print(e)
            print("sorry, check your internet connection")
while True:
    main()
