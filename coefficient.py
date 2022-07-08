import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from alpha_vantage.timeseries import TimeSeries
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib.pylab import rcParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import json
import numpy as np
import pandas as pd
import time
import webbrowser
import sqlite3

# style.use('') = theme for the graphs
style.use('dark_background')

font1 = ('Verdana', 20)
font2 = ('Verdana', 50)
font3 = ('Verdana', 14)
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

# #def stcksDB():
#     #with sqlite3.connect('stocksDB.db') as db:
#         #c = db.cursor()

#     stocksDB ="""
#     CREATE TABLE IF NOT EXISTS UsersTB(
#         UserID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Forename VARCHAR(80) NOT NULL,
#         Surname VARCHAR(80) NOT NULL,
#         Username VARCHAR(20) NOT NULL,
#         Password VARCHAR(80) NOT NULL
#         );

#     CREATE TABLE IF NOT EXISTS transactionsTB(
#         TransactionsID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Buys FLOAT NOT NULL,
#         Nº Buys INTEGER,
#         sells FLOAT NOT NULL,
#         Nº Sells INTEGER,
#         FOREIGN KEY(companyID) REFERENCES companyTB(companyID)
#         FOREIGN KEY(userID) REFERENCES userTB(userID) 
#         );

#     CREATE TABLE IF NOT EXISTS notesTB(
#         Note TEXT,
#         Date_created DATETIME,
#         FOREIGN KEY(userID) REFERENCES users_table(userID));

#     CREATE TABLE IF NOT EXISTS companyTB(
#         companyID INTEGER,
#         Symbol STRING,
#         Last_price FLOAT
#         );
        
#     INSERT INTO companyTB(companyID, Symbol)
#         SELECT NULL, 1, 'FB', 
#         WHERE NOT EXISTS (SELECT 1 FROM companyTB WHERE Symbol='FB'); 
        
#     INSERT INTO companTB(companyID, Symbol)
#         SELECT NULL, 2, 'AAPL', 
#         WHERE NOT EXISTS (SELECT 1 FROM companyTB WHERE Symbol='AAPL'); 
        
#     INSERT INTO companTB(compnyID, Symbol)
#         SELECT NULL, 3, 'AMZN', 
#         WHERE NOT EXISTS (SELECT 1 FROM companyTB WHERE Symbol='AMZN'); 
        
#     INSERT INTO companTB(companyID, Symbol)
#         SELECT NULL, 4, 'NFLX', 
#         WHERE NOT EXISTS (SELECT 1 FROM companyTB WHERE Symbol='NFLX'); 

#      INSERT INTO companyTB(companyID, Symbol)
#         SELECT NULL, 5, 'GOOGL', 
#         WHERE NOT EXISTS (SELECT 1 FROM companyTB WHERE Symbol='GOOGL');    
#     """
#     #c.execute(stocksDB)
#     #db.commit()
#     #db.close()


# *************************************************************************************
# Here I'm creating the graphs using Figure()
f = Figure()
#.add_subplot(a, b, c) is for setting up the number of graphs that will be displayed
ax1 = f.add_subplot(2,3,1)
# sharex=ax1 makes all the graphs share the same x axis
ax2 = f.add_subplot(2,3,2, sharex=ax1) 
ax3 = f.add_subplot(2,3,3, sharex=ax1)
ax4 = f.add_subplot(2,3,4, sharex=ax1)
ax5 = f.add_subplot(2,3,6, sharex=ax1)

# graph for the Facebook window
f2 = Figure()
FB1 = f2.add_subplot(2,1,1)
FBvol = f2.add_subplot(2,1,2)

# graph for the Apple window
f3 = Figure()
AA1 = f3.add_subplot(2,1,1)
AAvol = f3.add_subplot(2,1,2)

# graph for the Amazon window
f4 = Figure()
AM1 = f4.add_subplot(2,1,1)
AMvol = f4.add_subplot(2,1,2)

# graph for the Netflix window
f5 = Figure()
NF1 = f5.add_subplot(2,1,1)
NFvol = f5.add_subplot(2,1,2)

# graph for the Google window
f6 = Figure()
GO1 = f6.add_subplot(2,1,1)
GOvol = f6.add_subplot(2,1,2)
# *****************************************************************************

class GUI(tk.Tk):
    # args are arguments and kwargs are keyword arguments
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'StocksAI')
        # creating the frame
        window = tk.Frame(self)
        window.pack(side='top', fill='both', expand=True)
        # number of rows and columns
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # this is a tuple of all the different frames 
        # This is where you add the name of the existing frames
        for x in (MainFrame, Register, FAANG, Facebook, Apple, Amazon, Netflix, Google):
            frame = x(window, self)

            self.frames[x] = frame
            # nsew stretches in every direction
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises window to the front
        frame.tkraise()


class MainFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # This sets the background of the main frame to black
        MainFrame.config(self, background='black')
        # Simple strings to identify the fields or used as a title
        logolabel = tk.Label(self, text='"Logo"', font=font2, bg='black', fg='white')
        logolabel.grid(row=0, column=0)

        Wlabel = tk.Label(self, text="Welcome", font=font2, bg='black', fg='white')
        Wlabel.grid(row=0, column=3)

        userlabel = tk.Label(self, text="Username:", font=font1, bg='black', fg='white')
        userlabel.grid(row=3, column=2, sticky='E')

        passwlabel = tk.Label(self, text="Password:", font=font1, bg='black', fg='white')
        passwlabel.grid(row=4, column=2, sticky='E')

        optlabel = tk.Label(self, text="You can also:", font=font3, bg='black', fg='white')
        optlabel.grid(row=9, column=2, sticky='E')

        blanklabel1 = tk.Label(self, text="", font=font1, bg='black', fg='white')
        blanklabel1.grid(row=0, column=0, padx=255, pady=120)

        blanklabel2 = tk.Label(self, text="", font=font1, bg='black', fg='white')
        blanklabel2.grid(row=5, column=3, pady=50)

        blanklabel3 = tk.Label(self, text="", font=font1, bg='black', fg='white')
        blanklabel3.grid(row=12, column=3, pady=120)
        # tk.Entry allows user to input staright from tkinter 
        self.userentry = tk.Entry(self)
        self.userentry.grid(row=3, column=3)

        self.passwentry = tk.Entry(self)
        self.passwentry.grid(row=4, column=3)

        gobutton = tk.Button(self, text="Go")
        gobutton.grid(row=4, column=4)
        # here I'm assigning the function show_frame to button2 so that frame Register rises to the top 
        regisbutton = tk.Button(self, text="Register", width=13, command=lambda: controller.show_frame(Register))
        regisbutton.grid(row=9, column=3)

        fangbutton = tk.Button(self, text="FAANG", width=13, command=lambda: controller.show_frame(FAANG))
        fangbutton.grid(row=11, column=3)

        # this simple command allows user to end the application by clicking button4
        exitbutton = tk.Button(self, text="Exit", width=10, command=quit)
        exitbutton.grid(row=300, column=3)

    # def login(self):

    #     with sqlite3.connect('quit.db') as db:
    #         c = db.cursor()

    #     check_user = ('SELECT * FROM UsersTB WHERE Username = ? and Password = ?')
    #     c.execute(check_user, [(Username.get()), (Password.get())])
    #     search = c.fetchall()
    #     if search:
    #         self.pack_forget()
    #     else:
    #         ms.showerror('Username does not exist')

        
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Register.config(self, background='black')

        regislabel = tk.Label(self, text='Register', font=font2, bg='black', fg='white')
        regislabel.grid(row=0, column=2)

        forlabel = tk.Label(self, text='Forename:', font=font1, bg='black', fg='white')
        forlabel.grid(row=1, column=1, sticky='E')

        surlabel = tk.Label(self, text='Surname:', font=font1, bg='black', fg='white')
        surlabel.grid(row=2, column=1, sticky='E')

        userlabel = tk.Label(self, text='Username:', font=font1, bg='black', fg='white')
        userlabel.grid(row=3, column=1, sticky='E')

        passwlabel = tk.Label(self, text='Password:', font=font1, bg='black', fg='white')
        passwlabel.grid(row=4, column=1, sticky='E')

        blanklabel1 = tk.Label(self, text="", font=font1, bg='black', fg='white')
        blanklabel1.grid(row=0, column=0, padx=260, pady=120)

        blanklabel2 = tk.Label(self, text="", font=font1, bg='black', fg='white')
        blanklabel2.grid(row=12, column=3, pady=120)

        self.forentry = tk.Entry(self)
        self.forentry.grid(row=1, column=2, padx=8)

        self.surentry = tk.Entry(self)
        self.surentry.grid(row=2, column=2)

        self.userentry = tk.Entry(self)
        self.userentry.grid(row=3, column=2)

        self.passwentry = tk.Entry(self)
        self.passwentry.grid(row=4, column=2)

        # signbutton = tk.Button(self, text="sign up", width=5, command= self.signup())
        # signbutton.grid(row=4, column=3)

        backbutton = tk.Button(self, text="back", width=12, command=lambda: controller.show_frame(MainFrame))
        backbutton.grid(row=300, column=2,)

    # def signup(self):
    #     Forename = self.forentry
    #     Surname = self.surentry
    #     Username = self.userentry
    #     Password = self.passwentry

    #     with sqlite3.connect('stocksDB.db') as db:
    #         c = db.cursor()

    #     check_user = ('SELECT * FROM UsersTB WHERE Username = ?')
    #     c.execute(check_user, [(self.userentry.get())])
    #     if c.fetchall():
    #         ms.showerror('Sorry, username taken!')
    #     else:
    #         ms.showinfo('Your account has been created')
    #         self.grid(row=5, column=5)
    #     create_acc = 'INSERT INTO UserTB(Forename, Surname, Username, Password) VALUES(?, ?, ?, ?)'
    #     c.execute(insert,[(Forename.get()), (Surname.get()), (Username.get()), (Password.get())])
    #     db.commit()    


class FAANG(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        FAANG.config(self, background='black')
        label1 = tk.Label(self, text='FAANG', font=font1, bg='black', fg='white')
        label1.pack(side=tk.TOP)
        
        
        button1 = tk.Button(self, text='Back Home', command=lambda: controller.show_frame(MainFrame))
        button1.pack(side=tk.BOTTOM, pady=10)

        button3 = tk.Button(self, text="Facebook", width=10, command=lambda:controller.show_frame(Facebook))
        button3.pack(side=tk.BOTTOM)

        button4 = tk.Button(self, text="Apple", width=10, command=lambda:controller.show_frame(Apple))
        button4.pack(side=tk.BOTTOM)

        button5 = tk.Button(self, text="Amazon", width=10, command=lambda:controller.show_frame(Amazon))
        button5.pack(side=tk.BOTTOM)

        button6 = tk.Button(self, text="Netflix", width=10, command=lambda:controller.show_frame(Netflix))
        button6.pack(side=tk.BOTTOM)
        
        button7 = tk.Button(self, text="Google", width=10, command=lambda:controller.show_frame(Google))
        button7.pack(side=tk.BOTTOM)
        # combine_funcs is a function extracted from a user in stackoverflow because I wanted to be able to 
        # repeat the same function with different values in one go
        button8 = tk.Button(self, text='update', width=10, command=lambda: combine_funcs(alpha_vantage('FB', '5min'),
                                                                                         alpha_vantage('AAPL', '5min'),
                                                                                         alpha_vantage('AMZN', '5min'),
                                                                                         alpha_vantage('NFLX', '5min'),
                                                                                         alpha_vantage('GOOGL', '5min')))
        button8.pack(side=tk.BOTTOM)
        
        # FigureCanvasTkAgg is used to embbed the figure created at the top of the code into the frame FAANG
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        # .pack is used to place widgets inside the frame
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Facebook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Facebook.config(self, background='black')

        button1 = tk.Button(self, text='Main Page', command=lambda: controller.show_frame(FAANG))
        button1.pack(side=tk.BOTTOM)
        # open_url() opens the URL in your default browser
        news_button = tk.Button(self, text='News', width=10, command=lambda: open_url('https://uk.finance.yahoo.com/quote/FB/news?p=FB'))
        news_button.pack(side=tk.BOTTOM)

        canvasfb = FigureCanvasTkAgg(f2, self)
        canvasfb.draw()
        canvasfb.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        


class Apple(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Apple.config(self, background='black')

        button1 = tk.Button(self, text='Main Page', command=lambda: controller.show_frame(MainFrame))
        button1.grid(row=1, column=3)

        news_button = tk.Button(self, text='News', command=lambda: open_url('https://uk.finance.yahoo.com/quote/AAPL/news?p=AAPL'))
        news_button.grid(row=1, column=1)

        canvasfb = FigureCanvasTkAgg(f3, self)
        canvasfb.draw()
        canvasfb.get_tk_widget().grid(row=0, column=2)


class Amazon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Facebook.config(self, background='black')

        button1 = tk.Button(self, text='Main Page', command=lambda: controller.show_frame(MainFrame))
        button1.grid(row=1, column=3)

        news_button = tk.Button(self, text='News', command=lambda: open_url('https://uk.finance.yahoo.com/quote/AMZN/news?p=AMZN'))
        news_button.grid(row=1, column=1)

        canvasfb = FigureCanvasTkAgg(f4, self)
        canvasfb.draw()
        canvasfb.get_tk_widget().grid(row=0, column=2)


class Netflix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Facebook.config(self, background='black')

        button1 = tk.Button(self, text='Main Page', command=lambda: controller.show_frame(MainFrame))
        button1.grid(row=1, column=3)

        news_button = tk.Button(self, text='News', command=lambda: open_url('https://uk.finance.yahoo.com/quote/NFLX/news?p=NFLX'))
        news_button.grid(row=1, column=1)

        canvasfb = FigureCanvasTkAgg(f5, self)
        canvasfb.draw()
        canvasfb.get_tk_widget().grid(row=0, column=2)


class Google(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Facebook.config(self, background='black')

        button1 = tk.Button(self, text='Main Page', command=lambda: controller.show_frame(MainFrame))
        button1.grid(row=1, column=3)

        news_button = tk.Button(self, text='News', command=lambda: open_url('https://uk.finance.yahoo.com/quote/GOOGL/news?p=GOOGL'))
        news_button.grid(row=1, column=1)

        canvasfb = FigureCanvasTkAgg(f6, self)
        canvasfb.draw()
        canvasfb.get_tk_widget().grid(row=0, column=2)


# the following animate functions contain the data for the plotting 
# of each company's close value at a given time

def animate(i):
    data1 = pd.read_csv('FB.csv')
    data2 = pd.read_csv('AAPL.csv')
    data3 = pd.read_csv('AMZN.csv')
    data4 = pd.read_csv('NFLX.csv')
    data5 = pd.read_csv('GOOGL.csv')
   
    
    close1 = data1['4. close']

    close2 = data2['4. close']

    close3 = data3['4. close']

    close4 = data4['4. close']

    close5 = data5['4. close']

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()

    ax1.plot(close1)

    ax2.plot(close2)

    ax3.plot(close3)

    ax4.plot(close4)

    ax5.plot(close5)

    

    ax1.set_title('FB  $' + str(data1['4. close'][len(data1)-1]))
    ax2.set_title('AAPL  $' + str(data2['4. close'][len(data2)-1]))
    ax3.set_title('AMZN  $' + str(data3['4. close'][len(data3)-1]))
    ax4.set_title('NFLX  $' + str(data4['4. close'][len(data4)-1]))
    ax5.set_title('GOOGL  $' + str(data5['4. close'][len(data5)-1]))

    
def animateFB(i):
    dataFB = pd.read_csv('FB.csv')
    dataFB['date'] = pd.to_datetime(dataFB['date'])
    dataFB["date"] = dataFB["date"].apply(mdates.date2num)

    FB1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

    closeFB = dataFB['4. close']
    volumeFB = dataFB['5. volume']

    FB1.clear()
    FBvol.clear()

    FB1.plot(closeFB)
    FBvol.plot(volumeFB)

    FB1.set_title('FB  $' + str(dataFB['4. close'][len(dataFB)-1]))


def animateAA(i):
    dataAAPL = pd.read_csv('AAPL.csv')
    dataAAPL['date'] = pd.to_datetime(dataAAPL['date'])
    dataAAPL["date"] = dataAAPL["date"].apply(mdates.date2num)

    AA1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

    closeAA = dataAAPL['4. close']
    volumeAA = dataAAPL['5. volume']

    AA1.clear()
    AAvol.clear()

    AA1.plot(closeAA)
    AAvol.plot(volumeAA)

    AA1.set_title('AAPL  $' + str(dataAAPL['4. close'][len(dataAAPL)-1]))


def animateAM(i):
    dataAMZN = pd.read_csv('AMZN.csv')
    dataAMZN['date'] = pd.to_datetime(dataAMZN['date'])
    dataAMZN["date"] = dataAMZN["date"].apply(mdates.date2num)

    AM1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

    closeAM = dataAMZN['4. close']
    volumeAM = dataAMZN['5. volume']

    AM1.clear()
    AMvol.clear()

    AM1.plot(closeAM)
    AMvol.plot(volumeAM)

    AM1.set_title('AMZN  $' + str(dataAMZN['4. close'][len(dataAMZN)-1]))


def animateNF(i):
    dataNFLX = pd.read_csv('NFLX.csv')
    dataNFLX['date'] = pd.to_datetime(dataNFLX['date'])
    dataNFLX["date"] = dataNFLX["date"].apply(mdates.date2num)

    NF1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

    closeNF = dataNFLX['4. close']
    volumeNF = dataNFLX['5. volume']

    NF1.clear()
    NFvol.clear()

    NF1.plot(closeNF)
    NFvol.plot(volumeNF)

    NF1.set_title('NFLX  $' + str(dataNFLX['4. close'][len(dataNFLX)-1]))


def animateGO(i):
    dataGOOGL = pd.read_csv('GOOGL.csv')
    dataGOOGL['date'] = pd.to_datetime(dataGOOGL['date'])
    dataGOOGL["date"] = dataGOOGL["date"].apply(mdates.date2num)

    GO1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

    closeGO = dataGOOGL['4. close']
    volumeGO = dataGOOGL['5. volume']

    GO1.clear()
    GOvol.clear()

    GO1.plot(closeGO)
    GOvol.plot(volumeGO)

    GO1.set_title('GOOGL  $' + str(dataGOOGL['4. close'][len(dataGOOGL)-1]))


def open_url(company):
    webbrowser.open(company)


def alpha_vantage(company, interval):
    ts = TimeSeries(key='843G8U8909LG87Y7', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=company, interval=interval, outputsize='full')
    data.to_csv(company + '.csv')
      
  
def run():
    print('What company (write symbol e.g. GOOGL)')
    company = input()

    print('What interval between each price\n',
          '\n'
          'Type: 1min for 1 minute\n'
          '      5min for 5 minutes\n'
          '      15min for 15 minutes')
    interval = input()

    if interval == '1min':
        alpha_vantage(company, '1min')
    elif interval == '5min':
        alpha_vantage(company, '5min')
    elif interval == '15min':
        alpha_vantage(company, '15min')


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


StocksAI = GUI()
StocksAI.geometry("1500x900")
StocksAI.resizable(0, 0)
StocksAI.grid_propagate(0)


#clock = Label(StocksAI, font=font1, bg='black', fg='white')
clock = tk.Label(StocksAI, font=font1, bg='black', fg='white')
clock.pack(fill=tk.BOTH, side=tk.RIGHT, expand=1)


def tick():
    s = time.strftime('%H:%M:%S')
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200, tick)


tick()
anim = animation.FuncAnimation(f, animate, interval=1000)
animFB = animation.FuncAnimation(f2, animateFB, interval=1000)
animAA = animation.FuncAnimation(f3, animateAA, interval=1000)
animAM = animation.FuncAnimation(f4, animateAM, interval=1000)
animNF = animation.FuncAnimation(f5, animateNF, interval=1000)
animGO = animation.FuncAnimation(f6, animateGO, interval=1000)

StocksAI.mainloop()
