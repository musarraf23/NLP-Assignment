from dataclasses import dataclass 

@dataclass
class Question():
    question: str
    answers: list[str]

@dataclass
class Dialogues:
    wakeup_messages = [
        "Hey there! How can I help you today? Ready to jump into a fun game?",
        "Hi! What's on your mind? Want to dive into a game together?",
        "Hello! I'm here whenever you are. Feel like starting a fun game?",
        "Hey! What can I do for you? Up for a little game?",
        "Hi there! Need a hand with something? How about we kick things off with a game?",
        "Hello! How's your day going so far? Want to brighten it up with a fun game?",
        "Hey, good to see you! What can I help with? Ready to play a game?",
        "Hi! Just let me know what you need. Or—if you're in the mood—we can play a game.",
        "Hello! I'm here and ready to dive in. Shall we begin a fun game?",
        "Hey! How can I make things easier for you today? Maybe with a quick game?"
    ]

    couldnt_catch_messages = [
        "I didn't quite catch that—try again before the aliens get suspicious...",
        "Your voice faded out. Speak clearly, the scanners are watching...",
        "Hmm, that didn't register. Give it another try before the aliens notice...",
        "I couldn't hear you properly. Quick, try again before they track the anomaly...",
        "That was too faint. Repeat your answer—time is running out...",
        "Signal unclear. Say it again before the alien guards pick up the distortion...",
        "I missed that. Try once more, quietly... the walls are listening...",
        "No response detected. Hurry and try again before they grow impatient...",
        "Your words got scrambled. Repeat yourself before the ship's AI flags you...",
        "I couldn't decode that. Try again fast—the aliens are monitoring every sound..."
    ]

    correct_messages = [
        "Correct. The door slides open with a cold metallic hiss...",
        "Well done. The lock disengages and the door glides aside...",
        "Correct answer. You hear gears turning as the door slowly opens...",
        "You nailed it. A sharp hiss echoes as the door releases...",
        "Correct. The alien mechanism hums and the door unlocks...",
        "Nicely done. Lights flicker as the door parts with a metallic sigh...",
        "Correct response. The seal breaks and the door creeps open...",
        "You got it. A soft click followed by a hiss signals the door opening...",
        "Right again. The chamber shifts as the door splits open...",
        "Correct. The machinery awakens and the door unlocks in a shimmering hiss..."
    ]
    
    incorrect_messages = [
        "Incorrect... The aliens notice instantly. Sirens erupt as you're dragged toward the pit of slimy creatures...",
        "Wrong answer. Red lights flash—alien guards seize you and pull you toward the slime-filled abyss...",
        "Incorrect. The ship's alarm howls as the aliens advance, hauling you toward the writhing pit below...",
        "Nope… wrong. The chamber erupts in warning lights as you're taken toward the slimy horrors...",
        "Incorrect. A harsh alarm blares—alien hands grip you, guiding you straight to the creature pit...",
        "Wrong move. The system flags you, and the aliens drag you toward the churning mass of slimy beasts...",
        "Incorrect. The ship roars with alarms as you're escorted to the pit of hungry, dripping creatures...",
        "No luck. The aliens react instantly—alarms scream as you're pulled toward the slime pit...",
        "Incorrect... The floor lights up in warning patterns as aliens drag you to their slimy pets...",
        "Wrong answer. The alarm's wail echoes as you're forced toward the pit crawling with slimy creatures..."
    ]

    victory_messages = [
        "You did it! Every lock cracked, every challenge conquered. You've escaped the alien ship!",
        "Victory! You solved every puzzle and outsmarted the aliens. Freedom is yours!",
        "You made it! Every door opened, every code defeated. The alien ship is now behind you!",
        "Congratulations! You broke through every barrier and slipped away from the aliens' grasp!",
        "You've escaped! Your wits shattered every lock and earned your freedom from the ship!",
        "Well done! Every challenge has fallen before you. The alien ship fades into the distance!",
        "You did it! Your brilliance carried you through each test. You're free from the alien vessel!",
        "Success! You cracked every code and made your daring escape from the ship!",
        "Outstanding! You conquered every challenge and now the alien ship can no longer hold you!",
        "You've triumphed! Each puzzle solved has led you to freedom. You're off the alien ship at last!"
    ]



questions : list[Question] = [
    Question(question="What comes once in a minute, twice in a moment, but never in a thousand", answers=["m"]),
    Question(question=" I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", answers=["map"]),
    Question(question="I have branches, but no fruit, trunk, or leaves. What am I?", answers=["bank"]),
    Question(question="I have a neck but no head. I have two arms but no hands. What am I?", answers=["shirt"]),
]

dialogues = Dialogues()

