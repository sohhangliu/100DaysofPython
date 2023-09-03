from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question_number in question_data:
    text = question_number["text"]
    answer = question_number["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.stillhasquestions():
    quiz.nextquestion()