import tkinter as tk
from turtle import bgcolor
from PIL import ImageTk

bg_color = "#3d6466"

def load_frame1():
    frame1.pack_propagate(False)
    # logo widget
    logo_img = ImageTk.PhotoImage(file="assets\RRecipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    # instructions widget
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
            command=lambda:load_frame2()
            ).pack(pady=20)

def load_frame2():
    print("Hello")

# initialize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)
for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

# run app
root.mainloop()