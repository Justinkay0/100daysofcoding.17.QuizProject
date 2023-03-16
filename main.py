from data import question_data
from question_model import Question


question_bank = []
for qn in question_data:
    question_bank.append((Question(qn['text'], qn['answer'])))

print(question_bank[0].text)