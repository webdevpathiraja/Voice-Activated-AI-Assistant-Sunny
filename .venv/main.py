import speech_recognition as sr
import pyttsx3

Listener = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as input_device:
    print("Listening...Say something!")

    try:
        voice_content = Listener.listen(input_device, timeout=5)  # Set a timeout for listening
        text = Listener.recognize_google(voice_content)
        print(f"You said: {text}")

        # unable to understand the audio input
        # the audio input didn't result in any recognizable text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        text = None

        # when there's a problem with the network or the connection to the API server.
        # an issue while making a request to Google’s Speech Recognition service.
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        text = None

        # general exception that will catch any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        text = None

# Check if we have valid speech input, and if so, respond back.
if text:
    engine.say(f"You said: {text}")
else:
    engine.say("Sorry, I couldn't understand what you said.")

engine.runAndWait()
