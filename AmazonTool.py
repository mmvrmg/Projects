import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
matplotlib.use('TkAgg')
import datetime
import sys


style.use('seaborn-pastel')
#tax_rate = df['Item Subtotal Tax'].sum()/df['Total Owed'].sum()
#daily_orders = df.groupby('Order Date').sum()["Total Owed"]


def upload():
    filename = filedialog.askopenfilename()
    df = pd.read_csv(filename)
    df = df.fillna(0)

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    calc_numbers = df[['Price','Price Tax','Shipping Charge','Total Discounts',
                       'Total Owed','Item Subtotal','Item Subtotal Tax']]

    calc_numbers = calc_numbers.astype(float)
    return df

csv_name = upload()

class AmazonToolGUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'AmazonTool')

        window = tk.Frame(self)
        window.pack(side='top', fill='both', expand=True)
        
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (Main_Page,list_of_items):

            frame = F(window, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Main_Page)

    def show_frame(self, container):

        frame = self.frames[container]
        frame.tkraise()
   
#_______________________________________________________________

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

# ax1.plot('Order Date', 'Total Owed', data=csv_name)
# ax1.set(ylabel='Total(£)')
# ax1.set_title('Money')
# ax2.plot('Order Date', 'Item Subtotal Tax', data=csv_name)
# ax2.set(ylabel='Total(£)')
# ax2.set_title('Tax')

# ax3.plot('Order Date', 'Shipping Charge', data=csv_name)
# ax3.set(ylabel='Total(£)')
# ax3.set_title('Shipping Charge')

# ax4.plot('Order Date', 'Total Owed', data=csv_name)
# ax4.set(ylabel='Total(£)')
# ax4.set_title('Money')

#_______________________________________________________________

class Main_Page(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        Main_Page.config(self, background='#f5bd22')

        label = ttk.Label(self, text='This is the Main Page page')
        label.pack()

        button2 = ttk.Button(self, text='List of Purchases', command=lambda: controller.show_frame(list_of_items))
        button2.pack()

        exit_button = ttk.Button(self, text='Exit', command=self.quit) 
        exit_button.pack()

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

        ax1.plot('Order Date', 'Total Owed', data=csv_name)
        ax1.set(ylabel='Total(£)')
        ax1.set_title('Money')
        ax2.plot('Order Date', 'Item Subtotal Tax', data=csv_name)
        ax2.set(ylabel='Total(£)')
        ax2.set_title('Tax')

        ax3.plot('Order Date', 'Shipping Charge', data=csv_name)
        ax3.set(ylabel='Total(£)')
        ax3.set_title('Shipping Charge')

        ax4.plot('Order Date', 'Total Owed', data=csv_name)
        ax4.set(ylabel='Total(£)')
        ax4.set_title('Money')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()

class list_of_items(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        exit_button = ttk.Button(self, text='Exit', command=self.quit) 
        exit_button.pack()

        back_button = ttk.Button(self, text='Back', command=lambda: controller.show_frame(Main_Page))
        back_button.pack()

        product_names= list(csv_name['Product Name'])
        
        lb = tk.Listbox(self, height=len(product_names), width=50, font=('Times New Roman', 15))
        
        item_number = 0
        product_names[:] = (names[:30] + '...' for names in product_names)
        while item_number <= len(product_names)-1:
            lb.insert(item_number, product_names[item_number])
            item_number += 1
        
        lb.pack()

        

app = AmazonToolGUI()
app.geometry('1000x1000')
app.resizable(0, 0)
app.grid_propagate(0)

app.mainloop()
