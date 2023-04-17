import tkinter as tk

form=tk.Tk()
form.title('Tkinter Dersleri ders-3')
form.geometry('500x250+500+350')
form.minsize(450,400)
form.maxsize(550,550)

label=tk.Label(form,text='Ders-3-')
label.pack()

form.mainloop()