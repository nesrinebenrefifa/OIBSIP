import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Initialize recognizer and TTS engine
R= sr.Recognizer()
E = pyttsx3.init()

def speak(text):
    E.say(text)
    E.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = R.listen(source)
        try:
            command = R.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def tell_date():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    speak(f"Today's date is {current_date}")

def web_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search for" in command:
            search_query = command.split("search for")[-1].strip()
            speak(f"Searching for {search_query}")
            web_search(search_query)
        elif "Goodbye" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
