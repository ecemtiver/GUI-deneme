import tkinter as tk

form=tk.Tk() #nesne oluşturmak için form kullanır
form.title('Tkinter Dersleri Formu')
label=tk.Label(form,text='Python Tkinter')
label.pack()
label2=tk.Label(form,text='Ders-2-' ,fg='red')
label2.pack()
label3=tk.Label(form,text='Ders-2- arkaplan', fg='black', bg='green')
label3.pack()
label4=tk.Label(form,text='yeni label', fg='red', bg='blue', font='Times 15 italic')
label4.pack()
label5=tk.Label(form,text='En son label', fg='green', bg='red', fon='Times 17 bold')
label5.pack()

form.mainloop()