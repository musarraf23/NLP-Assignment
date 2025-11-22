import pyaudio
import wave 

class WavPlayer():
    def __init__(self):
        self.chunk = 1024

    def play(self, file_name: str):
        p = pyaudio.PyAudio()
        wf = wave.open(f'assets/sfx/{file_name}.wav', 'rb')
        stream = p.open(format =
                        p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)
        data = wf.readframes(self.chunk)
        while data:
            # Play Sound == write to steam
            stream.write(data)
            data = wf.readframes(self.chunk)

        # cleanup stuff.
        wf.close()
        stream.close()    
        p.terminate()