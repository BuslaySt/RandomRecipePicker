import tkinter as tk
from turtle import bgcolor
from PIL import ImageTk

bg_color = "#3d6466"

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

# run app
root.mainloop()