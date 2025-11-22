from core.asr import ASR
from core.tts import TTS
from core.WavPlayer import WavPlayer
import config
import random 
import time

class Game:
    def __init__(self, wakeup_word="iris"):
        self.asr = ASR()
        self.tts = TTS()
        voices = self.tts.listVoices()
        # TODO : remove hardcoded voice (2: Microsoft Zira Desktop) -- platform dependent
        self.tts.setVoice(voices[0])
        self.wakeup_word = wakeup_word.lower()
        self.questions = config.questions
        self.question_idx = 0
        self.wav_player = WavPlayer()

    def __is_running(self):
        return self.question_idx < len(self.questions)
    
    def __wait_for_wakeup(self):
        word = ''
        while self.wakeup_word not in word:
            asr_result = self.asr.listen()
            if not asr_result.error:
                word = asr_result.text.lower()
            print('You : ', word)

    def __get_answers(self):
        return self.questions[self.question_idx].answers

    def __match_answer(self, user_answer: str):
        toks = user_answer.lower().split(' ')
        print("toks: ", toks)
        answers = self.__get_answers()
        for answer in answers:
            matches = 0
            answer = answer.lower()

            for tok in toks:
                tok = tok.lstrip().rstrip()
                if tok == '':
                    continue
                print(tok in answer)
                if tok in answer:
                    matches += 1

            if matches != 0: 
                # even if 1 token in answer match then we accept
                return True 
        
        return False
    

    def __intro(self):
        text = f"You've been captured by aliens who are convinced you're the brightest mind on Earth. Now you're trapped aboard their ship, inside a looping chamber with {len(self.questions)} sealed doors. Each door opens only if you crack the code behind it. Solve them all to advance to the next chamber. Fail… and the aliens will gladly drop you into a pit of hungry, slimy creatures."
        self.tts.speak(text, 150)

    def __get_question(self):
        return self.questions[self.question_idx].question

    def __prompt(self):
        prompt = random.choice(config.dialogues.wakeup_messages)
        self.tts.speak(prompt)

    def __next(self):
        self.question_idx += 1

    def terminate(self):
        self.is_running = False

    def run(self):
        self.__wait_for_wakeup()
        self.__prompt()
        time.sleep(0.5)
        
        self.tts.speak('Ok Lets play game.')
        time.sleep(1.0)

        # Intro
        self.__intro()
        time.sleep(1.0)
        self.wav_player.play('open')

        # Game Loop
        while self.__is_running():
            question = self.__get_question()
            self.tts.speak(question, 120)

            self.wav_player.play('listen')
            answer = self.asr.listen()
            print("You : ", answer.text)

            if answer.error:
                self.wav_player.play('error')
                self.tts.speak(random.choice(config.dialogues.couldnt_catch_messages))
                continue

            if self.__match_answer(answer.text):
                self.wav_player.play('door_open')
                self.tts.speak(random.choice(config.dialogues.correct_messages))
                self.__next()

            else:
                self.wav_player.play('siren')
                self.tts.speak(random.choice(config.dialogues.incorrect_messages))
                self.wav_player.play('eating')
                self.terminate()
                return

        self.wav_player.play('escape')
        self.tts.speak("You did it! Every lock cracked, every challenge conquered. You've escaped the alien ship!")
        self.terminate()


