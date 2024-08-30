import speech_recognition as sr
from gtts import gTTS
import os
import platform

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define responses directly in the script
responses = {
    "hello": "Hello there! How can I assist you today?",
    "how are you": "I'm just a program, but I'm doing great! How can I help you?",
    "what is your name": "I'm a voice assistant created to help you with various tasks."
}

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the request.")
            return None

# Function to convert text to speech using gTTS, save it, and play it
def text_to_speech(text):
    if text:
        tts = gTTS(text=text, lang='en')
        filename = 'response.mp3'
        tts.save(filename)
        
        # Play the audio file using the default player
        if platform.system() == 'Windows':
            os.startfile(filename)
        elif platform.system() == 'Darwin':  # macOS
            os.system(f'afplay {filename}')
        else:  # Linux
            os.system(f'mpg321 {filename}')
        
        # Optional: Remove the audio file after playback
        # os.remove(filename)

# Main flow
if __name__ == "__main__":
    # Convert speech to text
    spoken_text = speech_to_text()

    # Find response based on recognized text
    if spoken_text:
        response = responses.get(spoken_text.lower(), "Sorry, I don't have a response for that.")
        text_to_speech(response)
