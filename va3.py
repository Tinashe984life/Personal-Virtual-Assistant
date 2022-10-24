from operator import contains
from xml.etree.ElementInclude import include
from colorama import Fore
from googlesearch import search
import sys, os, pyttsx3, webbrowser, wikipedia, datetime
import speech_recognition as sr
import re

#Obtaining voice input from the microphone
listener = sr.Recognizer() 

def assistant(audio):
    #initiate the pytts library 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 250)
    engine.say(audio)
    engine.runAndWait()
    


def greet():
    assistant('Hello, How may i help you')

# Taking voice from the microphone and using the microphone as the source
with sr.Microphone() as source:
    print(Fore.BLUE, "Say Something...!")
    greet()
    audio =  listener.listen(source)

#recognize your speech using the Google speech recognizer
try:
    phrase = listener.recognize_google(audio, language='en-uk')
    print(Fore.GREEN, 'You Said ' + Fore.YELLOW, phrase)

    if phrase.lower() == 'open youtube': # Opens Youtube
        assistant('Opening Youtube')
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab("https://www.youtube.com")

    elif phrase.lower() == 'what is the time': #Tells the time 
        time = str(datetime.datetime.now())
        hour = time[11:13] 
        min = time[14:16]
        assistant("The time is "+ hour +" " + min )

    elif "google" in phrase.lower(): #Does a Google search and collects results
        query = phrase.replace('Google', '')
        print(Fore.BLACK, query)
        results = search(query, tld='com', num=10, stop=10, lang='en', pause=3)
        assistant("Here are the results for "+ query)
        for r in results:
            print(Fore.RED, r)
except sr.UnknownValueError:
    print(Fore.RED, 'Hey, I could not understand that')
except sr.RequestError as e:
    print(Fore.RED, 'Request from Google Speech Recognition failed; {0}'.format(e))




