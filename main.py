from question_model import Question
from data import question_data
import random as r
from quiz_brain import Brain

q = question_data
brain = Brain()
broj_pitanja = len(q)
while True:
    number = r.randint(0,len(q)-1)
    question = Question(q[number]["text"], q[number]["answer"])
    brain.nextQuestion()
    print(f"Q_{brain.questionNumber()}:{question.getText()}")
    odgovor = input("Unesite vaš odgovor (True/False): ")

    if odgovor == question.getAnswers():
        brain.correctAnswer()
        brain.currentResult()
        

    elif odgovor != question.getAnswers():
        print("Odgovor netačan")
        brain.currentResult()

    
    q.pop(number)
    
    
    
    if len(q) == 0:
        print("Kviz se završava, osvojili ste: ")
        print(f" Osvojili ste: {brain.getPoints()}/{broj_pitanja}")
        break
    
    
