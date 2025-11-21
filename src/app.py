from core.asr import ASR
from core.tts import TTS
import config
import random 
import time
from Game import Game

class App:
    def __init__(self, wakeup_word="iris"):
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
                word = asr_result.text.lower()
            # print('You : ', word)

    def terminate(self):
        self.is_running = False

    def prompt(self):
        prompt = random.choice(config.prompts.wakeup_messages)
        self.tts.speak(prompt)

    def run(self):
        # self.wait_for_wakeup()
        self.prompt()
        time.sleep(0.2)
        
        self.tts.speak('Ok Lets play a fun game.')
        time.sleep(0.5)
        
        # Start Game 
        game = Game(questions=config.questions)
        # self.tts.speak(game.get_intro_text(), 150)
        time.sleep(0.5)

        while game.is_running():
            question = game.get_question()
            self.tts.speak(question, 120)
            answer = self.asr.listen()
            if answer.error:
                self.tts.speak("Can you try again. I didn't hear you properly.")
            elif game.match_answer(answer.text):
                self.tts.speak("Door Unlocked.")
                game.next()
            else:
                self.tts.speak("Nope Wrong Answer. You were cought in the malpractice and thrown to slimey")
                self.terminate()
                return


        self.tts.speak("Congrats You've Escaped From Ship.")
        self.terminate()
