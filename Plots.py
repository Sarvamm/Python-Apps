import matplotlib.pyplot as plt
from tkinter import font as tkfont
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
window = tk.Tk()
window.title("plot")
window.geometry("700x750")

custom_font = tkfont.Font(size=14)

frame1 = tk.Frame(window, padx=10, pady=10)
frame1.pack(padx=10, pady=4)
frame2 = tk.Frame(window, padx=10, pady=10)
frame2.pack(padx=10, pady=4)

#input
labelx = tk.Label(frame1, text="Enter a list of X", font=("Arial", 14)) 
labelx.grid(row=0, column=0, padx=5, pady=5)
xinput = tk.Entry(frame1, width=30, font=custom_font)
xinput.grid(row=0, column=1, padx=5, pady=5)

labely = tk.Label(frame1, text="Enter a list of Y", font=("Arial", 14)) 
labely.grid(row=1, column=0, padx=5, pady=5)
yinput = tk.Entry(frame1, width=30, font=custom_font)
yinput.grid(row=1, column=1, padx=5, pady=5)

title = tk.Label(frame1, text="Title:", font=("Arial", 14)) 
title.grid(row=2, column=0, padx=5, pady=5)
title_entry = tk.Entry(frame1, width=30, font=custom_font)
title_entry.grid(row=2, column=1, padx=5, pady=5)

xaxis = tk.Label(frame1, text="x label:", font=("Arial", 14)) 
xaxis.grid(row=3, column=0, padx=5, pady=5)
xaxis_entry = tk.Entry(frame1, width=30, font=custom_font)
xaxis_entry.grid(row=3, column=1, padx=5, pady=5)

yaxis = tk.Label(frame1, text="y label:", font=("Arial", 14)) 
yaxis.grid(row=4, column=0, padx=5, pady=5)
yaxis_entry = tk.Entry(frame1, width=30, font=custom_font)
yaxis_entry.grid(row=4, column=1, padx=5, pady=5)

theme_choice = tk.StringVar()
theme_choice.set("rose-pine")  # Set the default value
options = ["rose-pine", "rose-pine-moon", "rose-pine-dawn" , 
           "pitayasmoothie-dark", "pitayasmoothie-light"]

dropdown_label = tk.Label(frame1, text="select a theme", font=("Arial", 14))
dropdown_label.grid(row=0, column=2, padx=5, pady=5)
dropdown = tk.OptionMenu(frame1, theme_choice, *options)
dropdown.grid(row=1, column=2, padx=5, pady=5)


def on_submit():
     delete_fun()
     path = r'C:\\Users\\Sarvamm\\Jupyter\\'+ theme_choice.get() + '.mplstyle'
     input1 = eval(xinput.get()); input2 = eval(yinput.get())
     plt.style.use(path)
     plt.plot(input1, input2)
     plt.title(title_entry.get()); plt.xlabel(xaxis_entry.get()); plt.ylabel(yaxis_entry.get()); 
     plt.savefig('plot.png')
     plt.close()
     image = Image.open('plot.png')
     photo = ImageTk.PhotoImage(image)
     label = tk.Label(frame2, image=photo)
     label.image = photo  
     label.grid(row=0, column=0, padx=5, pady=5)
     save_button.grid(row=3, column=2, padx=5, pady=5)
     delete_button.grid(row=4, column=2, padx=5, pady=15)

def save_fun():
     file_path = filedialog.asksaveasfilename(defaultextension=".png")
     input1 = eval(xinput.get()); input2 = eval(yinput.get())
     plt.figure(figsize=(10,10))
     plt.plot(input1, input2)
     plt.title(title_entry.get()); plt.xlabel(xaxis_entry.get()); plt.ylabel(yaxis_entry.get()); 
     plt.savefig(file_path)
     plt.close()
def delete_fun():
     for widget in frame2.winfo_children():
         widget.destroy()

submit_button = tk.Button(frame1, text="Plot", command=on_submit, width=10, height=1, font=custom_font)
submit_button.grid(row=5, columnspan=2, padx=5, pady=5)

save_button = tk.Button(frame1, text="Save", command=save_fun, width=10, height=1, font=custom_font)
delete_button = tk.Button(frame1, text="Delete", command=delete_fun, width=10, height=1, font=custom_font)


window.mainloop()
     
