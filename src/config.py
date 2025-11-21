from dataclasses import dataclass

@dataclass
class Prompts:
    wakeup_messages = [ 
        "Hey there! How can I help you today?",
        "Hi! What's on your mind?",
        "Hello! Ready whenever you are.",
        "Hey! What can I do for you?",
        "Hi there! Need a hand with something?",
        "Hello! How's your day going so far?",
        "Hey, good to see you! What can I help with?",
        "Hi! Just let me know what you need.",
        "Hello! I'm here and ready to dive in.",
        "Hey! How can I make things easier for you today?"
    ]

prompts = Prompts()
