import tkinter as tk
from tkinter import messagebox #tk içine çağırmak 'şart'

form=tk.Tk()
form.geometry('500x500')
form.title('Messagebox')
def mesaj():
    messagebox.showinfo(title='mesaj1',message='Lütfen mesaja riayet edelim!')
    messagebox.asketrycancel(title='mesaj2',message='Lütfen et artık!') #yeniden dene ve iptal
    messagebox.askyesno(title='mesaj3',message='ARTIK!')
    messagebox.askquestion(title='mesaj4',message='tkinter messagebox son!')
buton=tk.Button(form,text='tıkla mesaj gelsin',command=mesaj).pack() #paketleme bu şekilde de yapılabilir

form.mainloop()
    
#İLK MESAJDAN SONRASI GELMİYOR, TEKRAR İNCELE