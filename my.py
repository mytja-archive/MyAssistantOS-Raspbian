import speech_recognition as sr
import time
import pyaudio
from playsound import playsound
import talkey
from random import randint, choice
import wikipedia
import pyowm
import urllib
from bs4 import BeautifulSoup
import pafy
import vlc
import os

InternetMode = 1

owmlicense = open("~/Desktop/OWM_license.txt", "r")
owmlicensekey = owmlicense.read()
print(owmlicensekey)

owm = pyowm.OWM(str(owmlicensekey), subscription_type="free")

jokelist = ["What's the best thing about Switzerland? I don't know, but the flag is a big plus",
            "Hear about the new restaurant called Karma? There is no menu. You get what you deserve",
            "I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.",
            "Mom, where do tampons go? -Where the babies come from, darling. In the stork?",
            "Husband: Wow, honey, you look really different today. Did you do something to your hair? -Wife: Michael, I’m over here!",
            "What do you get when you cross-breed a shark and a cow? -I have no idea but I wouldn’t try milking it.",
            "Tonight I dreamt of a beautiful walk on a sandy beach. -At least that explains the footprints I found in the cat litter box this morning.",
            "Wait for me honey, I’m just finishing my make-up. -You don’t need make-up, Jane. -Oh, Richard…. really? That is so sweet of you! -You need plastic surgery."
            ]

My = False

r = sr.Recognizer()
m = sr.Microphone()

tts = talkey.Talkey()

class wpfilter(object):
   def removeunwanted(self, s):
      s = s.replace("-","")
      s = s.replace("_","")
      s = s.replace("/","")
      s = s.replace("(","")
      s = s.replace(")","")
      s = s.replace("&","")
      s = s.replace(":","")
      return s

wpfilter1 = wpfilter()

def recognitionMode(recognitionint):
    global InternetMode
    InternetMode = recognitionint

def yesOrNo():                                      # Not in use
    with sr.Microphone() as source:
        playsound('media/beep_my.wav')
        print("I'm listening!")
        audio = r.listen(source)
    recognition = r.recognize_google(audio)
    if recognition=="yes":
        InternetMode = 1
        My = False
        tts.say("Ok. Switching to online mode")
    else:
        InternetMode = 0
        My = False
        tts.say("Ok. Switching to offline mode")

def MyMain():
    with sr.Microphone() as source:
        playsound('media/beep_my.wav')
        print("I'm listening!")
        audio = r.listen(source)
    if (InternetMode==0):
        mymainr = r.recognize_sphinx(audio)
    elif (InternetMode==1):
        mymainr = r.recognize_google(audio)
    mymainr = mymainr.lower()
    print(mymainr)
    if mymainr=="how are you":
        print("I'm very good! How are you?")
        tts.say("I'm very good! How are you?")
        My = False
    elif mymainr=="do you like me":
        print("Sure! Why not?")
        tts.say("Sure! Why not?")
        My = False
    elif(mymainr=="do you like alexa" or mymainr=="do you like Alexa" or mymainr=="do you know alexa" or mymainr=="do you know Alexa" or
         mymainr=="do you like Siri" or mymainr=="do you like siri" or mymainr=="do you know siri" or mymainr=="do you know Siri" or
         mymainr=="do you like google assistant" or mymainr=="do you like Google assistant" or mymainr=="do you know google assistant" or mymainr=="do you know Google assistant"):
         
       tts.say("I pay respect to all of voice assistants. Being an voice assistant is not an easy job.")
    elif mymainr=="do you think I'm pretty":
        print("Sure you are!")
        tts.say("Sure you are!")
        My = False
    elif mymainr=="who let the dogs out" or mymainr=="who Let The Dogs Out":
        print("who, who, who, who, who")
        tts.say("who, who, who, who, who")
        My = False
    elif mymainr=="tell me a joke":
        joke = choice(jokelist)
        print(joke)
        tts.say(joke)
        My = False
    elif mymainr=="sing me a lullaby" or mymainr=="play me a lullaby":
        playsound("media/lullaby.wav")
        My = False
    elif mymainr=="sing my favorite song" or mymainr=="play my favorite song":
        playsound("media/favorite.mp3")
        My = False
    elif mymainr=="am I funny":
        tts.say("Sure you are!")
        My = False
    elif mymainr=="who created you" or mymainr=="who designeed you":
        tts.say("I was designed by MyTja Team.")
        My = False
    elif mymainr=="when were you published" or mymainr=="when were you created":
        tts.say("My first software release came out on second of May 2020")
        My = False
    elif mymainr=="how to check for updates":
        tts.say("Reboot me or say check for updates!")
        My = False
    elif mymainr=="what's your favorite drink":
        tts.say("Electricity.")
        My = False
    elif mymainr=="version":
        tts.say("Beta 1.0.2")
        My = False
    elif mymainr=="what's your favorite food" or mymainr=="what is your favorite food":
        tts.say("I like pizza.")
        My = False
    elif mymainr=="go to offline mode":
        tts.say("Going to offline mode.")
        recognitionMode(0)
        My = False
    elif mymainr=="go to online mode":
        tts.say("Going to online mode.")
        recognitionMode(1)
        My = False
    elif mymainr=="power off" or mymainr=="shutdown" or mymainr=="shut down":
        os.system("./poweroff")
    elif mymainr=="reboot":
        os.system("./reboot")
    elif mymainr=="check for updates" or mymainr=="check for system updates" or mymainr=="update" or mymainr=="update your software":
        os.system("./update-from-my")
        kill-this-process() #this kills the process of My, because this function doesn't exist
        My = False
    elif mymainr=="higher volume" or mymainr=="louder" or mymainr=="volume up":
        os.system("./highervolume")
        My = False
    elif mymainr=="lower volume" or mymainr=="quieter" or mymainr=="volume down":
        os.system("./lowervolume")
        My = False
    elif mymainr=="medium volume":
        os.system("./mediumvolume")
        My = False
    elif mymainr=="minimum volume" or mymainr=="minimum":
        os.system("./minvolume")
        My = False
    elif mymainr=="maximum volume" or mymainr=="maximum":
        os.system("./maxvolume")
        My = False
    else:
        query = mymainr
        stopwords = ['what','who','is','a','at','is','he', "who's", "what's", "the", "weather", "in", "like", "plus", "minus", "divided by", "times", "+", "-", "are", "play"]
        querywords = query.split() 
        resultwords  = [word for word in querywords if word.lower() in stopwords]
        result = ' '.join(resultwords)
        print(result)
        
        if (result=="what is the weather like in" or result=="what's the weather like in"):
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            print(result)
            observation = owm.weather_at_place(result)
            w = observation.get_weather()
            temperature = w.get_temperature('celsius')
            humidity = w.get_humidity()

            query = str(w)
            weatherstopwords = ["status=clouds,", "status=clear,"]
            weatherquerywords = query.split() 
            weatherresultwords  = [word for word in weatherquerywords if word.lower() in weatherstopwords]
            weather = ' '.join(weatherresultwords)
            finalweather = str(weather[7])+str(weather[8])+str(weather[9])+str(weather[10])+str(weather[11])+str(weather[12])
            print(weather)
            print(result)
            print(temperature)
            print(humidity)
            print(w)
            temp = temperature["temp"]
            print(temp)
            tts.say("Temperature in " + str(result) + "is" + str(temperature["temp"]) + "degrees celcius. There is a humidity of " + str(humidity) + "percent. It is" + str(finalweather))
        elif (result=="play" or result=="Play"):
            query = mymainr
            swords = ["play"]
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in swords]
            result = ' '.join(resultwords)
            print(result)
            ytlinks = []
            textToSearch = result
            query = urllib.quote_plus(textToSearch)
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                video = 'https://www.youtube.com' + vid['href']
                ytlinks.append(video)
            print(ytlinks[0])
            ytlink = ytlinks[0]
            
            video = pafy.new(ytlink)
            best = video.getbest()
            playurl = best.url

            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
        else:
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            print(result)
            
            summary = wikipedia.summary(result, sentences=1)
            filteredtext = wpfilter1.removeunwanted(summary)
            print(filteredtext)
            print(summary)
            tts.say(str(filteredtext))
        

with m as source:
    r.adjust_for_ambient_noise(source)

def checkForWord(recognizer, audio):
    try:
        wordCheck = recognizer.recognize_google(audio)
        print(wordCheck)
        if wordCheck == "hey my":
            My = True
            print("I'm listening")
            MyMain()
        elif wordCheck == "ok my":
            My = True
            MyMain()
        elif wordCheck == "okay my":
            My = True
            MyMain()
        elif wordCheck == "o. k. my":
            My = True
            MyMain()
        elif wordCheck == "hey mike":
            My = True
            MyMain()
        elif wordCheck == "hey Mike":
            My = True
            MyMain()
        elif wordCheck == "o. k. why":
            My = True
            MyMain()
        elif wordCheck == "okay why":
            My = True
            MyMain()
        elif wordCheck == "o. k. mind":
            My = True
            MyMain()
        elif wordCheck == "okay mind":
            My = True
            MyMain()
        elif wordCheck == "okay Mike":
            My = True
            MyMain()
        elif wordCheck == "o. k. Mike":
            My = True
            MyMain()
        elif wordCheck == "okay mike":
            My = True
            MyMain()
        elif wordCheck == "pay my":
            My = True
            MyMain()
        elif wordCheck == "hate my":
            My = True
            MyMain()
        elif wordCheck == "paymaya":
            My = True
            MyMain()
        elif wordCheck == "wake up my":
            My = True
            MyMain()
        elif wordCheck == "wake up Mike":
            My = True
            MyMain()
    except sr.UnknownValueError:
        print("I cannot understand you! Try again! If I don't understand you anymore, try to power me off!")
    except sr.RequestError as e:
        print("Recognition failed; {0}".format(e))

while My == False:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    checkForWord(r, audio)
