from question_model import Question
from data import question_data

question_bank = []

for question_number in question_data:
    text = question_number["text"]
    answer = question_number["answer"]
    question = Question(text, answer)
    question_bank.append(question)

