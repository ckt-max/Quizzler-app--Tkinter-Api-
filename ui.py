THEME_COLOR = "#375362"
from tkinter import *


class tkwindow:
    def __init__(self, q):
        self.quiz = q
        self.window = Tk()
        self.window.title('self.quizzler')
        self.window.minsize(3*150, 4*150)
        self.window.maxsize(3*150, 4*150)
        self.window.config(bg= "#375362", padx=25, pady=25)
    
        # score Label
        self.score = Label(text='Score: 0/0', bg=THEME_COLOR, fg='#FFFFFF', font=('Raleway', 15, 'bold'))
        self.score.config(pady=25)
        self.score.grid(row=0, column=1, columnspan=1)
    
    
        # canvas
        self.can = Canvas(width=400, height=300)
        self.can.grid(row=1, column=0, columnspan=2)
        self.can_txt = self.can.create_text(200 ,150,text='Press tick for True. Press cross for False. '
                                                          'Press any of them to begin the game',
                                            font=("Lato", 16, 'italic'), width=350)
    
        # Label
        empty = Label(bg=THEME_COLOR)
        empty.config(pady=25)
        empty.grid(row=2, column=1, columnspan=1)

    
        # buttons
        right_img = PhotoImage(file=r'.\images\true.png')
        self.right_button = Button(image=right_img, highlightthickness=0, height=97, width=97, command=self.update_tick)
        self.right_button.config(pady=50, padx=25)
        self.right_button.grid(row=3, column=0)

        wrong_img = PhotoImage(file=r'.\images\false.png')
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, height=97, width=97, command=self.update_cross)
        # self.wrong_button.config(pady=50)
        self.wrong_button.grid(row=3, column=1)

    
        self.window.mainloop()

    def update_tick(self):
        ans = 'true'

        if(self.quiz.current_question == None):
            self.change_ques_on_screen()

        else:
            # blinks the light to green or red if the answer is right or wrong accordingly
            if self.quiz.check_answer(ans) is True:
                self.can.config(background='green')
                self.quiz.score += 1
                self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

            else:
                self.can.config(background='red')
                self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

            self.can.after(1000, lambda: self.can.config(bg='white'))
            if self.quiz.still_has_questions():
                self.change_ques_on_screen()

            else:
                self.endgame()

    def update_cross(self):
        ans = 'false'

        if(self.quiz.current_question == None):
            self.change_ques_on_screen()

        else:
            # blinks the light to green or red if the answer is right or wrong accordingly
            if self.quiz.check_answer(ans) is True:
                self.can.config(background='green')
                self.quiz.score += 1
                self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

            else:
                self.can.config(background='red')
                self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

            self.can.after(1000, lambda: self.can.config(bg='white'))
            if self.quiz.still_has_questions():
                self.change_ques_on_screen()

            else:
                self.endgame()


    # function to get to the next ques
    def change_ques_on_screen(self):
        self.quiz.next_question()
        self.can.itemconfig(self.can_txt, text=self.quiz.current_question.text)

    # function to show final msg at the end of the game
    def endgame(self):
        self.can.itemconfig(self.can_txt, text=f"Your final score is: {self.quiz.score}/{self.quiz.question_number}"
                                               + '\n' + "Thanks for playing")
        # removes the buttons at the end of the game
        self.right_button.destroy()
        self.wrong_button.destroy()






