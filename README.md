# MyAssistantOS Raspbian .... on Windows
1. Download batch files
2. Download latest version
3. Install Python 3 (or Python 2 (only LTS1.1p1))
4. Modify batch files with usernames and paths
5. Run batch files
PyAudio and PocketSphinx will cause some issues. You really don't need those libraries, but if you want them, then follow this steps:
```
cd <path-to-your-python>
python -m pip install pipwin
python -m pipwin install PyAudio
python -m pipwin install PocketSphinx
```
You shouldn't have any errors

6. Create OWM_license.txt file in directory, at which My is installed.

7. Modify my.py
https://github.com/mytja/MyAssistantOS-Raspbian/blob/0c93da354104d4525c176af81197c1ab5054d0b8/my.py#L52
to:
```
owmlicense = open("OWM_license.txt", "r")
```

8. Plug in your speakers and microphone

9. Run my.py
