import speech_recognition as sr
from dataclasses import dataclass

@dataclass
class ASR_result:
    text: str
    error: bool

class ASR:
    def __init__(self):
        self.recogonizer = sr.Recognizer()
    
    def listen(self):
        with sr.Microphone() as source:
            audio_text = self.recogonizer.listen(source)
            try:
                # text = self.recogonizer.recognize_google(audio_text)
                text = self.recogonizer.recognize_whisper(audio_text)
                return ASR_result(text=text, error=False)
            except Exception as e:
                print(e)
                return ASR_result(text="", error=True)


    