import sys
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime,date
import wikipedia
import pyjokes
import pyaudio



listener = sr.Recognizer()
engine = pyttsx3.init()
'''tone = engine.getProperty('voices')
engine.setProperty('voice',tone[1].id)'''

engine.say('Iam Your Assistant siri')
engine.say('What Can I Do For You')
engine.runAndWait()
#print(sr.Microphone.list_microphone_names())

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning!')
        talk('Good Morning!')
    elif hour>=12 and hour<=16:
        print('Good Afternoon')
        talk('Good Afternoon')
    elif hour>16 and hour<21:
        print('Good Evening!')
        talk('Good Evening!')
    else:
        print('Good Night')
        talk('Good Night')

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            talk('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            run_siri(command)
    except:
        print("something Went Wrong!")
        talk("something Went Wrong!")
        sys.exit()


def run_siri(command):
    if 'play' in command:
        song = command.replace('play','')
        print('playing.... '+song)
        talk('playing... ' + song)
        pywhatkit.playonyt(song)

    elif 'open youtube' in command:
        print('opening youtube....')
        talk('opening youtube....')
        webbrowser.open('www.youtube.com')

    elif 'open google' in command:
        print('opening google....')
        talk('opening google....')
        webbrowser.open('www.google.com')

    elif 'open pycharm' in command:
        print('opening pycharm....')
        talk('opening pycharm....')
        dir = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
        os.startfile(dir)
        os.system(dir)

    elif ('good morning' in command) or ('good morning siri' in command) :
        talk('Good Morning Aniket')
        talk("What can i do for you")
        take_command()

    elif ('good afternoon' in command) or ('good afternoon siri' in command) :
        talk('Good afternoon Aniket')
        talk("What can i do for you")
        take_command()

    elif ('good evening' in command) or ('good evening siri' in command) :
        talk('Good evening Aniket')
        talk("What can i do for you")
        take_command()

    elif ('good night' in command) or ('good night siri' in command) :
        talk('Good night Aniket')
        talk('Have a Sweet Dream')

    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print("Current Time Is "+time)
        talk("Current Time Is "+time)

    elif ('what is the date' in command) or ('todays date' in command) or ('date' in command):
        dat = date.today().strftime('%d %B, %Y')
        print("Today's date is "+str(dat))
        talk("Today's date is "+str(dat))

    elif 'who are you' in command:
        print("Iam Your Assistant."
              "\nIam Here to help you get your things done.")
        talk("Iam Your Assistant."
             "\nIam Here to help you get your things done.")

    elif 'what is your favourite food' in command:
        print("sorry i can't say that")
        talk("sorry i can't say that")

    elif 'when you was born' in command:
        print("I was Born on 22 June 2021")
        talk("I was Born on 22 June 2021")

    elif 'what is your name' in command:
        print("My Name is siri")
        talk("My Name is siri")

    elif 'who made you' in command:
        print("Aniket made me")
        talk("Aniket made me")

    elif 'who' in command:
        person = command.replace('who','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    
    elif 'what is' in command:
        srh = command.replace('what is','')
        inf = wikipedia.summary(srh,2)
        print(inf)
        talk(inf)


    elif ('i love you' in command) or ('i love you siri' in command):
        print('Iam in a relationship with wifi')
        talk('Iam in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open google chrome' in command:
        print("opening...", end=" ")
        talk("Opening")
        cd = command.replace('open','')
        print(cd)
        talk(cd)
        dir = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(dir)
        os.system(dir)

    elif ('search' in command) or ('on google' in command):
        search = command.replace('search', '')
        search_main = command.replace('on google','').replace('search','')
        print('searching.... ' + search)
        talk('searching... ' + search)
        pywhatkit.search(search_main)


    elif ('whatsapp' in command) or ('send message on whatsapp' in command) or ('send message' in command):
        talk("please Enter The Number To Send The Message")
        phone_num = input("Please Enter The Number To Send The Message: ")
        talk("Type Your Message Please")
        message = input("Type Your Message Please: ")
        if '+91' not in phone_num:
            phone_num='+91'+phone_num
        print('sending... your message through Whatsapp')
        talk('sending... your message through Whatsapp')
        pywhatkit.sendwhatmsg_instantly(phone_num,message)

    elif ('send mail' in command) or ('send an email' in command):
        pass

    elif ("exit" in command) or ("quit" in command) or ("close" in command) or ("0" in command):
        print("Exiting")
        talk("Exiting")
        sys.exit()

    else:
        talk("please say again!")
        take_command()

if _name=="__main_":
    take_command()
