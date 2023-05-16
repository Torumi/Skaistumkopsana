import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Skaistumkopsana")
window.geometry('1920x1080')


new_client_frame = ttk.Frame(borderwidth=1, relief='solid', padding=[10,10])
name_label = tk.Label(new_client_frame, text='Name')
name_entry = ttk.Entry(new_client_frame)
surname_label = tk.Label(new_client_frame, text='Surname')
surname_entry = ttk.Entry(new_client_frame)

name_label.pack(anchor="nw")
name_entry.pack(anchor='nw')
surname_label.pack(anchor="nw")
surname_entry.pack(anchor='nw')

new_client_frame.pack(anchor='nw')



window.mainloop()