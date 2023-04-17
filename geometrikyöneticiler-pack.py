import tkinter as tk

form=tk.Tk()
form.geometry('500x500')
label=tk.Label(text='Geometrik Yöneticiler')
label.pack(side=tk.TOP)
buton=tk.Button(text='Pack()',bg='red')
buton.pack(side=tk.BOTTOM,fill=tk.y,expand=tk.YES) #yekseni #YES yerine 1 de yazılabilir

#buton.pack(expand=1,anchor='s)
#n:yukarı, s:aşağı, e:sağ, w:sol
#ne:yukarı sağ, nw:yukarı sol, se:aşağı sağ, sw:aşağı sol
#buton.pack(padx=20,pady=50) kenarlardan istediğin oranda uzaklaştır
#buton.pack(ipadx=20,ipady=50) buton boyutu değiştir


form.mainloop()
