from gtts import gTTS
import os
import speech_recognition as sr
import pyaudio
print(pyaudio.__version__)

def text_to_speech():
    text = input('enter the text:- ')
    tts = gTTS(text)
    tts.save('output.mp3')
    os.system('open output.mp3')

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak...')
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

        try:
            print('Recognizing...')
            text = recognizer.recognize_google(audio)
            print(f'You said: {text}')
        except sr.unKnownValueError:
            print('Sorry, could not understand audio')
        except sr.RequestError as e:
            print(f'Error: {e}')

while True:
    print('Select an option:')
    print('1. text to speech')
    print('2. speech to text')
    print('3. Exit')

    choice = input('choice (1/2/3): ')

    if choice == '1':
        text_to_speech()
    elif choice == '2':
        speech_to_text()
    elif choice == '3':
        print('Exiting the program...')
        break
    else:
        print('Invalid choice. Please try again')
