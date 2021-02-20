import tkinter

BACKGROUND_COLOR = "#B1DDC6"
FONT_ITALIC = font=("Ariel", 40, "italic")
FONT_BOLD = font=("Ariel", 40, "bold")


########################################################################################################################
#
#   functions
#
########################################################################################################################
def known():
    print("known")
    pass


def unknown():
    print("unknown")
    pass


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
language_text = canvas.create_text(400, 150, text="Language", fill="black", font=FONT_ITALIC)
term_text = canvas.create_text(400, 263, text="Term", fill="black", font=FONT_BOLD)
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

########################################################################################################################
#
#   MAIN LOOP
#
########################################################################################################################
window.mainloop()
