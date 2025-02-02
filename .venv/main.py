import speech_recognition as sr
import pyttsx3

Listener = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as input_device:
    print("Listening...Say something!")
    voice_content = Listener.listen(input_device)
    text = Listener.recognize_google(voice_content)
    print(text)

engine.say("Hello, I'm VoiceBot.")
engine.runAndWait()

