import tkinter
import flashcard

BACKGROUND_COLOR = "#B1DDC6"
FONT_ITALIC = font = ("Ariel", 40, "italic")
FONT_BOLD = font = ("Ariel", 40, "bold")


########################################################################################################################
#
#   functions
#
########################################################################################################################
def next_card():
    card = flashcard.next_card()
    print(card)
    canvas.itemconfig(card_title, text=flashcard.FR)
    canvas.itemconfig(card_text, text=card[flashcard.FR])


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
card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front)
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
