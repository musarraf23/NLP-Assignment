from core.asr import ASR
from core.tts import TTS
import config
import random 
import time

class App:
    def __init__(self, wakeup_word="computer"):
        self.asr = ASR()
        self.tts = TTS()
        voices = self.tts.listVoices()
        # TODO : remove hardcoded voice (2: Microsoft Zira Desktop) -- platform dependent
        self.tts.setVoice(voices[2])
        self.wakeup_word = wakeup_word.lower()
        self.is_running = False

    def wait_for_wakeup(self):
        word = ''
        while self.wakeup_word not in word:
            asr_result = self.asr.listen()
            if not asr_result.error:
                word = asr_result.text
            print('You : ', word)

    def terminate(self):
        self.is_running = False

    def prompt(self):
        prompt = random.choice(config.prompts.wakeup_messages)
        self.tts.speak(prompt)

    def run(self):
        self.is_running = True
        while self.is_running:
            self.wait_for_wakeup()
            self.prompt()
            time.sleep(0.2)
            self.tts.speak('Ok Lets play a fun game.')
            time.sleep(0.5)
            self.tts.speak("You've been captured by aliens who believe you're the smartest person on Earth, and now you're trapped aboard their spaceship. To escape, you must crack a series of codes. You're confined in a recursive room with four doors, and each door will only open if you solve its code. Succeed, and you move on to the next room; fail, and the aliens will toss you into a pit of hungry, slimy creatures.", 150)
            self.terminate()
