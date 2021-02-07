import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flash me")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    raw_data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    raw_data = pd.read_csv("data/french_words.csv")
finally:
    data = raw_data.to_dict(orient="records")


# NEW RANDOM CARD
def select_new_word():
    global word_dict, fliptimer
    window.after_cancel(fliptimer)
    word_dict = random.choice(data)
    flashcard.itemconfig(current_card, image=card_front)
    flashcard.itemconfig(title_text, text="French", fill="black")
    flashcard.itemconfig(word_text, text=word_dict["French"], fill="black")
    window.after(3000, english_definitions)

def english_definitions():
    flashcard.itemconfig(current_card, image=card_back)
    flashcard.itemconfig(title_text, text="English", fill="white")
    flashcard.itemconfig(word_text, text=word_dict["English"], fill="white")


def known():
    data.remove(word_dict)
    current_data = pd.DataFrame(data)
    current_data.to_csv("data/to_learn.csv", index=False)
    select_new_word()

fliptimer = window.after(3000, english_definitions)
window.after_cancel(fliptimer)

# FLASHCARDS
flashcard = tk.Canvas(
    width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR
)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
current_card = flashcard.create_image((400, 273), image=card_front)
flashcard.grid(row=0, column=0, columnspan=2)

# FLASHCARD TEXT

title_text = flashcard.create_text((400, 150), text="Title", font=("Arial", 40, "italic"))

word_text = flashcard.create_text((400, 268), text="Word", font=("Arial", 60, "bold"))


# BUTTONS
right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")
yes_button = tk.Button(image=right_img, highlightthickness=0, command=known)
no_button = tk.Button(image=wrong_img, highlightthickness=0, command=select_new_word)

yes_button.grid(row=1, column=1)
no_button.grid(row=1, column=0)

select_new_word()

window.mainloop()
