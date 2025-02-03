import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
player = pyttsx3.init()


def listen():
    """Capture voice input and convert it to text."""
    with sr.Microphone() as input_device:
        print("I am ready, Listening ....")
        try:
            voice_content = listener.listen(input_device)
            text_command = listener.recognize_google(voice_content).lower()
            print(f"User said: {text_command}")
            return text_command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None


def talk(text):
    """Convert text to speech and speak it out."""
    player.say(text)
    player.runAndWait()


def get_summary(command):
    """Fetch a short Wikipedia summary while handling errors."""
    try:
        info = wikipedia.summary(command, sentences=2, auto_suggest=True)
        return info
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your search is ambiguous. Please specify more clearly. Options: {', '.join(e.options[:5])}."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find anything related to your request."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def run_voice_bot():
    """Main function to process voice commands."""
    command = listen()

    if command and "sunny" in command:
        command = command.replace("sunny", "").strip()

        if "what is" in command or "who is" in command:
            command = command.replace("what is", "").replace("who is", "").strip()
            info = get_summary(command)
            talk(info)
        elif "play" in command:
            command = command.replace("play", "").strip()
            talk(f"Playing {command} on YouTube")
            pywhatkit.playonyt(command)
        else:
            talk("Sorry, I am unable to find what you are looking for.")


# Run the voice assistant
run_voice_bot()
