import tkinter as tk
form=tk.Tk()
form.title('Ders 5')
form.geometry('500x400')
def topla():
    print('topla')

buton=tk.Button(form,text='Tıkla',fg='black',bg='red',command=topla)
buton.pack(side=tk.LEFT)
buton2=tk.Button(form,text='tıkla2',command=topla)
buton2.pack(side=tk.RIGHT)

form.mainloop()