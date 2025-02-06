# Voice Activated AI Assistant - Sunny

## ⭕ Overview 
This project is a simple voice assistant that can recognize speech, provide Wikipedia summaries, and play YouTube videos using voice commands. The assistant listens for a wake word (`sunny`) and then processes user commands accordingly.

## 🤖 Features
- Converts speech to text using `speech_recognition`.
- Converts text to speech using `pyttsx3`.
- Retrieves Wikipedia summaries for queries.
- Plays YouTube videos using `pywhatkit`.
- Stops execution when the user says "stop".

## 👷🏼‍♀️ Requirements
Ensure you have Python installed and the necessary libraries by running:
```sh
pip install speechrecognition pyttsx3 wikipedia pywhatkit
```

## 👩🏼‍💻 Usage
1. Run the script:
   ```sh
   python voice_assistant.py
   ```
2. Speak commands when prompted.
3. Use the wake word `sunny` followed by a command:
   - "Sunny what is Python?" → Provides a short Wikipedia summary.
   - "Sunny who is Elon Musk?" → Provides a short Wikipedia summary.
   - "Sunny play Shape of You" → Plays "Shape of You" on YouTube.
   - "Stop" → Exits the assistant.

## ❎ Error Handling
- If speech is unclear or unrecognized, an appropriate message is displayed.
- If Wikipedia cannot find a result, it informs the user.
- If there is an ambiguous Wikipedia search, the assistant suggests alternatives.

## Notes
- Adjust the speech rate using `pyttsx3` properties if needed.
- Ensure your microphone is working properly for best results.

## License
This project is open-source and free to use. Modify and enhance as needed!

