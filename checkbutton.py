import tkinter as tk

form=tk.Tk()

form.title('Checkbutton')
form.geometry('500x500')
x=tk.IntVar() #tk içinden IntVar alacağım ve set edeceğim bu integer variables ile
x.set(0) #checkbutton ekrana ilk geldiğinde seçili olup olmayacağı ile ilişkili
def kontrol():
    if x.get()==0:
        print('Onaylanmadı')
    else:
        print('Onaylandı')
    
check=tk.Checkbutton(form,text='onay',fg='pink',bg='green',variable=x,command=kontrol)
#oluşturacağımız checkbutton bir değer döndürecek
check.pack()

form.mainloop()