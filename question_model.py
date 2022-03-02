class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def getAnswers(self):
        return self.answer

    def getText(self):
        return self.text