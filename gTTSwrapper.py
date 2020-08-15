# gTTS wrapper

import io
import pygame
from gtts import gTTS

# To play audio text-to-speech during execution
def say(my_text, language="en", slo=False):
    with io.BytesIO() as f:
        gTTS(text=my_text, lang=language, slow=slo).write_to_fp(f)
        f.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

