import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
WHITE = "#FFFAFA"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

timer = None

start_pressed = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_marks["text"] = ""
    global reps
    reps = 0
    global start_pressed
    start_pressed = False


# ---------------------------- TIMER MECHANISM -------------------------------#
def press_start():
    global start_pressed
    if not start_pressed:
        start_pressed = True
        start_timer()
    else:
        pass


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 2 != 0:
        label.config(text="Work", fg=GREEN)
        countdown(work_sec)
    elif reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    else:
        label.config(text="Short Break", fg=PINK)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ---------------------------#
def countdown(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2

        for _ in range(work_sessions):
            marks += "✔"
        check_marks["text"] = marks

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato and clock
canvas = tk.Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image((100, 112), image=tomato_image)
timer_text = canvas.create_text(
                (100, 130), text="00:00", fill="white",
                font=(FONT_NAME, 35, "bold")
                )
canvas.grid(row=1, column=1)

# Labels
label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

check_marks = tk.Label(text="", font=(FONT_NAME, 32), bg=YELLOW, fg=GREEN)
check_marks.grid(row=4, column=1)

# Buttons
start_button = tk.Button(
                text="start", font=(FONT_NAME), bg=WHITE, fg=BLACK,
                activebackground=RED, highlightthickness=0, command=press_start
                )
start_button.grid(row=2, column=0)

reset_button = tk.Button(
                text="reset", font=(FONT_NAME), bg=WHITE, fg=BLACK,
                activebackground=RED, highlightthickness=0, command=reset_timer
                )
reset_button.grid(row=2, column=2)

window.mainloop()
