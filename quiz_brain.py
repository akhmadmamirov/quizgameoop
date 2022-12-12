class Quizbrain:
    def __init__(self,qs_list):
        self.qsnum = 0
        self.qslist = qs_list
        self.score = 0

    def still_has_qs(self):
        return self.qsnum < len(self.qslist)
           

    def next_question(self):
        current_qs = self.qslist[self.qsnum]
        self.qsnum += 1
        user_answer = input(f"Q.{self.qsnum} : {current_qs.text} (True/False): ")
        self.check_answer(user_answer, current_qs.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('Wrong answer')
        print(f"The Correct answer was {correct_answer}")
        print(f'Your current score is {self.score}/{self.qsnum}')
        print("\n")
 