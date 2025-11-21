import pyttsx3
from dataclasses import dataclass
from collections.abc import MutableSequence

@dataclass
class TTS_voices:
    id: str
    name: str

class TTS():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('volume', 0.9)

    def listVoices(self):
        available_voices: list[TTS_voices] = []
        voices = self.engine.getProperty('voices')
        for voice in voices:
            available_voices.append(TTS_voices(id=voice.id, name=voice.name))
        return available_voices

    def setVoice(self, voice: TTS_voices):
        self.engine.setProperty('voice', voice.id)


    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
