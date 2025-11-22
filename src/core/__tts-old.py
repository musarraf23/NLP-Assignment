import pyttsx3
from dataclasses import dataclass

@dataclass
class TTS_voices:
    id: str
    name: str

class TTS():
    def __init__(self):
        self._voice_id = None
        self._start_engine()

    def listVoices(self):
        available_voices: list[TTS_voices] = []
        voices = self.engine.getProperty('voices')
        for voice in voices:
            available_voices.append(TTS_voices(id=voice.id, name=voice.name))
        return available_voices

    def setVoice(self, voice: TTS_voices):
        self._voice_id = voice.id

    def _start_engine(self, rate = 200):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', 0.9)
        self.engine.setProperty('voice', "Computer\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech_OneCore\\Voices\\Tokens\\MSTTS_V110_enIN_RaviM")
        # if self._voice_id:
        #     self.engine.setProperty('voice', self._voice_id)


    def speak(self, text: str, rate = 200):
        self._start_engine(rate)
        # print("Computer : ",text)
        self.engine.say(text)
        self.engine.runAndWait()
        del self.engine
