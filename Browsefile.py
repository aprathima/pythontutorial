# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 09:47:40 2023

@author: Charishma
"""

import pandas as pd
import tkinter  as tk 
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

my_w = tk.Tk()
my_w.geometry("500x350")  # Size of the window 
my_w.title('Prathima Browse File App')

my_font1=('times', 12, 'bold')
lb1 = tk.Label(my_w,text='Read File & create DataFrame',
    width=30,font=my_font1)  
lb1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Browse File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,pady=5) 
lb2=tk.Label(my_w,width=40,text='',bg='lightyellow')
lb2.grid(row=3,column=1,padx=5)
l1=[] # List to hold headers of the Treeview 
def upload_file():
    global df ,l1
    f_types = [('CSV files',"*.csv"),('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    lb1.config(text=file) # display the path 
    df=pd.read_csv(file) # create DataFrame
    l1=list(df) # List of column names as header 
    str1="Rows:" + str(df.shape[0])+ " , Columns:"+str(df.shape[1])
    #print(str1)
    lb2.config(text=str1) # add to Text widget
    trv_refresh() # show Treeview 
	
def trv_refresh(): # Refresh the Treeview to reflect changes
    global df,trv,l1 
    r_set=df.to_numpy().tolist() # create list of list using rows
    trv=ttk.Treeview(my_w,selectmode='browse',height=10,
        show='headings',columns=l1)
    trv.grid(row=4,column=1,columnspan=3,padx=10,pady=20)
    
    for i in l1:
        trv.column(i,width=90,anchor='c')
        trv.heading(i,text=str(i))
    for dt in r_set:
        v=[r for r in dt]
        trv.insert("",'end',iid=v[0],values=v)
my_w.mainloop()  # Keep the window open
