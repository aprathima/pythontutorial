# Import Module
from tkinter import *
import pandas as pd
df = pd.read_csv("C:\\prathima\\Automobile_data.csv")
#print("First 30 from the List")
#print(df.head(30))

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to Auto Data App")
# Set geometry (widthxheight)
root.geometry('900x500')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

#adding a label to the root window
lbl = Label(root, text = "Welcome To Automobile world")
lbl.grid(column =0, row =0)

# adding Entry Field
#txt = Entry(root, width=50)
#txt.grid(column =5, row =5)

# function to display text when
# button is clicked
def clicked1():
    res = df.head(5)
    lbl.grid(column =2, row =4)
    lbl.configure(text = res)

# function to display text when
# button is clicked
def clicked2():
    car_Manufacturers = df.groupby('company')
    res = car_Manufacturers.get_group('toyota')
    lbl.grid(column =1, row =9)
    lbl.configure(text = res) 
    
def clicked3():
    res = df [['company','price']][df.price==df['price'].max()]
    lbl.grid(column =0, row =13)
    lbl.configure(text = res) 
   
def clicked4():
        res = df['company'].value_counts()
        lbl.grid(column =0,row = 9)
        lbl.configure(text=res)
        
def clicked5():
    car_Manufacturers = df.groupby('company')
    res = car_Manufacturers['company','price'].max() 
    lbl.grid(column =0,row= 9) 
    lbl.configure(text=res)
def clicked6():
    car_Manufacturers = df.groupby('company')
    res = car_Manufacturers['company','average-mileage'].mean()

    lbl.grid(column =4, row=15)
    lbl.configure(text=res)
    
def clicked7():
     carsDf = df.sort_values(by=['price', 'horsepower'], ascending=False)  
     res=carsDf.head(5)
     lbl.grid(column =0,row= 13)
     lbl.configure(text=res)
     
def clicked8():
    GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
    carsDf1 = pd.DataFrame.from_dict(GermanCars)
    japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],'Price': [29995, 23600, 61500 , 58900]}
    carsDf2 = pd.DataFrame.from_dict(japaneseCars)
    res = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
    lbl.grid(column =6, row=1)
    lbl.configure(text=res)
  
def clicked9():
    Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
    carPriceDf = pd.DataFrame.from_dict(Car_Price)

    car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
    carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

    res = pd.merge(carPriceDf, carsHorsepowerDf, on="Company" ,)
    lbl.grid(column =6, row=5)
    lbl.configure(text=res)
           
# button widget with red color text
# inside
btn1 = Button(root, text = "Click here to display Cars" ,
             fg = "blue", command=clicked1)

# set Button grid
btn1.grid(column=0, row=2)
# button widget with red color text
# inside
btn2 = Button(root, text = "Click here to display Toyoto Cars" ,
             fg = "red", command=clicked2)

# set Button grid
btn2.grid(column=0, row=4)
# all widgets will be here
# Execute Tkinter

#button widget with green color text 
#inside
btn3 = Button(root, text = "Click here to display most expensive car company" ,
             fg = "green", command=clicked3)

#set Button grid
btn3.grid(column=0, row=5)

#button widget with purple color text 
#inside
btn4 = Button(root, text = "Click here to display count total cars per company ",
              fg = "purple", command=clicked4)

#set button grid
btn4.grid(column=0, row=6)

#button widget with orange color text
btn5 = Button(root, text = "Click here to display Find each companys Highest price car" ,
              fg = "orange", command=clicked5)

#set button grid
btn5.grid(column=0, row=7)

#button widget with yellow color text
btn6 = Button(root, text = "Click here to display Find the average mileage of each car making company" , 
              fg = "yellow", command= clicked6)
#set button grid
btn6.grid(column=0, row=8)

#button widget with lavender color text 
btn7 = Button(root, text = "Click here to display sort all cars by  price column" ,  
              fg = "blue", command= clicked7)
#set button grid 
btn7.grid(column=0, row=9)

#button widget wih red color text
btn8 = Button(root, text = "Click here to display Concatenate two data frames using the followi ng conditions" ,
              fg="red", command= clicked8)
#set button grid
btn8.grid(column=6, row=1)

#button widget with blue color text
btn9 = Button(root, text = "Click here to display Merge two data frames using the following condition" ,
              fg="blue" , command= clicked9)
#set button grid
btn9.grid(column=6, row=2)

              
root.mainloop()
