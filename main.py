import speech_recognition as sr
import pyttsx3
import os

# ===== Voice Setup =====
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except:
            return None

# ===== Android Command Executor =====
def execute(command):
    if "open whatsapp" in command:
        os.system("am start -n com.whatsapp/com.whatsapp.HomeActivity")
    elif "open chrome" in command:
        os.system("am start -n com.android.chrome/com.google.android.apps.chrome.Main")
    elif "back" in command:
        os.system("input keyevent 4")
    elif "home" in command:
        os.system("input keyevent 3")
    elif "tap" in command:
        # Example: "tap 500 1000"
        parts = command.split()
        x, y = int(parts[1]), int(parts[2])
        os.system(f"input tap {x} {y}")
    elif "swipe" in command:
        # Example: "swipe 100 500 300 500"
        parts = command.split()
        x1, y1, x2, y2 = map(int, parts[1:5])
        os.system(f"input swipe {x1} {y1} {x2} {y2}")
    else:
        speak("Command not recognized.")

# ===== Main Loop =====
def main():
    speak("Jarvis Activated")
    while True:
        command = listen()
        if command:
            execute(command)

if __name__ == "__main__":
    main()
