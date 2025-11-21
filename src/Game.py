from dataclasses import dataclass
import config
@dataclass
class Question():
    question: str
    answer: str

class Game():
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.index = 0
    
    def get_intro_text(self):
        return f"You've been captured by aliens who believe you're the smartest person on Earth, and now you're trapped aboard their spaceship. To escape, you must crack a series of codes. You're confined in a recursive room with {len(self.questions)} doors, and each door will only open if you solve its code. Succeed, and you move on to the next room; fail, and the aliens will toss you into a pit of hungry, slimy creatures."

    def is_running(self):
        return self.index < len(self.questions)
    
    def next(self):
        self.index += 1

    def get_question(self):
        return self.questions[self.index].question

    def get_answer(self):
        return self.questions[self.index].question

    def match_answer(self, user_answer: str):
        toks = user_answer.lower().split(' ')
        actual_answer = self.get_answer().lower()
        score = 0
        for tok in toks:
            if tok in actual_answer:
                score += 1
        return score != 0 # even if 1 token in answer match then we accept


    def step(self):
        pass
