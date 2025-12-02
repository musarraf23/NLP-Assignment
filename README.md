# NLP Assignment - Voice-Interactive Escape Room Game

An immersive voice-controlled escape room game where you must solve riddles to escape from an alien ship. The game uses Automatic Speech Recognition (ASR) to understand your answers and Text-to-Speech (TTS) to provide an interactive narrative experience.

## 🎮 Game Overview

You've been captured by aliens who believe you're the brightest mind on Earth. You're trapped aboard their ship, inside a looping chamber with sealed doors. Each door opens only if you crack the code (solve the riddle) behind it. Solve them all to advance and escape. Fail, and the aliens will drop you into a pit of hungry, slimy creatures!

## ✨ Features

- **Voice Recognition**: Answer riddles using your voice with Google Speech Recognition
- **Text-to-Speech**: Immersive narration using Piper TTS with natural-sounding voices
- **Sound Effects**: Atmospheric audio cues for door openings, errors, sirens, and more
- **Interactive Gameplay**: Real-time voice interaction with the game
- **Multiple Riddles**: Challenge yourself with various brain teasers

## 🧭 Game Flow Preview

The high-level flow of the game and code execution is shown below:

![Game Flow Diagram](assets/images/flowchart.png)

## 📋 Requirements

- Python 3.10 or higher
- Microphone (for voice input)
- Audio output device (speakers/headphones)
- Internet connection (for Google Speech Recognition API)

## 🚀 Installation

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd NLP-Assignment
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies** using `uv` (recommended) or `pip`:
   ```bash
   # Using uv (if you have it installed)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

4. **Verify installation**:
   ```bash
   python scripts/env_check.py
   ```

## 🎯 Usage

Run the game with:

```bash
python src/main.py
```

### How to Play

1. The game will start and play an opening sound
2. Listen to each riddle carefully as it's read aloud
3. When you hear the "listen" sound effect, speak your answer clearly into your microphone
4. If correct, the door opens and you proceed to the next riddle
5. If incorrect, the aliens catch you and the game ends
6. Solve all riddles to escape the alien ship!

### Example Riddles

- "What comes once in a minute, twice in a moment, but never in a thousand?" (Answer: "m")
- "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?" (Answer: "map")
- "I have branches, but no fruit, trunk, or leaves. What am I?" (Answer: "bank")
- "I have a neck but no head. I have two arms but no hands. What am I?" (Answer: "shirt")

## 📁 Project Structure

```
NLP-Assignment/
├── assets/
│   ├── sfx/              # Sound effects (door_open, error, siren, etc.)
│   └── voices/           # TTS voice models (Piper ONNX format)
├── scripts/
│   └── env_check.py      # Environment verification script
├── src/
│   ├── config.py         # Game configuration (questions, dialogues)
│   ├── Game.py           # Main game logic
│   ├── main.py           # Entry point
│   └── core/
│       ├── asr.py        # Automatic Speech Recognition module
│       ├── tts.py        # Text-to-Speech module
│       └── WavPlayer.py  # Audio playback utility
├── pyproject.toml        # Project dependencies and metadata
└── README.md            # This file
```

## 🔧 Dependencies

- **piper-tts** (>=1.3.0): High-quality neural text-to-speech synthesis
- **pyaudio** (>=0.2.14): Audio I/O library for microphone input and audio playback
- **soundfile** (>=0.13.1): Audio file reading/writing
- **speechrecognition** (>=3.14.4): Speech recognition library (uses Google Speech Recognition API)

## 🎨 How It Works

1. **ASR (Automatic Speech Recognition)**: 
   - Captures audio from your microphone using PyAudio
   - Converts speech to text using Google's Speech Recognition API
   - Returns the transcribed text or an error if recognition fails

2. **TTS (Text-to-Speech)**: 
   - Uses Piper TTS with ONNX models for high-quality speech synthesis
   - Converts game text to speech with configurable speech rate
   - Plays audio through your default audio output device

3. **Answer Matching**: 
   - Uses token-based matching algorithm
   - Checks if any tokens in your spoken answer match tokens in the correct answers
   - Accepts answers even if only one token matches (flexible matching)

4. **Game Loop**: 
   - Progressively presents riddles from the configuration
   - Validates answers in real-time
   - Manages game state and progression
   - Plays appropriate sound effects for each game event

## 🛠️ Configuration

You can customize the game by editing `src/config.py`:

- **Questions**: Add or modify riddles and their answers in the `questions` list
- **Dialogues**: Customize wake-up messages, correct/incorrect responses, and error messages in the `Dialogues` class
- **Wake-up Word**: Change the wake-up word in `Game.py` (currently set to "iris", but wake-up functionality is commented out)

### Adding New Riddles

To add a new riddle, edit `src/config.py` and add a new `Question` object:

```python
Question(
    question="Your riddle here?",
    answers=["answer1", "answer2"]  # Multiple acceptable answers
)
```

## 📝 Notes

- Make sure your microphone is working and has proper permissions
- Speak clearly and wait for the "listen" sound before answering
- The game uses Google Speech Recognition, which requires an internet connection
- Audio output will play through your default audio device
- The wake-up word feature is currently commented out in the code

## 🐛 Troubleshooting

### Microphone Issues
- **Microphone not working**: Check your system's microphone permissions and ensure the device is properly connected
- **Permission denied**: Grant microphone access in your system settings (macOS: System Preferences > Security & Privacy > Microphone)

### Audio Issues
- **No audio output**: Verify your audio device is working and check system volume settings
- **Sound effects not playing**: Ensure the `assets/sfx/` directory contains all required `.wav` files

### Recognition Issues
- **Recognition errors**: Ensure you have a stable internet connection (required for Google Speech Recognition)
- **Can't understand my answer**: Speak clearly and ensure your microphone is close enough. The matching algorithm is flexible, so partial matches are accepted

### Installation Issues
- **Import errors**: Make sure all dependencies are installed correctly using `pip install -e .`
- **PyAudio installation fails**: On macOS, you may need to install portaudio first: `brew install portaudio`
- **Virtual environment**: Make sure you're running in a virtual environment (check with `python scripts/env_check.py`)

## 🔍 Technical Details

- **Speech Recognition**: Uses Google's Speech Recognition API (requires internet)
- **TTS Engine**: Piper TTS with ONNX models for offline synthesis
- **Audio Processing**: PyAudio for real-time audio I/O
- **Answer Matching**: Token-based fuzzy matching for flexible answer validation

## 📄 License

This project is part of an NLP assignment.

---

**Enjoy escaping the alien ship!** 🚀👽

