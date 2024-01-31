import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
ph=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3,9.3,8.9,8.8,8.5,8.6,8.2,9,8.7,9,9.1,8.7,8.6,8.8,9.06,0,8.6,8.2,8.9,8.6,8.5,8.4,7.4,8.6,8.4,8.4,8.5,8.6,8.7,8.1,8.4,8.6,9.2,9.4,9.6,9.1,0,8.9,8.64,8.77,8.5,9.2,8.7,0,8.5,8.3,8.5,8.5,8.4,8.5,9.7,8.5,8.4,8.6,8.3,8.7,8.4,8.7,8.8,8.4,8.7,8.8,8.6,8.7,8.4,8.4,8.4,8.3,8.4,8.3,8.7,8.3,8.4,8.6,8.7,8.2,8.5,8.4,8.7,8.6,8.2,8.4,8.7,8.6,8.8,8.4,8.4,8.5,8.4,8.4,8.5,8.3,8.2,8.5,8.4,8.6,8.6,8.5,8.3,8.0,8.4,8.5,8.5,8.5,8.4,8.4,0,8.4,8.4,8.3,8.6,8.4,8.4,0,8.4,8.4,8.3,8.6,8.4,8.4,8.4,8.4,8.5,8.4,8.5,8.3,8.4,8.4,8.6,8.6,8.5,8.5,8.6,8.4,8.2,8.3,8.3,8.5,8.4,8.2,8.3,8.5,0,0,0,0,0,0,8.7,8.7,8.7,8.6,8.6,8.5,8.6,8.4,8.5,8.5,8.4,8.5,8.5,8.6,8.4,8.4,8.5,8.4,8.5,8.3,8.4]
temp=[7.7,7.3,7.4,7.6,7.1,7.2,7,6.7,8.4,8.5,8.5,8.6,8.5,9.2,0,13.7,13.6,14,14.1,15.3,13.8,12.8,12.7,12.6,12.8,13.1,13.2,13,12.8,12.7,12.6,12.8,13.1,13.2,13,27.6,27.6,28.4,29.2,28.3,28.6,28.7,30.1,28.6,28.3,29.3,28.8,29.1,29.9,0,24.8,24,24.7,24.9,25,25.1,19.9,20,20.6,20.6,20.3,20.4,20,11.8,10.4,10.5,10.7,10.2,10.8,11.3,11.5,10.6,10.5,11.6,10.7,10.3,10.1,0,6.8,7.1,7.3,7.3,7.2,7.3,6.6,6.6,6.7,6.9,6.7,6.6,6.7,10,9.6,9.8,10.1,9.7,9.7,10,0,18.5,20.2,16.8,16.5,20.3,17.0,0,20.9,20.8,20.1,20.3,20.4,20.6,19.0,25.0,24.8,25.2,25.1,24.7,25.3,22.0,24.7,24.6,24.3,24.7,24.9,24.8,23,23.4,23.4,23.6,23.5,23.6,23.6,24.8,24.5,24.8,24.7,24.2,23.8,24.1,23.69,23.2,23.7,24.0,25.2,23.3,23.7,5.8,5.7,6.2,6.3,6.4,6.6,6.8,5.6,5.4,6.6,6.6,6.7,6.8,6.8,8.5,7.5,9.3,9.4,9.4,9.5,9.5,0,10.5,11.3,11.4,11.9,11.5,12.0,0,19.5,20.3,20.4,20.9,20.5,20.0,21.9,23.9,24.0,20.4,24.0,24.1,23.9,25.0,29.0,29.2,28.7,29.0,29.1,28.5,23.0,26.2,26.1,26.0,25.0,26.3,26.0,0,0,0,0,0,0,0,19.1,19.8,20.1,19.9,20.0,20.1,20.0,11.1,12.5,12.8,12.9,13.1,13.1,13.4,8.3,8.9,9.2,9.5,9.4,9.6,9.6]
elekkeciricilik=[438,596,593,597,594,592,593,467,653,671,668,657,663,647,0,683,681,672,678,669,687,459,883,888,879,881,867,890,459,883,888,879,881,867,890,370,326,364,1494,357,345,386,1601,349,508,1565,1311,988,1462,0,0,0,0,0,0,0,0,519,1672,1518,1504,418,584,363,744,710,3510,780,755,770,367,539,555,488,490,518,631,374,540,523,22000,528,529,523,0,539,522,534,1047,545,547,624,354,421,427,446,447,348,407,565,544,522,616,610,402,0,514,524,557,562,727,560,0,610,592,605,600,589,645,411,544,585,620,590,618,612,377,530,810,950,680,575,510,374,562,566,567,565,560,564,385,410,830,910,860,840,713,525,840,830,750,780,890,775,0,0,0,0,0,0,0,0,0,0,0,0,0,0,502.0,601.0,610.0,605.0,608.0,606.0,598.0,508.0,616.0,620.0,1348.0,1350.0,614.0,596.0,523.0,629.0,630.0,800.0,810.0,632.0,630.0,0,620.0,600.0,810.0,800.0,632.0,630.0,0,632.0,620.0,822.0,784.0,628.0,624.0,405.0,639.0,650.0,740.0,620.0,640.0,634.0,381.0,705.0,700.0,1195.0,1200.0,700.0,845.0,404.0,556.0,750.0,1200.0,800.0,700.0,764.0,0,0,0,0,0,0,0,452.0,572.0,630.0,2900.0,610.0,600.0,570.0,452.0,554.0,610.0,1200.0,600.0,594.0,570.0,400.0,560.0,600.0,941.0,620.0,640.0,634.0]
codluq=[3.2,3.2,3,3.3,3.4,3.3,3,3.4,3.8,4.2,3.4,3,2.92,3.2,0,3.2,3,3.1,3,2.9,3.3,3.2,4.1,3.7,6.5,3.4,4,4,3.2,4.1,3.7,6.5,3.4,4,4,2.2,3,2.8,3.6,3.2,3.3,2.8,2.4,2.6,3.1,2.9,4,3,2.8,0,0,0,0,0,0,0,0,2.5,2.7,3.3,3.6,4.2,2.5,2.6,2.8,2.9,3.2,3.6,4.7,2.7,2.6,2.8,3.1,3.3,2.8,2.4,2.6,3.4,3.8,4.2,3.4,3,2.92,3.2,0,2.9,2.8,2.2,2.9,2.5,3.6,3.2,4,3.8,3.,4,4.4,3.8,3.2,2.6,2.8,2.4,3,3.1,3.2,0,3.8,3.6,3.9,3.7,4.1,3.8,0,3.2,3.8,4.,3.,4.,4.2,2.8,2.9,3.2,3.4,3.8,3.4,2.6,3.6,3.8,4.2,4.9,4.8,3.9,3.4,3.5,3.4,3.6,4.6,4.8,4.4,3.2,3.6,3.6,3.4,4.8,4.6,5.6,4.2,3.5,3.6,3.4,4.2,4.4,4.2,3.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3.5,3.9,4.0,4.2,4.4,3.7,3.3,3.8,3.4,4.4,4.6,5.2,3.9,3.3,3.9,3.7,4.4,4.1,4.2,3.8,3.6,0,3.1,4.1,4.3,4.2,3.6,3.4,0,3.2,4.1,4.2,4.1,3.7,3.5,4.1,4.2,5.1,5.2,5.1,4.7,5.5,3.0,2.0,3.0,3.0,2.0,2.0,3.0,3.5,4.1,4.6,5.2,4.5,3.9,3.5,0,0,0,0,0,0,0,3.8,3.9,4.2,4.4,5.6,3.9,3.7,3.8,3.7,4.0,4.2,5.4,3.7,3.4,4.1,4.2,5.1,5.2,5.1,4.7,5.5]
qelevilik=[150,173,176,173,170,167,179,840,900,890,840,850,890,900,0,350,325,345,380,325,345,141,162,159,159,159,159,162,141,162,159,159,159,159,162,132,138,123,150,482,135,129,112,120,92,135,133,118,117,0,0,0,0,0,0,0,0,150,1665,1615,1614,1504,620,150,173,170,600,170,176,173,114,102,110,122,118,131,120,120,170,150,300,153,163,173,0,173,170,182,173,176,170,173,183,181,150,153,158,150,134,118,124,141,112,108,120,0,180,193,200,207,183,197,0,173,145,153,157,153,150,153,140,120,133,152,144,135,120,134,142,151,144,144,110,132,150,153,156,147,150,153,131,122,141,152,146,136,117,130,140,120,150,136,124,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
qoxu=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dates=["Yanvar 2018", "Fevral 2018", "Mart 2018", "Aprel 2018","May 2018","İyun 2018","İyul 2018","Sentyabr 2018","Oktyabr 2018","Noyabr 2018","Dekabr 2018","Yanvar 2019","Fevral 2019","Mart 2019","Aprel 2019","May 2019","İyun 2019","İyul 2019","Avqust 2019","Sentyabr 2019","Oktyabr 2019","Yanvar 2020","Fevral 2020","Mart 2020","Aprel 2020","May 2020","İyun 2020","İyul 2020","Avqust 2020","Sentyabr 2020","Oktyabr 2020","Noyabr 2020","Dekabr 2020"]
menteqeler=['Taxtakörpü-Ceyranbatan kanalı','Su götürücü qurğunun yanı','Cənub nasos stansiyasının yanı','Cənub-qərb dambası, sızma suları','Cənub dambası, sızma suları','Şimal-şərq dambası, sızma suları','Meliorasiya nasos stansiyasının girişi']
path1='photo_1.jpg'
path2='photo_2.jpg'
path3='photo_3.jpg'
path4='photo_4.jpg'
def createceyran():
    ceyran=tk.Toplevel()
    ceyran.geometry("400x500")
    image=Image.open("ceyran.jpg")
    image= image.resize((300,205))
    image=ImageTk.PhotoImage(image)
    imaje=tk.Label(ceyran, image=image)
    mainbutton=Button(ceyran, text='Ceyranbatan Su Anbarı İnfocenter',command=createinfo)
    secondbutton=Button(ceyran, text='Qalereya', command=createGallery)
    exitbtn=Button(ceyran, text='Çıxış', command=ceyran.destroy)
    imaje.pack()
    mainbutton.pack()
    secondbutton.pack()
    exitbtn.pack()
    ceyran.mainloop()
def createstat():
    stat=tk.Toplevel()
    stat.geometry('400x500') 
    def phstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
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
        num=[]
        for i in range(len(h)):
            num.append(i+1)
        abc=[]
        root=tk.Toplevel()
        root.geometry('500x400')
        columns = ('say','menteqeler', 'qiymetler')
        tree = Treeview(root, columns=columns)
        tree.heading('say', text='Say')
        tree.heading('menteqeler', text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(num)):
            abc.append((num[i], locations[i], h[i]))
        for i in abc:
            tree.insert('',tk.END, values=i)
        sonrabtn=Button(root, text='Sonrakı', command=tempstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
        if (sum(h)/len(h))>8.5 or (sum(h)/len(h))<6.5:
            answer=messagebox.askyesno("error","Qiymətlərdə uyğunsuzluq müşahidə olunur. Müvafiq orqanlara xəbərdarlıq göndərilsinmi?")
            if answer:
                messagebox.showinfo("sending", "Xəbərdarlıq göndərilir.")
            else:
                messagebox.showinfo("not sent", "Xəbərdarlıq göndərilmədi.")
        root.mainloop()
    def tempstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(temp[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        num=[]
        for i in range(len(h)):
            num.append(i+1)
        abc=[]
        root=tk.Toplevel()
        root.geometry('500x400')
        columns = ('say','menteqeler', 'qiymetler')
        tree = Treeview(root, columns=columns)
        tree.heading('say', text='Sayı')
        tree.heading('menteqeler', text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(num)):
            abc.append((num[i], locations[i], h[i]))
        for i in abc:
            tree.insert('',tk.END, values=i)
        sonrabtn=Button(root, text='Sonrakı', command=elekstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
        root.mainloop()
    def qelevilikstat():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(qelevilik[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        num=[]
        for i in range(len(h)):
            num.append(i+1)
        abc=[]
        root=tk.Toplevel()
        root.geometry('500x400')
        columns = ('say','menteqeler', 'qiymetler')
        tree = Treeview(root, columns=columns)
        tree.heading('say', text='Sayı')
        tree.heading('menteqeler', text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(num)):
            abc.append((num[i], locations[i], h[i]))
        for i in abc:
            tree.insert('',tk.END, values=i)
        sonrabtn=Button(root, text='Sonrakı', command=codluqstatistika)
        tree.pack()
        sonrabtn.pack()
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
        root.mainloop()
    def elekstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(elekkeciricilik[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        num=[]
        for i in range(len(h)):
            num.append(i+1)
        abc=[]
        root=tk.Toplevel()
        root.geometry('500x400')
        columns = ('say','menteqeler', 'qiymetler')
        tree = Treeview(root, columns=columns)
        tree.heading('say', text='Sayı')
        tree.heading('menteqeler', text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(num)):
            abc.append((num[i], locations[i], h[i]))
        for i in abc:
            tree.insert('',tk.END, values=i)
        tree.pack()
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
        root.mainloop()
    def codluqstatistika():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(codluq[c])
            c+=1
        while 0 in h:
            k=h.index(0)
            del locations[k]
            del h[k]
        num=[]
        for i in range(len(h)):
            num.append(i+1)
        abc=[]
        root=tk.Toplevel()
        root.geometry('500x400')
        columns = ('say','menteqeler', 'qiymetler')
        tree = Treeview(root, columns=columns)
        tree.heading('say', text='Sayı')
        tree.heading('menteqeler', text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(num)):
            abc.append((num[i], locations[i], h[i]))
        for i in abc:
            tree.insert('',tk.END, values=i)
        tree.pack()
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
        root.mainloop()
    def qoxustat():
        k=0
        plt.clf()
        while k not in dates:
            k=simpledialog.askstring(title='Sorğu',prompt='Hansı ay və il üzrə?')
            k=k.capitalize()
            if k not in dates:
                messagebox.showerror('Xəta', 'Axtardığınız sorğu üzrə nəticə tapılmadı.')
        c=dates.index(k)
        c=c*7
        h=[]
        locations=menteqeler
        for i in range(7):
            h.append(qoxu[c])
            c+=1
        num=[]
        for i in range(len(h)):
            num.append(i+1)
        abc=[]
        root=tk.Toplevel()
        root.geometry('500x400')
        columns = ('say','menteqeler', 'qiymetler')
        tree = Treeview(root, columns=columns)
        tree.heading('say', text='Sayı')
        tree.heading('menteqeler', text='Məntəqə')
        tree.heading('qiymetler', text='Qiyməti')
        for i in range(len(num)):
            abc.append((num[i], locations[i], h[i]))
        for i in abc:
            tree.insert('',tk.END, values=i)
        tree.pack()
        plt.plot(locations, h, 'g',marker='o')
        plt.grid()
        plt.show()
        root.mainloop()
    back=Button(stat, text='Geri', command=stat.destroy)
    def fizikpler():
        fizikiler=tk.Toplevel()
        fizikiler.geometry("200x200")
        phbtn=Button(fizikiler, text='Ph statistikası',command=phstatistika)
        tempbtn=Button(fizikiler, text='Temperatur statistikası',command=tempstatistika)
        elekbtn=Button(fizikiler, text='Elektrik keçiricilik statistikası', command=elekstatistika)
        back=Button(fizikiler, text='Geri', command=fizikiler.destroy)
        phbtn.pack()
        tempbtn.pack()
        elekbtn.pack()
        back.pack(side='right')
        fizikiler.mainloop()
    def kimyepler():
        kimyalar=tk.Toplevel()
        kimyalar.geometry("200x200")
        qelevibtn=Button(kimyalar, text='Qelevilik statistikası', command=qelevilikstat)
        codbtn=Button(kimyalar, text='Codluq statistikası', command=codluqstatistika)
        back=Button(kimyalar, text='Geri', command=kimyalar.destroy)
        qelevibtn.pack()
        codbtn.pack()
        back.pack(side='right')
    def orqanlar():
        orqanaleptik=tk.Toplevel()
        orqanaleptik.geometry("200x200")
        qoxubtn=Button(orqanaleptik, text='Qoxu statistikası', command=qoxustat)
        back=Button(orqanaleptik, text='Geri', command=orqanaleptik.destroy)
        qoxubtn.pack()
        back.pack(side='right')
        orqanaleptik.mainloop()
    fiziki_btn=Button(stat, text='Fiziki parametrlər', command=fizikpler)
    kimya_btn=Button(stat, text="Kimyəvi parametrlər", command=kimyepler)
    orqanaleptik_btn=Button(stat, text='Orqanaleptik parametrlər', command=orqanlar)
    fiziki_btn.pack()
    kimya_btn.pack()
    orqanaleptik_btn.pack()
    back.pack(side='right')
    stat.mainloop()
def createGallery():
    Gallery=tk.Toplevel()
    Gallery.geometry('600x600')
    img1 = ImageTk.PhotoImage((Image.open(path1)).resize((300,250)))
    panel1 = tk.Label(Gallery, image = img1)
    img2 = ImageTk.PhotoImage((Image.open(path2)).resize((300,250)))
    panel2 = tk.Label(Gallery, image = img2)
    img3 = ImageTk.PhotoImage((Image.open(path3)).resize((300,250)))
    panel3 = tk.Label(Gallery, image = img3)
    img4 = ImageTk.PhotoImage((Image.open(path4)).resize((300,250)))
    panel4 = tk.Label(Gallery, image = img4)
    back=Button(Gallery, text='Geri', command=createceyran and Gallery.destroy)
    back.pack(side='right')
    panel1.pack(side='left')
    panel2.pack(side='bottom')
    panel3.pack(side='top')
    panel4.pack()
    Gallery.mainloop()
def createinfo():
    Info=tk.Toplevel()
    Info.geometry('700x700')
    T=tk.Text(Info, height = 5, width = 57)
    l = Label(Info, text = "Məlumat")
    back=Button(Info, text='Geri', command=Info.destroy)
    lookatstats=Button(Info, text='Statlara bax', command=createstat)
    melumat='Samur-Abşeron kanalından qidalanan Ceyranbatan su anbarı və anbarın sahilində tikilmiş su təmizləyici qurğular kompleksi Abşeron yarımadasının içməli su təchizatında böyük paya malikdir.'
    image=Image.open("ceyran.jpg")
    image= image.resize((400,500))
    image=ImageTk.PhotoImage(image)
    imaje=tk.Label(Info, image=image)
    l.pack()
    T.pack()
    imaje.pack()
    back.pack()
    lookatstats.pack()
    T.insert(tk.END, melumat)
    Info.mainloop()
titul=tk.Tk()
titul.geometry('500x400')
image=Image.open("ceyran.jpg")
image= image.resize((400,500))
image=ImageTk.PhotoImage(image)
titulbtn=Button(titul, text = 'kliklə', image = image, command=createceyran).pack()
titul.mainloop()
