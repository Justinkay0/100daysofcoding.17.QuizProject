from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for qn in question_data:
    question_bank.append((Question(qn['text'], qn['answer'])))

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.next_question()

print("\n\nYou have completed the quiz!!")
print(f"Your score was {game.score}/{game.question_number}")
