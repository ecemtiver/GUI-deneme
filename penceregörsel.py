import tkinter as tk

form=tk.Tk()
form.geometry('500x500+350+250')
form.title('Ders 4')

form.state('normal')
#form.state('zoomed') #tam ekran
#form.state('iconic')
form.wm_attributes('-alpha', 0.3) #saydam

form.mainloop()