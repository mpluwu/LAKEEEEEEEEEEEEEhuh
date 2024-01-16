import time
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from tkinter.ttk import *
from PIL import Image, ImageTk
ph=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0 ,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3,9.3,8.9,8.8,8.5,8.6,8.2,9,8.7,9,9.1,8.7,8.6,8.8,9.06,0,8.6,8.2,8.9,8.6,8.5,8.4,7.4,8.6,8.4,8.4,8.5,8.6,8.7,8.1,8.4,8.6,9.2,9.4,9.6,9.1,0,8.9,8.64,8.77,8.5,9.2,8.7]
phnorm=[6.5,8.5]
dates=["Yanvar 2018", "Fevral 2018", "Mart 2018", "Aprel 2018","May 2018","Iyun 2018","Iyul 2018","Sentyabr 2018","Oktyabr 2018","Noyabr 2018","Dekabr 2018","Yanvar 2019","Fevral 2019","Mart 2019","Aprel 2019"]
menteqeler=['Taxtakorpu','Su goturucu qurgunun adi','Cenub stansiyasi','cenub qerb dambasi','cenub dambasi','simal serq dambasi','meliorasiya']
abc=[]
a=0
k=0
av=[]
for i in range(len(dates)):
    abc=ph[i:i+7]
    n=7
    if 0 in abc:
        n=n-abc.count(0)    
    a=sum(abc)/n
    av.append(a)
ceyran=tk.Tk()
ceyran.geometry("400x500")
image=Image.open("ceyran.png")
image= image.resize((300,205))
image=ImageTk.PhotoImage(image)
imaje=tk.Label(ceyran, image=image)
mainbutton=Button(ceyran, text='Ceyranbatan infocenter',command=ceyran.destroy)
imaje.pack()
mainbutton.pack()
ceyran.mainloop()
stat=tk.Tk()
stat.geometry('400x500') 
value = 1
def change_value():
    global value
    value -= 1
    if value == 0:
        k=simpledialog.askstring(title='???',prompt='Hansi ay ve il uzre?')
        k=k.capitalize()
        while k not in dates:
            k=simpledialog.askstring(title='???',prompt='Hansi ay ve il uzre?')
            k=k.capitalize()
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(ph[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        plt.plot(menteqeler,h)
        plt.show()
    else:
        pass
phbtn=Button(stat, text='Ph statistikasi!',command=change_value)
phbtn.pack()
stat.mainloop()
