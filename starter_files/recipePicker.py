import tkinter as tk
from turtle import bgcolor
from PIL import ImageTk

bg_color = "#3d6466"

def load_frame2():
    pass

# initialize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="assets\RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(frame1,
         text="ready for your random recipe?",
         bg=bg_color,
         fg="white",
         font=("TkMenuFont", 14)
         ).pack()

# button widget
tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28392a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=load_frame2()
        ).pack()

# run app
root.mainloop()