from tkinter import *
from ast import literal_eval
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class RightFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid(row=0, column=1,sticky=S+N+E+W)
        master.grid_columnconfigure(0,weight=1)
        master.grid_rowconfigure(0,weight=1)

    def insert(self, x, y):
        fig = plt.figure(figsize=(4, 5))
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("Expression Value")
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky=S+N+E+W, ipadx=40, ipady=20)
        toolbarframe = Frame(master=self)
        toolbarframe.grid(row=2, column=0)
        NavigationToolbar2Tk(canvas, toolbarframe)



class LeftFrame(Frame):
    def __init__(self, master=None,rframe=None):
        Frame.__init__(self, master)
        self.master = master
        self.rframe = rframe
        self.grid(row=0, column=0, sticky=S+N+E+W)
        master.grid_columnconfigure(1,weight=1)

        self.lab1 = Label(self,text="Expression (variable x): ", font = ("Fixedsys", 12, "bold"))
        self.lab1.grid(row=0,column=0, sticky=S+N+E+W)

        self.exprtext = Text(self, width=25 ,height=2, font = ("Fixedsys", 12))
        self.exprtext.insert(END, "expr")
        self.exprtext.grid(row=0, column=1, columnspan=2, sticky=S+N+E+W)

        self.lab2 = Label(self, text="Variable Range (a,b): ", font = ("Fixedsys", 12, "bold"))
        self.lab2.grid(row=1, column=0, sticky=S+N+E+W)

        self.variablevalue = Text(self,width=25,height=2, font = ("Fixedsys", 12))
        self.variablevalue.insert(END, "value")
        self.variablevalue.grid(row=1, column=1, columnspan=2)


        self.evaluatebutton = Button(self,text="Evaluate !",command=self.evaluate,width=28,height=2)
        self.evaluatebutton.grid(row=2, column=0, sticky=S+N+E+W)

        self.exitbutton = Button(self, text="Exit", command=exit, width=28, height=2)
        self.exitbutton.grid(row=2, column=1, sticky=S+N+E+W)

    def evaluate(self):
        expr = self.exprtext.get(1.0,END)
        varval = self.variablevalue.get(1.0,END)
        a = literal_eval(varval)
        aa = []
        np.array(aa)
        points = 1000 # Number of points
        xmin, xmax = a[0], a[1]
        xlist = []
        ylist = []
        for i in range(points+1):
            x = float(xmax - xmin) * float(i) // points
            x = x+xmin
            expr1 = expr.strip('\n')
            xlist.append(x)
            y = eval(expr1)
            ylist.append(y)
        self.rframe.insert(xlist, ylist)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.geometry("1000x600")
        self.rightframe = RightFrame(master)
        self.leftframe = LeftFrame(master,self.rightframe)
        master.wm_title("Graph plotting window")
        self.grid(row=0,column=0,sticky="nsew")

root = Tk()
app = Window(root)
root.mainloop()