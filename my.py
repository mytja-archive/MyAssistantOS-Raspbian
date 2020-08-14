import speech_recognition as sr
import time
# import pyaudio
from playsound import playsound
import talkey
from random import randint, choice
import wikipedia
import pyowm
import urllib
import pafy
import vlc
import os
import StrToInt as strtoint
import thread
from youtubesearchpython import searchYoutube

alarm1 = []
alarm2 = []
alarm3 = []

daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
monthsOfTheYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def RTCwithAlarm():                # Some functions are not in use and will be used in future
   while True:
      lt = time.localtime()
      dayoftheweek = lt.tm_wday
      day = lt.tm_mday
      month = lt.tm_mon
      year = lt.tm_year
      minute = lt.tm_min
      hour = lt.tm_hour
      if (hour == alarm1 and minute < (alarm[1] + 3)):
         playsound("media/alarm.wav")
      if (hour == alarm2 and minute < 3):
         playsound("media/alarm.wav")
      if (hour == alarm3 and minute < 3):
         playsound("media/alarm.wav")

stopwatch = False
stopwatchTime = 0

timer = False
timerTime = 0

InternetMode = 1

myalarm = True

owmlicense = open("~/Desktop/OWM_license.txt", "r")
owmlicensekey = owmlicense.read()
print(owmlicensekey)

owm = pyowm.OWM(str(owmlicensekey), subscription_type="free") # Here you can change your subscription to OWM and API

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

def redirectPickANumber(number, trial):
   tts.say("Try again")
   PickANumberGame(number, trial+1)
   

def PickANumberGame(number, trial):  # Currently defective - still in production
   with sr.Microphone() as source:
      playsound('media/beep_my.wav')
      print("I'm listening!")
      audio = r.listen(source)
   recognition = r.recognize_google(audio)
   query = recognition
   stopwords = ['is','the','number','it']
   querywords = query.split() 
   resultwords  = [word for word in querywords if word.lower() not in stopwords]
   result = ' '.join(resultwords)
   print(result)
   numberguess = strtoint.StrToInt(result)
   print(numberguess)
   print(number)
   if query == "tell me it":
      tts.say(number)
   if trial < 4:
      if numberguess == number:
         tts.say("You guessed!")
      else:
         
         redirectPickANumber(number, trial)
   else:
      tts.say("Oooof! That was hard. Number was " + str(number))

def Timer(seconds):
   global timer
   global timerTime
   timerTime = seconds
   while timer==True:
      time.sleep(1)
      timerTime = timerTime - 1
      print(timerTime)
      print(timer)
      if timerTime == 0:
         tts.say("Stop!")
         timer = False
         
def Countdown():
   tts.say("5")
   time.sleep(1)
   tts.say("4")
   time.sleep(1)
   tts.say("3")
   time.sleep(1)
   tts.say("2")
   time.sleep(1)
   tts.say("1")
   time.sleep(1)
   tts.say("Start")

def Stopwatch():
   global stopwatch
   global stopwatchTime
   stopwatchTime = 0
   while (stopwatch==True):
      time.sleep(1)
      stopwatchTime = stopwatchTime + 1

def StopwatchStartup():
   global stopwatch
   tts.say("5")
   time.sleep(1)
   tts.say("4")
   time.sleep(1)
   tts.say("3")
   time.sleep(1)
   tts.say("2")
   time.sleep(1)
   tts.say("1")
   time.sleep(1)
   tts.say("Start")
   stopwatch = True
   thread.start_new_thread(Stopwatch, ())

def TimerSetup(sec):
   global timer
   timer = True
   thread.start_new_thread(Timer, (sec))
   

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
    print("I'm listening!")
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
        tts.say("LTS 1.1 patch 1")
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
    elif mymainr=="what's the time" or mymainr=="what is the time":
       lt = time.localtime()
       lth = lt.tm_hour
       ltm = lt.tm_min
       tts.say("It's " + str(lth) + "and" + str(ltm) + "minutes.")
    elif mymainr=="what's the date":
       lt = time.localtime()
       lty = lt.tm_year
       ltmon = lt.tm_mon
       ltday = lt.tm_mday
       ltdayofweek = lt.tm_wday
       print(ltdayofweek)
       th = ""
       if (ltday=="21"):
          th = "twentyfirst"
       elif (ltday=="1"):
          th = "first"
       elif (ltday=="31"):
          th = "thirtyfirst"
       elif (ltday=="22"):
          th = "twentysecond"
       elif (ltday=="2"):
          th = "second"
       elif (ltday=="23"):
          th = "thirtythird"
       elif (ltday=="3"):
          th = "third"
       elif (ltday=="5"):
          th = "fifth"
       elif (ltday=="15"):
          th = "fifteenth"
       elif (ltday=="25"):
          th = "twentyfifth"
       elif (ltday=="30"):
          th = "thirtieth"
       elif (ltday=="20"):
          th = "twentieth"
       else:
          th = str(ltday) + "th"
          
       tts.say("It's " + daysOfTheWeek[ltdayofweek] + th + "Of" + monthsOfTheYear[ltmon-1] + str(lty))
    elif mymainr=="set the stopwatch" or mymainr=="set a stopwatch" or mymainr=="stopwatch":
       StopwatchStartup()
    elif mymainr=="stop":
       global stopwatch
       if (stopwatch==True):
          stopwatch = False
          tts.say("Time (in seconds): " + str(stopwatchTime))
    elif mymainr == "pick a number":
       PickANumberGame(randint(0, 10), 1)
    elif mymainr=="countdown":
       Countdown()
    else:
        query = mymainr
        stopwords = ['what','who','is','a','at','is','he', "who's", "what's", "the", "weather", "in", "like", "plus", "minus", "divided by", "times", "+", "-", "are", "play", "set the alarm at", "set alarm at", "set an alarm at", "set stopwatch", "set the timer for", "set", "timer", "for"]
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
            search = searchYoutube(textToSearch, offset = 1, mode = "dict", max_results = 1)
            result = search.result()["search_result"]
            for video in result:
               vid = video["link"]
            video = pafy.new(vid)
            best = video.getbest()
            playurl = best.url

            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            
               #tts.say("Please be more specific. Maybe tell me an author or something more.")
               
        elif (result=="set the alarm at" or result=="set alarm at" or result=="set an alarm at"):
           stopwords = ["o'clock", "oclock", "sharp", "set the alarm at", "set alarm at", "set an alarm at"]
           resultwords  = [word for word in querywords if word.lower() not in stopwords]
           result = ' '.join(resultwords)
           hoursstr = result[0:2]
           hoursalmostfinal = hoursstr.replace(":", "")
           minstr = result[2:4]
           finalresultm = strtoint.StrToInt(minstr)
           finalresulth = strtoint.StrToInt(hoursalmostfinal)
           
           if (len(alarm1) == 0):
              alarm1.append(finalresulth)
              alarm1.append(finalresultm)
           else:
              if (len(alarm2) == 0):
                 alarm2.append(finalresulth)
                 alarm2.append(finalresultm)
              else:
                 if (len(alarm3) == 0):
                    alarm3.append(finalresulth)
                    alarm3.append(finalresultm)
                 else:
                    tts.say("All my alarm capabilities are full.")
           
        elif result=="set the timer for" or result=="set a timer for":   # Timer
           stopwords = ["set the timer for", "set a timer for"]
           resultwords  = [word for word in querywords if word.lower() not in stopwords]
           result = ' '.join(resultwords)
           timestr = result[0:2]
           timesetstr = result[2:]
           if timesetstr=="hour" or timesetstr=="hours":
              if timestr[1] == " ":
                 timeint = strtoint.StrToInt(timestr[1])
                 timefinal = timeint * 60 * 60
                 TimerSetup(timefinal)
              else:
                 timeint = strtoint.StrToInt(timestr)
                 timefinal = timeint * 60 * 60
                 TimerSetup(timefinal)
           elif timesetstr=="minute" or timesetstr=="minutes":
              if timestr[1] == " ":
                 timeint = strtoint.StrToInt(timestr[1])
                 timefinal = timeint * 60
                 TimerSetup(timefinal)
              else:
                 timeint = strtoint.StrToInt(timestr)
                 timefinal = timeint * 60
                 TimerSetup(timefinal)
           elif timesetstr=="second" or timesetstr=="seconds":
              if timestr[1] == " ":
                 timeint = strtoint.StrToInt(timestr[1])
                 timefinal = timeint
                 TimerSetup(timefinal)
              else:
                 timeint = strtoint.StrToInt(timestr)
                 timefinal = timeint
                 TimerSetup(timefinal)
           elif timesetstr=="day" or timesetstr=="days":
              if timestr[1] == " ":
                 timeint = strtoint.StrToInt(timestr[1])
                 timefinal = timeint * 24 * 60 * 60
                 TimerSetup(timefinal)
              else:
                 timeint = strtoint.StrToInt(timestr)
                 timefinal = timeint * 24 * 60 * 60
                 TimerSetup(timefinal)

        else:
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            print(result)
            
            try:
               summary = wikipedia.summary(result, sentences=1)
               filteredtext = wpfilter1.removeunwanted(summary)
               print(filteredtext)
               final = filteredtext.encode("utf8")
               print(summary)
               tts.say(str(final))
            except:
               tts.say("Sorry, but I cannot tell you that, because a bug in my code.")
        

with m as source:
    r.adjust_for_ambient_noise(source)

def checkForWord(recognizer, audio):
    try:
        wordCheck = recognizer.recognize_google(audio)
        print(wordCheck)
        if wordCheck == "hey my":
            My = True
            
            MyMain()
        elif wordCheck == "ok my" or wordCheck=="okay my" or wordCheck=="o. k. my":
            My = True
            MyMain()
        elif wordCheck == "hey mike" or wordCheck=="hey Mike":
            My = True
            MyMain()
        elif wordCheck == "o. k. why" or wordCheck=="okay why":
            My = True
            MyMain()
        elif wordCheck == "o. k. mind" or wordCheck=="okay mind":
            My = True
            MyMain()
        elif wordCheck == "okay Mike" or wordCheck=="ok Mike" or wordCheck=="o. k. Mike" or wordCheck=="okay mike":
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
        elif wordCheck == "yo My" or wordCheck=="yo my" or wordCheck=="Yo My" or wordCheck=="Yo my":
            My = True
            MyMain()
        elif wordCheck == "stop":
           global stopwatch
           if stopwatch == True:
              global stopwatchTime
              stopwatch == False
              tts.say("Time: " + str(stopwatchTime) + "seconds")
              stopwatchTime = 0
              
    except sr.UnknownValueError:
        print("I cannot understand you! Try again! If I don't understand you anymore, try to power me off!")
    except sr.RequestError as e:
        print("Recognition failed; {0}".format(e))

def MyRecognition():
   while My == False:
      with sr.Microphone() as source:
         print("Say one of my keywords!")
         audio = r.listen(source)
      checkForWord(r, audio)

thread.start_new_thread(RTCwithAlarm, ())
thread.start_new_thread(MyRecognition, ())
