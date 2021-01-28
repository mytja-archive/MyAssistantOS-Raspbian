# MyAssistantOS-Raspbian
![mytja-myassistantos-logo](https://user-images.githubusercontent.com/52399966/85886486-803c0680-b7e6-11ea-9e16-a1fd212c0f81.png)

# Note
As of 28.1.2020, this library is unmaintained for at least a period of 1 year. It will not recieve any updates during that period.

## *We moved our codes to Python 3. Last supported Python 2 version is LTS1.1p1. Talkey is also depricated, and we moved to gTTS and our gTTS wrapper. Talkey is still TTS engine in LTS1.1p1*

<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mytja/MyAssistantOS-Raspbian"> <img alt="GitHub All Releases" src="https://img.shields.io/github/downloads/mytja/MyAssistantOS-Raspbian/total"> <img alt="GitHub issues" src="https://img.shields.io/github/issues/mytja/MyAssistantOS-Raspbian"> <img alt="GitHub" src="https://img.shields.io/github/license/mytja/MyAssistantOS-Raspbian"> <img src="https://img.shields.io/badge/Python-3-blue">

<img alt="GitHub forks" src="https://img.shields.io/github/forks/mytja/MyAssistantOS-Raspbian?style=social"> <img alt="GitHub stars" src="https://img.shields.io/github/stars/mytja/MyAssistantOS-Raspbian?style=social"> <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/mytja/MyAssistantOS-Raspbian?style=social">

<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/mytja/MyAssistantOS-Raspbian?label=Stable%20release"> <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/mytja/MyAssistantOS-Raspbian?include_prereleases&label=Pre-release">

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
3. Get API key from OWM
4. Plug in speakers and microphones
5. Customizing

# Installing Python libraries
Okay. I would need you to install this libraries with pip:
```
pip install SpeechRecognition
pip install PyAudio
pip install playsound
pip install gTTS
pip install wikipedia
pip install pyowm
pip install PocketSphinx
pip install python-vlc
pip install pafy
pip install youtube-search-python
pip install youtube-dl
pip install StringToInteger
```
But if you run command ./oobe, this will install libraries for you!

# OOBE and OWM key
OOBE will automaticly create txt file called "OWM_license.txt", which will be first empty. Your job is to fill it in with an OWM key, so that you will be able to recieve weather information.

# Releases

## Guinea Pig
Guinea Pig releases are under branch "guineapig" and are first public releases of newest releases!

This releases got support for 3 months under following conditions:
- If none of newer releases (Beta, Stable or LTS) has been released
- If none of new guineapig releases are released

## Beta
Beta releases are under branch "beta"! Less than 20% of releases got its Beta release!

This releases got support for 3 months under following conditions:
- If none of newer releases (Stable or LTS) has been released
- If none of new beta releases are released

## Stable
Stable releases are under branch "master"! Less than 10% of releases got its Stable release!

This releases got support for unlimited time under following conditions:
- If none of newer LTS releases has been released
- If none of new stable releases are released

## LTS (Long Term Support)
*This releases are new and patches will come*

LTS releases are under branch "lts"! Less than 5% of releases got its LTS release! Every release gets also its own branch

Long Term Support (LTS) release is a stable release, that is promoted to an LTS edition. Normaly, an LTS edition has 2 years of support, other releases end their support in 3 months from first publishing.

### LTS release patches

LTS releases can get patches, if:
- LTS version has a bug, that massively influences quality of My and everyday questions and answers

LTS release patches are named like this:
- LTS + version of LTS release + p + patch number (example LTS1.1p1 (Long Term Support release 1.1 patch 1)

If a LTS release patch is published:
- All of its LTS not-patched versions are ended with its support, and this one is supported, which how much time has been left on previous release

# Get the API keys from ...

## OWM
OWM is OpenWeatherMap. If you want My to tell you the weather, then you will need the API key.
Full tutorial is avaiable here: https://github.com/csparpa/pyowm
Thanks to @csparpa

## Wolfram Alpha
*Not yet made!*
Wolfram Alpha is a API key service, that provides answers to expert questions, and calculations, and it's some kind of upgrade to Wikipedia (which will still be used)!

## NewsAPI
*Not yet released!*
NewsAPI is a API for gathering News.

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

## Compatibility

If you could contribute with testing our software, that would be great. Write bugs and ideas in issues. I will respond as fast as possible. Thank you.

Here is a compatibility table:

Devices / OS       | Tested Works | Doesn't Work | Not Tested  | Notes
------------------ | :----------: | :----------: | :---------: | -----
Microsoft Windows 7|      ✔      |             |            | We used eSpeak for TTS engine
Raspbian           |      ✔       |             |            | We are slowly testing 1.2, 1.3 should be fully tested
Debian              |              |             |      ✔     | 
Ubuntu             |              |             |      ✔     | 
Windows 10         |              |             |      ✔     | 
macOS              |              |             |      ✔     | 

## Testing it on _______ machine
This is how it goes!

### Windows
Follow instructions on this branch: https://github.com/mytja/MyAssistantOS-Raspbian/tree/batches/

### Raspbian as virtual machine
I recommend QEMU as emulator, since VirtualBox and VMware, can't emulate ARM32 arhitecture.

You can also use QiEmu (GUI QEMU emulator)

I find this article very useful: https://www.how2shout.com/how-to/how-to-set-up-virtual-machines-with-qemu-gui-on-windows-10.html

# DLL Files

IMPORTANT!!!!!!

DLL files are included, because during the testing I had some problems with dll files. If you are using Windows include them into C:/Windows/System32.

THIS DLL FILES ARE NOT DEVELOPED BY MyTja AND THEY MIGHT NOT BE COMPATIBLE WITH YOUR DEVICE!!! USE THEM AT YOUR OWN RISK!!! FILES ARE SCANNED WITH VIRUSTOTAL AND WITH LATEST RELEASE DO NOT COME WITH ANY MALWARE!!!!

You can get DLL files in dll branch.

# Transition to Python 3
*We succesfully moved to Python 3*

As of 1st January 2020, Python 2 is unsupported. Most of our libraries are unsupported. Since YouTube is making some changes to its platform, it is very hard to maintain by ourselfs. As of version 1.2, our platform will be completelly moved to Python 3 and Python 2 releases (except LTS 1.1) will become unsupported.

Watch for updates here: https://github.com/mytja/MyAssistantOS-Raspbian/issues/43
