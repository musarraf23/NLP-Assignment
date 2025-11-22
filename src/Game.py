from core.asr import ASR
from core.tts import TTS
import config
import random 
import time
import Question

class Game:
    def __init__(self, wakeup_word="iris"):
        self.asr = ASR()
        self.tts = TTS()
        voices = self.tts.listVoices()
        # TODO : remove hardcoded voice (2: Microsoft Zira Desktop) -- platform dependent
        self.tts.setVoice(voices[2])
        self.wakeup_word = wakeup_word.lower()
        self.questions = Question.questions
        self.question_idx = 0

    def __is_running(self):
        return self.question_idx < len(self.questions)
    
    def __wait_for_wakeup(self):
        word = ''
        while self.wakeup_word not in word:
            asr_result = self.asr.listen()
            if not asr_result.error:
                word = asr_result.text.lower()
            print('You : ', word)

    def __get_answer(self):
        return self.questions[self.question_idx].answer

    def __match_answer(self, user_answer: str):
        toks = user_answer.lower().split(' ')
        actual_answer = self.__get_answer().lower()
        score = 0
        for tok in toks:
            if tok in actual_answer:
                score += 1
        return score != 0 # even if 1 token in answer match then we accept

    def __get_intro_text(self):
        return f"You've been captured by aliens who believe you're the smartest person on Earth, and now you're trapped aboard their spaceship. To escape, you must crack a series of codes. You're confined in a recursive room with {len(self.questions)} doors, and each door will only open if you solve its code. Succeed, and you move on to the next room; fail, and the aliens will toss you into a pit of hungry, slimy creatures."

    def __get_question(self):
        return self.questions[self.question_idx].question

    def __prompt(self):
        prompt = random.choice(config.prompts.wakeup_messages)
        self.tts.speak(prompt)

    def __next(self):
        self.question_idx += 1

    def terminate(self):
        self.is_running = False

    def run(self):
        # self.wait_for_wakeup()
        self.__prompt()
        time.sleep(0.2)
        
        # self.tts.speak('Ok Lets play a fun game.')
        # time.sleep(0.5)

        # Intro        
        # self.tts.speak(self.__get_intro_text(), 150)
        # time.sleep(0.5)

        # Game Loop
        while self.__is_running():
            question = self.__get_question()
            self.tts.speak(question, 120)
            answer = self.asr.listen()
            if answer.error:
                self.tts.speak("Can you try again. I didn't hear you properly.")
            elif self.__match_answer(answer.text):
                self.tts.speak("Door Unlocked.")
                self.__next()
            else:
                self.tts.speak("Nope Wrong Answer. You were cought in the malpractice and thrown to slimey")
                self.terminate()
                return


        self.tts.speak("Congrats You've Escaped From Ship.")
        self.terminate()


