from core.asr import ASR
from core.tts import TTS

class App:
    def __init__(self, wakeup_word="computer"):
        self.asr = ASR()
        self.tts = TTS()
        # TODO : remove hardcoded voice (1: Microsoft Hazel Desktop) -- platform dependent
        self.tts.setVoice(self.tts.listVoices()[1])
        self.wakeup_word = wakeup_word.lower()
        self.is_running = False

    def wait_for_wakeup(self):
        word = ''
        while self.wakeup_word not in word:
            asr_result = self.asr.listen()
            if not asr_result.error:
                word = asr_result.text
            print('Rec: ', word)

    def terminate(self):
        self.is_running = False



    def run(self):
        self.is_running = True
        while self.is_running:
            self.wait_for_wakeup()
            self.tts.speak("Hello, how can i help you?")
            
            
            self.terminate()