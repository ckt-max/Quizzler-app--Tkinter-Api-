from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from tkinter import *
from ui import tkwindow
import json

# -------------------UI-----------------------------
question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank) # creates self.quiz by taking the list of questions

quiz_ui = tkwindow(quiz)



