from dataclasses import dataclass

@dataclass
class Question():
    question: str
    answer: str



questions : list[Question] = [
    Question(question="How many times can you subtract the number 5 from 35?", answer="seven"),
    Question(question="Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?", answer="yes"), 
    Question(question="The day before two days after the day before tomorrow is Saturday. What day is it today?", answer="friday"),
    Question(question="Susan and Lisa decided to play tennis against each other. They bet $1 on each game they played. Susan won three bets and Lisa won $5. How many games did they play?", answer="eleven"),
]