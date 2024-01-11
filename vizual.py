import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from tkinter.ttk import *
ph_2018=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0 ,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3,9.3,8.9,8.8,8.5,8.6,8.2,9,8.7,9,9.1,8.7,8.6,8.8,9.06]
phnorm=[6.5,8.5]
dates_2018=["Yanvar", "Fevral", "Mart", "Aprel","May","Iyun","Iyul","Sentyabr","Oktyabr","Noyabr","Dekabr"]
ph_2019=[]
menteqeler=['Taxtakorpu','Su goturucu qurgunun adi','Cenub stansiyasi','cenub qerb dambasi','cenub dambasi','simal serq dambasi','meliorasiya']
dates_2019=[]
abc=[]
a=0
av_2018=[]
av_2019=[]
for i in range(len(dates_2018)):
    abc=ph_2018[i:i+7]
    n=7
    if 0 in abc:
        n=n-abc.count(0)
    a=sum(abc)/n
    av_2018.append(a)
for i in range(len(dates_2019)):
    abc=ph_2019[i:i+7]
    n=7
    if 0 in abc:
        n=n-abc.count(0)
    a=sum(abc)/n
    av_2019.append(a)
stat=tk.Tk()
stat.geometry('400x500') 
value = 1
def change_value():
    global value
    value -= 1
    if value == 0:
        plt.plot(dates_2018,av_2018)
        plt.show()
        value = 1
        k=simpledialog.askstring(title='???',prompt='Ay uzre?')
        if k=='yes':
            k=simpledialog.askstring(title='????',prompt='Hansi?')
            k=k.capitalize()
        c=dates_2018.index(k)
        h=[]
        for i in range(7):
            h.append(ph_2018[c])
            c+=1
        plt.plot(menteqeler,h)
        plt.show()
        for i in h:
            if phnorm[0]>i or phnorm[1]<i:
                danger=tk.Tk()
                danger.geometry('400x500')
                dangerssss=Button(danger, text='Xeberdarliq?',command=danger.destroy)
                dangerssss.pack()
                danger.mainloop()
    else:
        pass
phbtn=Button(stat, text='Ph statistikasi!',command=change_value)
phbtn.pack()
stat.mainloop()
