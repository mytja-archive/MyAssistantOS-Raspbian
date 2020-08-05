# MyAssistantOS-Raspbian
![mytja-myassistantos-logo](https://user-images.githubusercontent.com/52399966/85886486-803c0680-b7e6-11ea-9e16-a1fd212c0f81.png)

Open-source voice assistant platform by MyTja. It is fully compatible with Raspbian.

Offical pages, useful links & linked repositories: 
- [GitHub Pages](https://mytja.github.io/MyAssistantOS-Raspbian)
- [GitHub Repository](https://github.com/mytja/MyAssistantOS-Raspbian)
- [MyTja Offical page](https://mytja.000webhostapp.com)
- [Travis CI testment](https://travis-ci.org/github/mytja/MyAssistantOS-Raspbian)
- [SDK for MyAssistantOS Raspbian](https://github.com/mytja/MyAssistantOS-Raspbian-SDK)
- [HAM Arduino(Home Automation with My for Arduino & ESP WiFi boards)](https://github.com/mytja/HAM-Arduino)

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
But if you run command ./oobe, this will install libraries for you!

# OOBE and OWM key
*This part is talking about a feature, that isn't tested yet!*

OOBE will automaticly create txt file called "OWM_license.txt", which will be first empty. Your job is to fill it in with an OWM key, so that you will be able to recieve weather information.

# LTS (Long Term Support)
*This releases are new and patches will come*

Long Term Support (LTS) release is a stable release, that is promoted to an LTS edition. Normaly, an LTS edition has 2 years of support, other releases end their support in 3 months from first publishing.

# Install TTS engine
That is one of the most difficult part if you use Windows. If you use Linux it is simple.
Full tutorial is avaiable here: https://github.com/grigi/talkey
Thanks to @grigi.

# Get the API key from OWM
OWM is OpenWeatherMap. If you want My to tell you the weather, then you will need the API key.
Full tutorial is avaiable here: https://github.com/csparpa/pyowm
Thanks to @csparpa

Here you go! You are done with basic part!

# Customizing
You can play offline your favorite song. Download it and rename it to "favorite" it is best to use mp3.

# How to use me?
You say: "Hey, My" or "O.K. My" or "Okay My" or "Wake up, My"

If he senses that succesfully, then he will respond with beep beep sound. Then you say your question. But he doesn't know everything.

# Programming language
I'm based on Python.
Python 2 is already installed on Raspbian.

# Features

## Play music and videos from YouTube
*This part is currently problematic, and YouTube playing won't work as normal. It won't always play your video! We are working on this. More info: https://github.com/mytja/MyAssistantOS-Raspbian/issues/41*

Thanks to VLC for Python, pafy and BeautifulSoup we can play music and video from YouTube. You just say "play <your video name>". He will choose first result so be very detailed.

## Offline mode
*This feature is new and tested*

Offline mode is only for chat and some music. My uses as offline speech recognition service Sphinx. It doesn't recognize the best, but it certanly tries.

## Check for updates
_This part is talking about new feature, that was not tested._

You can check for updates with 2 different ways:
1. Reboot My (tested way)
2. Say "check for updates" or "update" (new feature that is not yet tested)

## Volume commands
Volume commands are
- Maximum
- Minimum
- Volume up/down
- Medium volume

## Timer, stopwatch, alarm and countdown
*This features are partly tested*

### Stopwatch
You can use stopwatch by saying: Hey, My - Stopwatch

### Timer
*Timer doesn't work. We are developing new ways for timer*

You can use timer by saying: Hey, My - Set a timer for XX seconds/minutes/hours/days

### Countdown
You can use countdown by saying: Hey, My - Countdown

Countdown will automaticly countdown from 5 seconds

### Alarm
Recognition for alarm doesn't work the best, so we don't reccomend to use it!

IMPORTANT NOTE: If you turn off your device, your alarms will delete!

## Real time clock (RTC)
Just say "what's the time" or "what's the date" and he will answer you

## Pick a number game
*This game is not functional as first tests showed us! We will continue to resolve it but LTS 1.1 won't solve it!*

Just say pick a number and guess numbers. Tell him only number, not "is it ....".

# Testing & Compatibility

If you could contribute with testing our software, that would be great. Write bugs and ideas in issues. I will respond as fast as possible. Thank you.

Here is a compatibility table:

Devices / OS       | Tested Works | Doesn't Work | Not Tested  | Notes
------------------ | :----------: | :----------: | :---------: | -----
Microsoft Windows 7|      ✔      |             |            | We used eSpeak for TTS engine
Raspbian           |      ✔       |             |            | We tested only Guinea pig 1.0
Debian              |              |             |      ✔     | 
Ubuntu             |              |             |      ✔     | 
Windows 10         |              |             |      ✔     | 
macOS              |              |             |      ✔     | 

# DLL Files

IMPORTANT!!!!!!

DLL files are included, because during the testing I had some problems with dll files. If you are using Windows include them into C:/Windows/System32.

THIS DLL FILES ARE NOT DEVELOPED BY MyTja AND THEY MIGHT NOT BE COMPATIBLE WITH YOUR DEVICE!!! USE THEM AT YOUR OWN RISK!!! FILES ARE SCANNED WITH VIRUSTOTAL AND WITH LATEST RELEASE DO NOT COME WITH ANY MALWARE!!!!

You can get DLL files in dll branch.

# Transition to Python 3
As of 1st January 2020, Python 2 is unsupported. Most of our libraries are unsupported. Since YouTube is making some changes to its platform, it is very hard to maintain by ourselfs. As of version 1.2, our platform will be completelly moved to Python 3 and Python 2 releases (except LTS 1.1) will become unsupported.

Watch for updates here: #43
