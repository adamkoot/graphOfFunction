from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def zero():
       if(entryA.get()!=""):
              a = int(entryA.get())
       else:
              a = 0
       if (entryB.get() != ""):
              b = int(entryB.get())
       else:
              b = 0
       if (entryC.get() != ""):
              c = int(entryC.get())
       else:
              c = 0
       delta = b**2 - 4*a*c
       if(delta>0):
              sdelta = math.sqrt(delta)
              x1 = round((-b - sdelta)/(2 * a),2)
              x2 = round((-b + sdelta) / (2 * a),2)
              labelX.configure(text="x = "+str(x1)+" /\\ x = "+str(x2))

       elif delta==0:
              x = (-b)/(2*a)
              labelX.configure(text="x = "+str(x))
       else:
              labelX.configure(text="Nie ma miejsc zerowych")
       rysowanie(a,b,c)
def rysowanie(a,b,c):
       x = np.arange(-10, 10, 0.1)
       y = (a * (x ** 2)) + (b * x) + c
       if(b<0 and c<0):
              plt.title("Wykres y = "+str(a)+" * x^2 "+str(b)+" * x" + str(c))
       elif(b>0 and c<0):
              plt.title("Wykres y = " + str(a) + " * x^2 + " + str(b) + " * x" + str(c))
       elif (b < 0 and c > 0):
              plt.title("Wykres y = " + str(a) + " * x^2 " + str(b) + " * x + " + str(c))
       else:
              plt.title("Wykres y = " + str(a) + " * x^2 + " + str(b) + " * x + " + str(c))
       plt.close('all')
       fig = plt.figure()
       wykres = FigureCanvasTkAgg(fig, root)
       wykres.get_tk_widget().grid(row=7,column=0, columnspan=2)
       fig.add_subplot().plot(x, y)

plt.figure(figsize=(10,8), dpi=100)
root = Tk()
root.title("Quadratic function")
root.geometry("1000x1000")
title = Label(root, text =" Miejsca zerowe, wykres funkcji", justify="center")
title.grid(row=0, column=0, columnspan=4)
entryA = Entry(root)
labelA = Label(root, text = "Podaj a: ")
labelA.grid(row=1, column=0, columnspan=2)
entryA.grid(row=1, column=2, columnspan=1)
entryB = Entry(root)
labelB = Label(root, text = "Podaj b: ")
labelB.grid(row=2, column=0, columnspan=2)
entryB.grid(row=2, column=2, columnspan=5)
entryC = Entry(root)
labelC = Label(root, text = "Podaj c: ")
labelC.grid(row=3, column=0, columnspan=2)
entryC.grid(row=3, column=2, columnspan=1)
button = Button(root, text="Oblicz", command=lambda: zero() )
button.grid(row=4,column=1, columnspan=2)
labelX = Label(root, text="Miejsca zerowe rimpimpim")
labelX.grid(row=5, column=1, columnspan = 4)

root.mainloop()