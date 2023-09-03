from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""
Trivia Quiz

This is a script that tests users of basic trivia questions (True/False0.

Soh Hang Liu
2023/09/02
"""

question_bank = []
1

for question_number in question_data["results"]:
    text = question_number["question"]
    answer = question_number["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.stillhasquestions():
    quiz.nextquestion()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")