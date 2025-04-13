import matplotlib.pyplot as plt
from tkinter import font as tkfont
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import seaborn as sns
import pandas as pd
import numpy as np
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Functions
def plot_fun(xin=6.4,yin=4.8):
  plt.figure(figsize=(9,6)) 
  path = r'C:\\Users\\Sarvamm\\Jupyter\\'+ theme_choice.get() + '.mplstyle'
  plot = plot_choice.get()          
  plt.style.use(path)
  plt.title(title_entry.get()); 
  xaxis = col1.get(); yaxis=col2.get();    
  match plot:
      case 'line-plot':
        sns.lineplot(x=xaxis,y=yaxis, data=df)
      case 'hist-plot':
        sns.histplot(x=xaxis,y=yaxis, data=df)
      case 'scatter-plot':
        sns.scatterplot(x=xaxis,y=yaxis, data=df, s=10)
      case 'reg-plot':
        sns.regplot(x=xaxis,y=yaxis, data=df, scatter_kws={'s': 5}) 
      case 'heatmap':
          corr = df.select_dtypes(['number']).corr() 
          sns.heatmap( corr , annot=True )
      case 'box-plot':
         sns.boxplot(x=xaxis, y=yaxis, data=df)
      case 'kde-plot':
        sns.kdeplot(x=xaxis, y=yaxis, data=df)

def on_submit():
     delete_fun(frame2)
     plot_fun()

     plt.savefig('plot.png')
     image = Image.open('plot.png')
     photo = ImageTk.PhotoImage(image)
     label = tk.Label(frame2, image=photo)
     label.image = photo  

     label.grid(rowspan=2, column=0, padx=5, pady=5)
     save_button.grid(row=12, columnspan=2, padx=5, pady=15)
     delete_button.grid(row=13, columnspan=2, padx=5, pady=0)
     plt.close()

def delete_cols():
  col1_label.destroy(); col2_label.destroy()
  col1_dropdown.destroy(); col2_dropdown.destroy();

def open_file():
    global df, col1, col2, ndf, col1_label,col2_label, col1_dropdown, col2_dropdown
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    file_title = file_path[(len(file_path) - file_path[::-1].index('/')) ::]
    title_entry.delete(0, tk.END)
    title_entry.insert(0, file_title)
    if file_path:
      if frame2:
          delete_fun(frame2)
      try:
        delete_cols()
      except Exception:
        pass
      
      df = pd.read_csv(file_path)
      ndf = df.select_dtypes(include=['number'])
      columns = ndf.columns.tolist()

      col1=tk.StringVar();                                                          
      col2=tk.StringVar()
      col1.set(columns[0]);                                                         
      col2.set(columns[1])
      col1_label = tk.Label(frame1, text='X axis',  font=("Arial", 14));     
      col2_label = tk.Label(frame1, text='Y axis', font=("Arial", 14))  
      col1_dropdown = tk.OptionMenu(frame1, col1, *columns);                       
      col2_dropdown = tk.OptionMenu(frame1, col2, *columns)

      _='Columns found:\n';                        
      for i in ndf.columns.to_list():
        _+=i+'\n';

      colsfound=tk.Label(frame2, text= _,  font=("Arial", 14))
      colsfound.grid(row=1, columnspan=2, padx=50, pady=5)
      title_label.grid(row=2, column=0, padx=10, pady=15);
      title_entry.grid(row=2, column=1, padx=10, pady=15)
      #Drop Downs
      
      plot_dropdown.grid(row=9, column=1, padx=5, pady=5)
      plot_dropdown_label.grid(row=9, column=0, padx=5, pady=5)
      plot_button.grid(row=10, columnspan=2, padx=5, pady=15)
      col1_label.grid(row=3, column=0, padx=5, pady=5);                          
      col1_dropdown.grid(row=3, column=1, padx=5, pady=5);                       
      col2_label.grid(row=4, column=0, padx=5, pady=5)
      col2_dropdown.grid(row=4, column=1, padx=5, pady=5)
        
def save_fun():
     delete_fun(frame2)
     file_path = filedialog.asksaveasfilename(defaultextension=".png")
     plot_fun(10,10)
     plt.savefig(file_path)
     plt.close()
def delete_fun(frame):
     for widget in frame.winfo_children():
         widget.destroy()
def bigo():
    delete_fun(frame2)
    path = r'C:\\Users\\Sarvamm\\Jupyter\\'+ theme_choice.get() + '.mplstyle'
    plt.style.use(path)
    n = np.linspace(1, 50, 50)

    BigO = { 'O(1)': np.ones_like(n), 
        'O(log n)': np.log(n), 
        'O(n)': n,
        'O(n log n)': n * np.log(n),
        'O(n^2)': n**2,
        'O(2^n)': 2**n }

    plt.figure(figsize=(9, 6))
    for key, value in BigO.items():
        plt.plot(n, BigO[key], label=key)

    plt.ylim(0, 200)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Operations')
    plt.title('Big O Time Complexities')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot.png')
    image = Image.open('plot.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(frame2, image=photo)
    label.image = photo
    label.grid(rowspan=2, column=0, padx=5, pady=5)
    save_button.grid(row=12, columnspan=2, padx=5, pady=5)
    delete_button.grid(row=13, columnspan=2, padx=5, pady=15)
    plt.close()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
window = tk.Tk()
window.title("Basic Python GUI Plotting by Sarvamm")
window.geometry("1400x650")

custom_font = tkfont.Font(size=13)

#Left Frame                                                     
frame1 = tk.Frame(window, padx=10, pady=10);   
#RightFrame                
frame2 = tk.Frame(window, padx=10, pady=10);

#Buttons
open_button = tk.Button(frame1, text="Open File", command=open_file, width=12, height=1, font=custom_font)
plot_button = tk.Button(frame1, text="Plot", command=on_submit, width=12, height=1,  font=custom_font)
save_button = tk.Button(frame1, text="Save", command=save_fun, width=12, height=1, font=custom_font,fg='#c4a7e7')
delete_button = tk.Button(frame1, text="Delete", command=lambda: delete_fun(frame2), width=12, height=1, font=custom_font, fg='#eb6f92')
bigo_button = tk.Button(frame1, text="Plot Big O", command=bigo, width=12, height=1, font=custom_font)

#Entry
title_label = tk.Label(frame1, text="Title:", font=("Arial", 14));   
title_entry = tk.Entry(frame1, width=30, font=custom_font)

#Dropdowns
theme_choice = tk.StringVar()
theme_choice.set("rose-pine")  # Set the default value
theme_options = ["rose-pine", "rose-pine-moon", "rose-pine-dawn" ,"pitayasmoothie-dark", "pitayasmoothie-light"]
theme_dropdown_label = tk.Label(frame1, text="Theme chosen:", font=("Arial", 10))
theme_dropdown = tk.OptionMenu(frame1, theme_choice, *theme_options)

plot_choice = tk.StringVar()
plot_choice.set("heatmap")  # Set the default value
plot_options = ['heatmap', "line-plot", "hist-plot", "scatter-plot" ,"reg-plot", 'kde-plot','box-plot']
plot_dropdown_label = tk.Label(frame1, text="Plot kind:", font=("Arial", 10))
plot_dropdown = tk.OptionMenu(frame1, plot_choice, *plot_options)
                   
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Placement
def pack_default():
  frame1.grid(row=0, column=0, padx=10, pady=0);
  frame2.grid(row=0, column=1, padx=10, pady=0)
  theme_dropdown_label.grid(row=8, column=0, padx=5, pady=5)
  theme_dropdown.grid(row=8, column=1, padx=5, pady=5)
  open_button.grid(row=0, columnspan=4, padx=5, pady=15)
  bigo_button.grid(row=14, columnspan=2, padx=5, pady=30)
pack_default()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
window.mainloop()