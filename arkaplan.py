import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import combobox

form=tk.Tk()
form.geometry('500x500')
form.title('Pizza Sipariş Sistemi')
resim=ImageTk.PhotoImage(Image.open(C:/Users/etive/OneDrive/Masaüstü//form_back.jpg))
label=tk.Label(form,image=resim)

form.mainloop()