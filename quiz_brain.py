class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        print(f"Q{self.question_number + 1}. {self.question_list[self.question_number].text} ")
        user_input = input("True or False \n").lower()
        self.check_answer(user_input, self.question_list[self.question_number].answer)
        print(f"Your current score is {self.score}/{self.question_number + 1}")
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the correct answer!!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer} \n")
