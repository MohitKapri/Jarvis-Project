import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""


def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif  "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")

    elif c.lower() .startswith("play"):
        song = c.lower().split(" ",1)[1]
        link =musicLibrary.music.get[song]
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry , I don't have that song in my library.")
        
    
    elif "news" in  c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()  # Convert response to JSON
            articles = data.get("articles", [])

            # Print the titles (headlines)
            print("Top Headlines:")
            for i, article in enumerate(articles, start=1):
                speak(f"{i}. {article['title']}")
        else:
            speak("Sorry, I couldn't fetch the news right now.")
    elif "exit" in c or "quit" in c or "stop" in c:
        speak("Shutting down. Goodbye!")
        exit()

    else:
        speak("Sorry, I did not understand that command.")
    

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain auddio from microphone
        r = sr.Recognizer()
       

        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source , timeout=5 , phrase_time_limit=5)
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                    speak("Yes, how can I help you?")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("jarvis Active....")
                        audio = r.listen(source, timeout=5, phrase_time_limit=7)
                        command = r.recognize_google(audio)
                        processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice.")
        except sr.RequestError:
            print("Network error.")
        except Exception as e:
            print(f"Error: {e}")







