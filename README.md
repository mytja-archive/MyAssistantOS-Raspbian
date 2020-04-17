# MyAssistantOS-Raspbian
Open-source voice assistant platform by MyTja. It is fully compatible with Raspbian.

# What can I do?
I can play your favorite music, offline and recognize offline. We can have a small chat (also offline). I can use multiple TTS engines. I can gather information from Wikipedia, give you a weather report, tell you a joke, sing you a lullaby, and most importantly, I do not spy on you. There is a lot of things. Since I'm new, I cannot understand properly or I may have a bug. If you see so, then please report on Issues tab on GitHub.

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
```

# Install TTS engine
That is one of the most difficult part if you use Windows. If you use Linux it is simple.
Full tutorial is avaiable here: https://github.com/grigi/talkey
Thanks to grigi.

# Get the API key from OWM
OWM is OpenWeatherMap. If you want My to tell you the weather, then you will need the API key.
Full tutorial is avaiable here: https://github.com/csparpa/pyowm
Thanks to csparpa

Here you go! You are done!

# How to use me?
You say: "Hey, My" or "O.K. My" or "Okay My"
If he senses that succesfully, then he will respond with beep beep sound. Then you say your question. But he doesn't know everything.

# Customizing
You can play offline your favorite song. Download it and rename it to "favorite" it is best to use mp3.

# Offline mode
Offline mode is only for chat and some music. My uses as offline speech recognition service Sphinx. It doesn't recognize the best, but it certanly tries.
