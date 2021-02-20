import tkinter

BACKGROUND_COLOR = "#B1DDC6"


########################################################################################################################
#
#   functions
#
########################################################################################################################
def right():
    print("right")
    pass


def wrong():
    print("wrong")
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
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 250, image=card_front)
language_text = canvas.create_text(400, 150, text="Language", fill="black", font=("Ariel", 40, "italic"))
term_text = canvas.create_text(400, 263, text="Term", fill="black", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
########################################################################################################################
#
#   buttons
#
########################################################################################################################
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=right)
wrong_button.grid(row=1, column=0)
#
right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

########################################################################################################################
#
#   MAIN LOOP
#
########################################################################################################################
window.mainloop()
