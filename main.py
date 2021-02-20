import tkinter
import flashcard

BACKGROUND_COLOR = "#B1DDC6"
FONT_ITALIC = font = ("Ariel", 40, "italic")
FONT_BOLD = font = ("Ariel", 40, "bold")

FLASH_TIME = 3 * 1000
current_timer = None
########################################################################################################################
#
#   functions
#
########################################################################################################################
def show_front(title, word):
    canvas.itemconfig(card_title, text=title, fill="black")
    canvas.itemconfig(card_text, text=word, fill="black")
    canvas.itemconfig(card_background, image=card_front_image)


def show_back(title, word):
    canvas.itemconfig(card_title, text=title, fill="white")
    canvas.itemconfig(card_text, text=word, fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def flip(title, word):
    global current_timer
    if current_timer is not None:
        window.after_cancel(current_timer)
    current_timer = window.after(FLASH_TIME, show_back, title, word)


def next_card():
    card = flashcard.next_card()
    print(card)
    show_front(flashcard.FR, card[flashcard.FR])
    flip(flashcard.EN, card[flashcard.EN])


def known():
    next_card()


def unknown():
    next_card()


########################################################################################################################
#
#   window
#
########################################################################################################################
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
########################################################################################################################
#
#   canvas
#
########################################################################################################################
canvas = tkinter.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
#   cards
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
#   texts
card_title = canvas.create_text(400, 150, fill="black", font=FONT_ITALIC)
card_text = canvas.create_text(400, 263, fill="black", font=FONT_BOLD)
#
canvas.grid(row=0, column=0, columnspan=2)
########################################################################################################################
#
#   buttons
#
########################################################################################################################
unknown_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=unknown_image, highlightthickness=0, command=unknown)
unknown_button.grid(row=1, column=0)
#
known_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=known_image, highlightthickness=0, command=known)
known_button.grid(row=1, column=1)

next_card()
########################################################################################################################
#
#   MAIN LOOP
#
########################################################################################################################
window.mainloop()
