class Brain:
    def __init__(self):
        self.points = 0
        self.questions = 0

    def correctAnswer(self):
        print("Tačan odgovor!")
        self.points += 1


    def getPoints(self):
        return self.points

    def nextQuestion(self):
        self.questions += 1

    def questionNumber(self):
        return self.questions

    def currentResult(self):
        print(f"{self.getPoints()}/{self.questionNumber()}")