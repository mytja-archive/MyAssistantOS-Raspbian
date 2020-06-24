# MyAssistantOS-Raspbian
Open-source voice assistant platform by MyTja. It is fully compatible with Raspbian.

# What can I do?
I can play your favorite music, offline and recognize offline. We can have a small chat (also offline). I can use multiple TTS engines. I can gather information from Wikipedia, give you a weather report, tell you a joke, sing you a lullaby, and most importantly, I do not spy on you. I can also play music and videos from Youtube. There is a lot of things that I can do. Since I'm quite new, I cannot understand properly or I may have a bug. If you see so, then please report on Issues tab on GitHub.

# How to get me working?
1. Get the code from GitHub - If you get it from elsewhere it might not be an original or outdated version.
2. Install Python libraries. That is down this article
3. Install TTS engine.
4. Get API key from OWM
5. Plug in speakers and microphones
6. Customizing

# Installing Python libraries
Okay. I would need you to install this libraries with pip:
```
pip install SpeechRecognition
pip install PyAudio
pip install playsound
pip install talkey
pip install wikipedia
pip install pyowm
pip install PocketSphinx
pip install python-vlc
pip install pafy
pip install bs4
```

# Install TTS engine
That is one of the most difficult part if you use Windows. If you use Linux it is simple.
Full tutorial is avaiable here: https://github.com/grigi/talkey
Thanks to @grigi.

# Get the API key from OWM
OWM is OpenWeatherMap. If you want My to tell you the weather, then you will need the API key.
Full tutorial is avaiable here: https://github.com/csparpa/pyowm
Thanks to @csparpa

Here you go! You are done!

# How to use me?
You say: "Hey, My" or "O.K. My" or "Okay My" or "Wake up, My"

If he senses that succesfully, then he will respond with beep beep sound. Then you say your question. But he doesn't know everything.

# Play music and videos from YouTube
Thanks to VLC for Python, pafy and BeautifulSoup we can play music and video from YouTube. You just say "play <your video name>". He will choose first result so be very detailed.

# Customizing
You can play offline your favorite song. Download it and rename it to "favorite" it is best to use mp3.

# Offline mode
*This feature is new and tested*

Offline mode is only for chat and some music. My uses as offline speech recognition service Sphinx. It doesn't recognize the best, but it certanly tries.

# Testing & Compatibility

If you could contribute with testing our software, that would be great. Write bugs and ideas in issues. I will respond as fast as possible. Thank you.

Here is a compatibility table:

Devices / OS       | Tested Works | Doesn't Work | Not Tested  | Notes
------------------ | :----------: | :----------: | :---------: | -----
Microsoft Windows 7|      ✔      |             |            | We used eSpeak for TTS engine
Raspbian           |      ✔       |             |            | We tested only Guinea pig 1.0
Linux              |              |             |      ✔     | 
Ubuntu             |              |             |      ✔     | 
Windows 10         |              |             |      ✔     | 
macOS              |              |             |      ✔     | 

# DLL Files

IMPORTANT!!!!!!

DLL files are included, because during the testing I had some problems with dll files. If you are using Windows include them into C:/Windows/System32.

THIS DLL FILES ARE NOT DEVELOPED BY MyTja AND THEY MIGHT NOT BE COMPATIBLE WITH YOUR DEVICE!!! USE THEM AT YOUR OWN RISK!!! FILES ARE SCANNED WITH VIRUSTOTAL AND WITH LATEST RELEASE DO NOT COME WITH ANY MALWARE!!!!

You can get DLL files in dll branch.

# Programming language
I'm based on Python.
Python 2 is already installed on Raspbian.

# Check for updates
_This part is talking about new feature, that was not tested._

You can check for updates with 2 different ways:
1. Reboot My (tested way)
2. Say "check for updates" or "update" (new feature that is not yet tested)

# OOBE and OWM key
*This part is talking about a feature, that isn't released yet, or is in early publishment phase*

OOBE will automaticly create txt file called "OWM_license.txt", which will be first empty. Your job is to fill it in with an OWM key, so that you will be able to recieve weather information.

# LTS (Long Term Support)
*This part is talking about special LTS releases, that aren't published yet*

Long Term Support (LTS) release is a stable release, that is promoted to an LTS edition. Normaly, an LTS edition has 2 years of support, other releases end their support in 3 months from first publishing.

# Volume commands
Volume commands are
- Maximum
- Minimum
- Volume up/down
- Medium volume

# Timer, stopwatch and alarm
*This feature is partly tested*

Recognition for alarm doesn't work the best, so we don't reccomend to use it!
You can use stopwatch by saying: Hey, My - Stopwatch
You can use timer by saying: Hey, My - Set a timer for XX seconds/minutes/hours/days

# Real time clock (RTC)
Just say "what's the time" or "what's the date" and he will answer you

# Pick a number game
*This game is not functional as first tests showed us! We will continue to resolve it and hopefuly with stable/LTS 1.1, we will fix it*
Just say pick a number and guess numbers. Tell him only number, not "is it ....".
