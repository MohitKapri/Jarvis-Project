import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0e97f86742334009a7b626b698133da6"


def speak(text):
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
        song = c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in  c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=ind&apiKey= {newsapi}")
        if r.status_code == 200:
            data = r.json()  # Convert response to JSON
            articles = data.get("articles", [])

            # Print the titles (headlines)
            print("Top Headlines:")
            for i, article in enumerate(articles, start=1):
                speak(f"{i}. {article['title']}")

    else:
        #Let openAI handle the request
        pass

    

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
                audio = r.listen(source , timeout=2 , phrase_time_limit=1)
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                    speak("bol kya huwa")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("jarvis Active....")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)


                        processCommand(command)
        except Exception as e:
         print("Error; {0}".format(e))





