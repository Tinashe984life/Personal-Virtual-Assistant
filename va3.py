from colorama import Fore
from googlesearch import search
import sys, os, pyttsx3, webbrowser, wikipedia, datetime
import speech_recognition as sr
import re
import pywhatkit
import smtplib

contacts = {
    "James": "madtinashe@gmail.com",
    "John": "tinashe984life@gmail.com"
}

#Obtaining voice input from the microphone
listener = sr.Recognizer() 

def assistant(audio):
    #initiate the pytts library 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
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

    elif "look up" in phrase.lower(): #Does a Google search and prints the top 10 url results in the console
        query = phrase.replace('look up', '')
        print(Fore.BLUE, query)
        results = search(query, tld='com', num=10, stop=10, lang='en', pause=3)
        assistant("Here are the results for "+ query)
        for r in results:
            print(Fore.RED, r)

    elif "google" in phrase.lower(): #Does a google search and shows results in the browser
        query = phrase.replace("Google", "")
        print(Fore.BLUE, query)
        assistant("Here are the google results for " + query)
        pywhatkit.search(query)

    elif "go to" in phrase.lower():
        site = phrase.replace('go to', '')
        site = site.strip()
        print(Fore.BLUE, site)
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(site)

    elif "play" in phrase.lower(): #Play songs from Youtube
        song = phrase.replace('play', '')
        assistant("playing" + song)
        pywhatkit.playonyt(song)
    
    elif "who is" in phrase.lower(): #Search famous people on wikipedia
        person = phrase.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        assistant(info)
    
    elif "what is" in phrase.lower(): #Search info from wikipedia with "What is" command
        query = phrase.replace("what is", "")
        info = wikipedia.summary(query, 3)
        print(info)
        assistant(info)
    
    elif "search" in phrase.lower():
        query = phrase.replace("search", "")
        info = wikipedia.summary(query, 2)
        print(info)
        assistant(info)
    

except sr.UnknownValueError:
    print(Fore.RED, 'Hey, I could not understand that')
    assistant("Hey, I could not understand that")
except sr.RequestError as e:
    print(Fore.RED, 'Request from Google Speech Recognition failed; {0}'.format(e))




