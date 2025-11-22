from piper import PiperVoice, SynthesisConfig
import pyaudio

class TTS():
    def __init__(self):
        self.voice = PiperVoice.load("assets/voices/en_GB-semaine-medium.onnx")
    
    def listVoices(self):
        return ['']

    def setVoice(self, voice):
        pass

    def speak(self, text: str, rate = 200):
        syn_config = SynthesisConfig(
            length_scale = 200 / rate,
        )
        p = pyaudio.PyAudio()
        synth = self.voice.synthesize(text, syn_config)
        for syn in synth:
            stream = p.open(format =
                            p.get_format_from_width(syn.sample_width),
                            channels = syn.sample_channels,
                            rate = syn.sample_rate,
                            output = True)
            stream.write(syn.audio_int16_bytes)
        p.terminate()
