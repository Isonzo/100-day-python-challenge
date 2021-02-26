import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

DIRTY_WHITE = "#e8e4c9"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg=DIRTY_WHITE, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(height=250, width=300, bg=DIRTY_WHITE)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            (150, 125),
            text="Question goes here, товарищ!",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
            )


        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")

        self.true_button = tk.Button(
            image=true_img, highlightthickness=0,
            command=lambda: self.check_answer("True")
            )
        self.false_button = tk.Button(
            image=false_img, highlightthickness=0,
            command=lambda: self.check_answer("False")
            )

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz. Thanks for Playing!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # def true_pressed(self):
    #     self.quiz.check_answer("True")
    #
    # def false_pressed(self):
    #     self.quiz.check_answer("False")

    def check_answer(self, answer: str):
        is_right = self.quiz.check_answer(answer)
        if is_right:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="green")
            self.window.after(1000, self.normal)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="red")
            self.window.after(1000, self.normal)

    def normal(self):
        self.canvas.config(bg=DIRTY_WHITE)
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.get_next_question()
