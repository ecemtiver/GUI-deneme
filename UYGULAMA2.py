#UYGULAMA:mail,şifre,kaydol,giriş,ad soyad,şifre

import tkinter as tk
form=tk.Tk()
form.title('Uygulama-2')
form.geometry('500x300')
mail=tk.Label(text='mail:',fg='black',bg='blue',font='Times 10 bold')
mail.place(x=10,y=30)
şifre=tk.Label(text='şifre:',fg='black',bg='blue',font='Times 10 bold')
şifre.place(x=10,y=60)

mail_entr=tk.Entry()
mail_entr.place(x=50,y=30)
şifre_entr=tk.Entry(show='*')
şifre_entr.place(x=50,y=62)

def kayıtol():
    mail=tk.Label(text='mail:',fg='black',bg='blue',font='Times 10 bold')
    mail.place(x=10,y=150)
    şifre=tk.Label(text='şifre:',fg='black',bg='blue',font='Times 10 bold')
    şifre.place(x=10,y=180)
    ad=tk.Label(text='ad:',fg='black',bg='blue',font='Times 10 bold')
    şifre.place(x=10,y=120)
    mail_entr=tk.Entry()
    mail_entr.place(x=50,y=150)
    şifre=tk.Entry(show='*')
    şifre.place(x=50,y=180)
    ad=tk.Entry()
    ad.place(x=50,y=120)
    
def giriş():
    mail_entr.delete(0,'end')
    şifre_entr.delete(0,'end')
kayıtol_btn=tk.Button(form,text='Kayıt ol', fg='black',bg='green',command=kayıtol)
kayıtol_btn.place(x=45,y=90)

giriş_btn=tk.Button(form,text='Giriş', fg='black',bg='green',command=giriş)
giriş_btn.place(x=120,y=90)
form.mainloop()
