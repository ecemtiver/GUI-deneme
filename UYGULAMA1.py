#UYGULAMA: 1-50 arasında 5 adet rastgele sayı üretip göster adındaki butona tıklandığında değerleri label'a yazdır, değerleri saydamlaştır adındaki buton da içersin

import tkinter as tk
import random as rd

form=tk.Tk()
form.title('Uygulama')
form.geometry('500x400+500+350')
liste=[]
for i in range(5):
    while len(liste) !=6:
        a=rd.randint(1,50)
        if a not in liste:
            liste.append(a)

def göster():
    label.config(text=liste,bg='green')
def saydamlaştır():
    form.wm_attributes('-alpha',0.3)
def döndür():
    form.wm_attributes('-alpha',0.9)

def MaxYap():
    form.state('zoomed')
def MinYap():
    form.state('iconic')
    
label=tk.Label(form,fg='red',bg='red',font='Times 20 bold') #değişecek
label.pack() 

göster=tk.Button(form,text='göster',fg='black',bg='yellow',command=göster)
göster.pack()
göster=tk.Button(form,text='saydamlaştır',fg='black',bg='yellow',command=saydamlaştır)
göster.pack(side=tk.LEFT)
göster=tk.Button(form,text='döndür',fg='black',bg='yellow',command=döndür)
göster.pack(side=tk.LEFT)
        
göster=tk.Button(form,text='MaxYap',fg='black',bg='yellow',command=saydamlaştır)
göster.pack(side=tk.RIGHT)
göster=tk.Button(form,text='MinYap',fg='black',bg='yellow',command=döndür)
göster.pack(side=tk.RIGHT)

















form.mainloop()