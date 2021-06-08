from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from pygame import mixer
import random
import selenium 
import webbrowser
import os
from tkinter import *
import tkinter as tk
import time 
import datetime
import pywhatkit as k
import RPi.GPIO as gpio
from time import sleep
import sys
name =  'MG'
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12 , gpio.OUT,initial=gpio.HIGH)

terminal = 'exo-open --launch TerminalEmulator'
discord = 'https://discord.com/channels/@me'
imager = 'rpi-imager'
firefox = '/usr/lib/firefox-esr/firefox-esr'
visual = '/usr/share/code/code --no-sandbox --unity-launch'
screenshot = 'xfce4-screenshooter'
logout = 'xfce4-session-logout'
shutdown ='/home/pi/Desktop/ALPHA.py'
bluetooth = 'blueman-manager'
appstore = '/home/pi/pi-apps/gui'
hardware = '/home/pi/.local/share/applications/arduino-arduinoide.desktop'
whatsapp = '/home/pi/WhatsAppWeb/WhatsAppWeb'
settings = '/usr/share/desktop-directories/xfce-settings.directory'

# VOICE OF ALPHA

def alpha(audio1):
   
    Alp = pyttsx3.init()
    voices = Alp.getProperty('voices')
    Alp.setProperty('voice', 'english_rp+m1')
    rate = Alp.getProperty('rate')
    Alp.setProperty('rate', 140)
    Alp.say(audio1)
    print(audio1)
    Alp.runAndWait()


# VOICE OF LOGIC

def logic(audio1):
   
    log = pyttsx3.init()
    voices = log.getProperty('voices')
    log.setProperty('voice', 'english_rp+m3')
    rate = log.getProperty('rate')
    log.setProperty('rate', 140)
    log.say(audio1)
    print(audio1)
    log.runAndWait()

#VOICE OF PARROT

def talk(audio1):
    for line in audio1.splitlines():
        text_to_speech = gTTS(text=audio1, lang='en-uk')
        text_to_speech.save('audio1.mp3')
        mixer.init()
        mixer.music.load("audio1.mp3")
        mixer.music.play()
    print(audio1)

#VOICE OF TETRA

def hey(audio):
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
    print(audio)

def mc():
    #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech. 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 0.5
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, duration=2)
        #listens for the user's input
        audio = r.listen(source)
        print("thinking...")
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = mc()
        command = command.lower()

    return command

def app():
    a = mc()
    os.system(a)
  
def bots():

    while True:
        command = mc().lower()


##################################################################################################
##################################################################################################

#ALPHA COMMANDS - (SYSTEM RELATED)

        if 'hello' in command:
            hello = mc()
            if 'alpha' in hello:
                alpha("busy")
            elif 'logic' in hello:
                logic("give me a command sir")
            elif 'tetra' in hello:
                hey("hi there")
            elif 'parrot' in hello:
                talk("Im here")     
            else:
                hey("excuse")
                logic("huh")
                alpha("please repeat")
                hey("say it slowly")

        elif 'guys' in command:
            hey("hi")
            logic("hello")
            alpha("ready")
            hey("lets do this") 
        elif 'application' in command:
            talk("which application?")
            launch =mc()
            if 'terminal' in launch:
                alpha("launching " + launch)
                os.system(terminal)
            elif 'raspberry pi imager' in launch:
                alpha("launching " + launch)
                os.system(imager)
            elif 'discord' in launch:
                alpha("launching " + launch)
                webbrowser.open_new(discord)
            elif 'screenshot' in launch:
                alpha("launching " + launch)
                os.system(screenshot)
            elif 'firefox' in launch:
                alpha("launching " + launch)
                os.system(firefox)
            elif 'logout' in launch:
                alpha("launching " + launch)
                os.system(logout)
            elif 'visual' in launch:
                alpha("launching " + launch)
                os.system(visual)
            elif 'app store' in launch:
                alpha("launching " + launch)
                os.system(appstore)
            elif 'bluetooth' in launch:
                alpha("launching " + launch)
                os.system(bluetooth)
            elif 'hardware' in launch:
                alpha("launching " + launch)
                os.system(hardware)
            elif 'whatsapp' in launch:
                alpha("launching " + launch)
                app(whatsapp)
            elif 'settings' in launch: 
                alpha("launching " + launch)
                os.system(settings)           
        elif 'close' in command:
            talk("which application")
            close = mc()
            if 'terminal' in close:
                alpha("closing" + close)
                os.close(terminal)
            elif 'imager' in close:
                alpha("closing" + close)
                os.close(imager)
            elif 'discord' in close:
                alpha("closing" + close)
                webbrowser.open_new(discord)
            elif 'screenshot' in close:
                alpha("closing" + close)
                os.close(screenshot)
            elif 'firefox' in close:
                alpha("closing" + close)
                os.close(firefox)
            elif 'logout' in close:
                alpha("closing" + close)
                os.close(logout)
            elif 'visual' in close:
                alpha("closing" + close)
                os.close(visual)
            elif 'app store' in close:
                alpha("closing" + close)
                os.close(appstore)
            elif 'bluetooth' in close:
                alpha("closing" + close)
                os.close(bluetooth)
            elif 'hardware' in close:
                alpha("closing" + close)
                os.close(hardware)
            elif 'whatsapp' in close:
                alpha("closing" + close)
                os.close(whatsapp)
            elif 'settings' in close: 
                alpha("closing" + close)
                os.close(settings) 
        elif 'sleep' in command:
            alpha("shutting down")
            break

##################################################################################################
##################################################################################################

#PARROT COMMANDS - (WEB SURFING)
    
        elif 'google' in command:
            talk("what should i search?")
            google = mc()
            k.search(google)

        elif 'youtube' in command:
            talk("what should i search?")
            yt = mc()
            k.playonyt(yt)
        

##################################################################################################
##################################################################################################

#LOGIC COMMANDS - (HARDWARE)

        elif 'light' in command:
            logic("turning on the light")
            gpio.setup(12 , gpio.OUT,initial=gpio.HIGH)
        elif 'led' in command:
            logic("turning off the light")
            gpio.setup(12 , gpio.OUT,initial=gpio.LOW)

##################################################################################################
##################################################################################################

#TETRA COMMANDS - (GAMES)   

        elif 'rand' in command:
            win = Tk()
            win.geometry("300x300")
            win.configure(background='cyan')
            win.title('RANDOM NUMBER')
            #Fname = Label(win , text = 'Email Recipient').place(x=20,y=5)
            fn = IntVar()
            sn = IntVar()
            entry_frame = Entry(win ,width=15,textvariable=fn).place(x=100,y=20)
            entry_frame = Entry(win ,width=15,textvariable=sn).place(x=100,y=50)
            mainloop()
            a = fn.get()
            b = sn.get()
            c = a+1
            d = b-1
            s = random.randint(c,d)
            hey(f"the number is {s}")

if __name__ == "__main__":
      
    while True:
        start = mc()
        if "wake up" in start:
            alpha("hello sir , waking up parrot ,logic and tetra")
            bots()
        elif 'shut' in start:
            alpha("okay sir , see you soon")
            sys.exit()
        else:
            alpha("can u repeat that")
