import vlc
from gtts import gTTS 
from time import ctime
import webbrowser
import pyperclip
import os
import urllib
from google import search
from bs4 import BeautifulSoup
import sys

def google_scrape(url):
    thepage = urllib.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text


class Alice(object):
    def __init__(self):
        self.COMMAND_INITIATOR = ["alice", "allys", "ales"]
        self.STOP_LISTENING_COMMANDS = [
            "go away", "stop listening", "shut down"
        ]

    def speak(self, audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("audio.mp3")
        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new('audio.mp3')
        player.set_media(media)
        player.play()

    def handle_action(self, command):
        size = len(command) 
        command = command.lower()
        print("Received command:", command)
        if not any(sub_command in command for sub_command in self.COMMAND_INITIATOR):
            return

        if "time" in command:
            self.speak("Its " + str(ctime()))
            return 1
        if "how are you" in command:
            self.speak("Sorry I have a boyfriend")
            return 1

        if "where is" in command:
            address=command[15:]     
            print(command)   #address=pyperclip.paste()
            webbrowser.open('https://www.google.com/maps/place/'+ address)
            return 1
        
        if "what is" in command:
            i = 1
            
            query=command[13:]
            for url in search(query, num=5,stop=5):
              a = google_scrape(url)
              print(str(i) + ". " + a)
              print(url)
              webbrowser.open(url)
              i += 1
            return 1    
        
        if "Search for" in command:
            i = 1
            query=command[17:]
            for url in search(query, stop=10):
              a = google_scrape(url)
              print(str(i) + ". " + a)
              print(url)
              webbrowser.open(url)
              i += 1
            return 1

        if "Search " in command:
            i = 1
            query=command[13:]
            for url in search(query, stop= 10):
              a = google_scrape(url)
              print(str(i) + ". " + a)
              print(url)
              webbrowser.open(url)
              i += 1
            return 1
        
        if "go away":
            return 0
        
        if "shut down":        
            return 0
        
        if "switch off":
            return 0