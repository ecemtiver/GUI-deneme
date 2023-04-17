import tkinter as tk

form=tk.Tk()
form.title('Place')
form.geometry('500x450+250+250')
buton=tk.Button(text='Deneme',fg='red',bg='green',font='Times 17 bold')
#buton.place(x=150,y=140)
buton.place(relx=150,rely=140) #buton pencereyle hareket eder
#buton.place(width=150,heigh=140)




form.mainloop()