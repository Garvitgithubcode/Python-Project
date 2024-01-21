# Voice Assistant
# It takes command and react
# Ex:- open youtube, open facebook, open twitter, tell me the time, send email, Anything search in wikipedia, etc.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser #allows us to search a query supplied as an argument using the search() method
import os
import smtplib  # for mailing

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)
rate = engine.getProperty("rate")
# print(rate)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-gmail', 'your-password')
    server.sendmail('your-gmail', to, content)
    server.close()

if __name__ == '__main__':
    wish_me()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'path'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\123\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.4\\bin\\pycharm64.exe"
            os.startfile(pyPath)

        elif 'email to garvit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry garvit. I am not able to send this email")

        elif 'thanks' in query:
            speak("welcome sir")
            print("welcome sir")
            break

        elif 'stop' in query:
            speak("okay sir")
            print("okay sir")
            break

        else:
            print("No query matched")
            speak("No query matched")

