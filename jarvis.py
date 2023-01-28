import pyttsx3  # pyttsx3 is text-to-speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

# using the voice of the windows using the api
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir!")
    elif (hour >= 12 and hour < 6):
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak(" I am Jarvis AI, How may I help you?")


def takecommand():
    '''It takes microphone input from the user and return the string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your-email","your-password")
    server.sendmail('you-email', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing taks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "E:\\movies"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strtime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(code_path)

        elif ' send email' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                print("Enter the email of the person to whom you want to send the email")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry, I am not able to send the Email at the moment")
