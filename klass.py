import tkinter as tk

root = tk.Tk()
text = tk.Text(root)
text.pack()

# Inserting text at the end of the Text widget
text.insert(tk.END, "Hello, World!")
