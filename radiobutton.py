import tkinter as tk

form=tk.Tk()
form.geometry('500x450')
def kontrol():
    if x.get()=='1':
        print('buton1')
    elif x.get()=='2':
        print()
    else:
        print('buton2 and buton1')
#radiobuttonlarımızı kullanabilmek için önce button eklenir
buton=tk.Button(form,text='tıla',fg='black',bg='red',activebackground='green',command=kontrol)
buton.pack()

x=tk.StringVar()

radio=tk.Radiobutton(form,text='radio1',activebackground='red',value='1',variable=x)
radio.pack()

radio2=tk.Radiobutton(form,text='radio2',activebackground='green',value='2',variable=x)
radio2.pack()