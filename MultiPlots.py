import matplotlib.pyplot as plt
from tkinter import font as tkfont
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import seaborn as sns
import pandas as pd

window = tk.Tk()
window.title("plot")
window.geometry("1400x600")

custom_font = tkfont.Font(size=14)

frame1 = tk.Frame(window, padx=10, pady=10)
frame1.grid(row=0, column=0, padx=10, pady=20)
frame2 = tk.Frame(window, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=20)

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
theme_options = ["rose-pine", "rose-pine-moon", "rose-pine-dawn" , 
           "pitayasmoothie-dark", "pitayasmoothie-light"]
plot_choice = tk.StringVar()
plot_choice.set("line-plot")  # Set the default value
plot_options = ["line-plot", "hist-plot", "scatter-plot" , 
           "reg-plot", 'lmplot']

theme_dropdown_label = tk.Label(frame1, text="select a theme", font=("Arial", 14))
theme_dropdown_label.grid(row=0, column=2, padx=5, pady=5)
theme_dropdown = tk.OptionMenu(frame1, theme_choice, *theme_options)
theme_dropdown.grid(row=1, column=2, padx=5, pady=5)

plot_dropdown = tk.OptionMenu(frame1, plot_choice, *plot_options)
plot_dropdown.grid(row=5, columnspan=2, padx=5, pady=5)


def on_submit():
     delete_fun()
     path = r'C:\\Users\\Sarvamm\\Jupyter\\'+ theme_choice.get() + '.mplstyle'
     x_values = eval(xinput.get()); y_values = eval(yinput.get())
     plot = plot_choice.get()
               
     plt.style.use(path)
     plt.title(title_entry.get()); plt.xlabel(xaxis_entry.get()); plt.ylabel(yaxis_entry.get()); 
     df = pd.DataFrame({ 'x': x_values, 'y': y_values })
     match plot:
          case 'line-plot':
            sns.lineplot(x='x',y='y', data=df)
          case 'hist-plot':
            sns.histplot(x='x',y='y', data=df)
          case 'scatter-plot':
            sns.scatterplot(x='x',y='y', data=df)
          case 'reg-plot':
            sns.regplot(x='x',y='y', data=df)
          case 'lmplot':
            sns.lmplot(x='x',y='y', data=df)   

     plt.savefig('plot.png')
     image = Image.open('plot.png')
     photo = ImageTk.PhotoImage(image)
     label = tk.Label(frame2, image=photo)
     label.image = photo  
     label.grid(row=0, column=0, padx=5, pady=5)
     save_button.grid(row=3, column=2, padx=5, pady=5)
     delete_button.grid(row=4, column=2, padx=5, pady=15)
     plt.close()

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
submit_button.grid(row=6, columnspan=2, padx=5, pady=0)

save_button = tk.Button(frame1, text="Save", command=save_fun, width=10, height=1, font=custom_font)
delete_button = tk.Button(frame1, text="Delete", command=delete_fun, width=10, height=1, font=custom_font)


window.mainloop()
     
