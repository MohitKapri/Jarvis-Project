# 🧠 Jarvis - Your Personal Voice Assistant  

Jarvis is a Python-based voice assistant that can perform a variety of tasks using voice commands.  
It listens for the wake word **"Jarvis"** and then executes commands such as opening apps, telling jokes, fetching the latest news, playing songs, and more.  

---

## 🚀 Features

### 🌐 Web Browsing
- `Open Google` → Opens **Google**
- `Open Facebook` → Opens **Facebook**
- `Open Instagram` → Opens **Instagram**
- `Open YouTube` → Opens **YouTube**

### 🎵 Music
- `Play <song_name>` → Plays a song from your **musicLibrary** (local dictionary of songs and links).  

### 📰 News
- `News` → Fetches and reads out the **top headlines** using the **News API**.  

### 📅 Date & ⏰ Time
- `What is the date?` → Reads today’s date  
- `What is the time?` → Reads the current time  

### 😂 Jokes
- `Tell me a joke` → Reads a random programming joke using the **pyjokes** library  

### 🖥️ System Apps
- `Open Notepad` → Opens **Notepad**  
- `Open Camera` → Opens **Camera**  
- `Open Calculator` → Opens **Calculator**  

### 🔚 Exit
- `Exit / Quit / Stop` → Stops the assistant  

---

## 🛠️ Tech Stack
- **Python**  
- **SpeechRecognition** → For speech-to-text  
- **pyttsx3** → For text-to-speech  
- **requests** → For fetching news  
- **pyjokes** → For random jokes  
- **os** → To open system applications  
- **webbrowser** → To open websites  

---

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
