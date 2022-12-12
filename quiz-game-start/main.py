from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    qs = Question(question_text,question_answer)
    question_bank.append(qs)

quiz = Quizbrain(question_bank)

while quiz.still_has_qs():
    quiz.next_question()

print('You have completed the quiz!')
print(f'Your final score was {quiz.score}/{quiz.qsnum}')