import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import speech_recognition as sr
from config.settings import load_env
from assistant import router
import pyttsx3 as py
recognizer = sr.Recognizer()
engine = py.init()



def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    # Initialize recognizer

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source,phrase_time_limit= 20)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return "sorry, i did not understand that."
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    return ''

def main():
    print("Starting the assistant...")
    load_env()
    speak("Hello! I am  Purushu. How can I help you today?")
    
    while True:
        command = listen()
        if command:
            response = router.handle_command(command)
            if response:
                speak(response)
                if response == 'Goodbye! Aswin':
                    break
            
if __name__ == "__main__":
    main()




#need to to weadher app api also openai api
    