import tkinter as tk
from PIL import ImageTk

# initialize app
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg="#3d6466")
frame1.grid(row=0, column=0)

# frame1 widgets
ImageTk.PhotoImage(file="assets/RRecipe_logo.png")

# run app
root.mainloop()