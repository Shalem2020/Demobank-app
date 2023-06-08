import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Define the audio source (in this case, a microphone)
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

# Use Google's Speech Recognition API to transcribe the audio
try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print(f"Error: {e}")
