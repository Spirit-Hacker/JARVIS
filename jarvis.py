import datetime
from email.mime import audio
from http import server
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Jarvis , Please tell how may i help you")  

def take_command() : 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pranildhutraj@gmail.com','hqefvfftnhwtuxye')
    server.sendmail('pranildhutraj@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    speak("Hello, Pranil sir")
    wishMe()
   
    query = take_command().lower()

    if 'wikipedia' in query:
        speak("Searching on wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}\n")
            
    elif 'open code' in query:
        codepath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'email' in query:
        try:
            speak("what should i say")
            content = take_command()
            to = "harshwardhanmeshram21@gmail.com" 
            sendemail(to,content)
            print(content)
            speak("email has been sent")

        except Exception as e:
            print(e)
            speak("sorry , sir i was unable to send email")

    