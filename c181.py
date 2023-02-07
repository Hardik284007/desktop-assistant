from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(background="light blue")

label = Label(root, text="Welcome to your personal desktop assistant", bg="light blue", font=("Bahnschrift Light", 15, "bold"))
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speech_recognisor = sr.Recognizer()
    speak("How can i help you?")
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat I did not get that')
            speak('Please repeat I did not get that')
    respond(voice_data)
        
def respond(voice_data):
    voice_data=voice_data.lower()
    print(voice_data)
    if "name" in voice_data :
        speak("My name is JARVIS")
        print("My name is JARVIS")
        
    if "time" in voice_data:
        speak("Current time is")
        now = datetime.now()
        current_time= strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data :
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com")
        
    if "video" in voice_data :
        speak("Opening Youtube")
        print("Opening Youtube")      
        webbrowser.get().open("https://youtube.com")


    if "text editor" in voice_data :
        speak("Opening the app")
        print("Opening the app")    
        subprocess.Popen(["notepad.exe"])
    
r_audio()



btn = Button(root, text="Start", bg="red3",fg="white",padx=10, pady=1, font=("Arial", 11, "bold"), relief=FLAT, command=r_audio)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

