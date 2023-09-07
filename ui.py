from functools import partial
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_source: QuizBrain):
        self.quiz = quiz_source
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Placeholder",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=partial(self.check_answer, "True"))
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=partial(self.check_answer, "False"))
        self.false_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_quest = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_quest)
        else:
            self.canvas.itemconfig(self.question_text, text="you've finished this quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.window.after(500, self.get_question())


