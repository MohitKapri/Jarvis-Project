import speech_recognition as sr    #It converts speech(voice) into text.
import webbrowser    #Open websites using default browsers.
import pyttsx3    #Text-to-speech conversion.
import musicLibrary    #Stores a dictionary of song and their links.
import requests    #Sending HTTP requests to APIs.
import datetime    #Work with current date and time.
import pyjokes    #Generate random jokes.
import os    #Interact with the operating system.
import sys    #Handle system-level tasks
import wikipedia    #Search and fetch summaries from Wikipedia.

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "" #Enter your API key here


def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()


#Open Websites
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif  "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")


    #Listen music 
    elif c.lower() .startswith("play"):
        song = c.lower().split(" ",1)[1]
        link =musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry , I don't have that song in my library.")
        
    #Listen Latest News 
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
    

    #Check date & time
    elif "date" in c.lower(): 
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "time" in c.lower():
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")


    #Listen random jokes
    elif "joke" in c.lower():
        joke = pyjokes.get_joke()
        speak(joke)

    
    #Open  System Apps 
    elif "open notepad" in c.lower():
        os.system("notepad")
    elif "open calculator" in c.lower():
        os.system("calc")

    #Wikipedia Search
    elif "who is " in c.lower() or "what is" in c.lower() or "tell me about" in c.lower:
        try:
            query = c.lower().replace("who is","").replace("what is","").replace("tell me about","")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find any information on that. ")

    #Exit
    elif "exit" in c.lower() or "quit" in c.lower() or "stop" in c.lower():
        speak("Shutting down. Goodbye!")
        sys.exit()
    
    else:
        speak("Sorry, I did not understand that command.")
     

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from microphone
        r = sr.Recognizer()
       
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source , timeout=5 , phrase_time_limit=5)
                try:
                    word = r.recognize_google(audio) 
                except sr.UnknownValueError:
                    print("Sorry, I could not understand your voice.")
                    continue
                
                if(word.lower() == "jarvis"):
                    speak("Yes, how can I help you?")
                    #Listen for command
                    with sr.Microphone() as source:
                        print("jarvis Active....")
                        audio = r.listen(source, timeout=5, phrase_time_limit=7)
                        try:
                            command = r.recognize_google(audio)
                            processCommand(command)
                        
                        except sr.UnknownValueError:
                            print("Sorry, I could not understand your voice.")
        except sr.RequestError:
            print("Network error.")
        except Exception as e:
            print(f"Error: {e}")







