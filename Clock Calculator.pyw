#Made By Dylan Logan @ Cleardata Ltd.

import sys
import os
from tkcalendar import Calendar, DateEntry #3rd party python module, make sure you do: pip install tkcalendar
from datetime import datetime, timedelta

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
    
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Clock_Calculator (root)
    init(root, top)
    root.mainloop()

w = None
def create_Clock_Calculator(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Clock_Calculator (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Clock_Calculator():
    global w
    w.destroy()
    w = None


class Clock_Calculator:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "TkDefaultFont"

        top.geometry("480x180")
        top.title("Clock Calculator")
        top.iconbitmap(r"I:\Dylans Folder\Icon\myIcon.ico")
        top.configure(background="#d9d9d9")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.02, rely=0.06, height=21, width=50)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''In''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.02, rely=0.33, height=21, width=50)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''In''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.02, rely=0.61, height=21, width=50)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''In''')

        self.E1 = StringVar()
        self.Entry1 = Entry(top, textvariable=self.E1)
        self.Entry1.place(x=60, y=10, height=20, width=164)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        
        self.E2 = StringVar()
        self.Entry2 = Entry(top, textvariable=self.E2)
        self.Entry2.place(x=60, y=60, height=20, width=164)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.E3 = StringVar()
        self.Entry3 = Entry(top, textvariable=self.E3)
        self.Entry3.place(x=60, y=110, height=20, width=164)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        
        self.Label4 = Label(top)
        self.Label4.place(relx=0.5, rely=0.06, height=21, width=50)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Out''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.5, rely=0.33, height=21, width=50)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Out''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.5, rely=0.61, height=21, width=50)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Out''')

        self.E4 = StringVar()
        self.Entry4 = Entry(top, textvariable=self.E4)
        self.Entry4.place(x=290, y=10, height=20, width=164)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.E5 = StringVar()
        self.Entry5 = Entry(top, textvariable=self.E5)
        self.Entry5.place(x=290, y=60, height=20, width=164)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")

        self.E6 = StringVar()
        self.Entry6 = Entry(top, textvariable=self.E6)
        self.Entry6.place(x=290, y=110, height=20, width=164)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Label7 = Label(top)
        self.Label7.place(relx=0.79, rely=0.83, height=21, width=80)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Total: 00:00:00''')

        def time_diff(time1, time2):
            FMT = '%H:%M'
            difference = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)

            return difference
            
        
        def search(*args):
            in1 = self.E1.get()
            in2 = self.E2.get()
            in3 = self.E3.get()
            out1 = self.E4.get()
            out2 = self.E5.get()
            out3 = self.E6.get()

            if in1 and out1:
                diff1 = time_diff(in1, out1)
            if in2 and out2:
                diff2 = time_diff(in2, out2)
            if in3 and out3:
                diff3 = time_diff(in3, out3)

            if in1 and in2 and in3 and out1 and out2 and out3:
                overall = diff1 + diff2 + diff3
                average = timedelta(hours=7, minutes=15, seconds=0) #change this, to match your working hours in a day.
                
                if overall < average:
                    self.Label7.configure(foreground="#ff0000")

                elif overall == average:
                    self.Label7.configure(foreground="#000000")

                elif overall > average:
                    self.Label7.configure(foreground="#008000")
                    
                self.Label7.configure(text='''Total: %s''' % overall)
        
        self.Button1 = Button(top)
        self.Button1.place(relx=0.62, rely=0.83, height=25, width=65)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Calculate''', command=search)

        self.cal = DateEntry(top, background='grey',
                    foreground='white', borderwidth=2)
        self.cal.place(x=60, y=150, height=20, width=163)
        #self.cal.set_date('01/01/0001')
        
        def Save():
            in1 = self.E1.get()
            in2 = self.E2.get()
            in3 = self.E3.get()
            out1 = self.E4.get()
            out2 = self.E5.get()
            out3 = self.E6.get()

            if in1 and out1:
                diff1 = time_diff(in1, out1)
            if in2 and out2:
                diff2 = time_diff(in2, out2)
            if in3 and out3:
                diff3 = time_diff(in3, out3)

            if in1 and in2 and in3 and out1 and out2 and out3:
                overall = diff1 + diff2 + diff3

            date = self.cal.get()
            day, month, year = date.split('/')
            datestamp = year+month+day

            #datestamp = datetime.today().strftime('%Y%m%d')
            #date = datetime.today().strftime('%d/%m/%Y') 

            if not os.path.exists(os.path.join(os.getcwd(), 'Logs')):
                os.mkdir(os.path.join(os.getcwd(), 'Logs'))
            
            with open(os.path.join(os.path.join(os.getcwd(), 'Logs'), datestamp+'.txt'), 'w') as fout:
                fout.write('%s\n\nIn: %s - Out: %s\nIn: %s - Out: %s\nIn: %s - Out: %s\n\nTotal: %s' % (date, in1, out1, in2, out2, in3, out3, overall))
        
        self.menubar = Menu(top,font=font10,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=Save,
                font=font10,
                foreground="#000000",
                label="Save")

if __name__ == '__main__':
    vp_start_gui()



