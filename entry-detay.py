import tkinter as tk

form=tk.Tk()
form.title('Entry')
form.geometry('500x300')

entry=tk.Entry()
entry.pack()

def verial():
    etiket['text']=entry.get() #get fonksiyoonu ile entry içindeki yazıyı alır
def sil():
    entry.delete(0,'end') #class 0'dan başlar, sona kadar gider
    entry.delete(2,'end')
entry2=tk.Entry(show='*')
entry2.pack()

buton=tk.Button(text='verileri al',fg='red',bg='green',command=verial)
buton.pack
buton=tk.Button(text='sil',fg='red',bg='green',command=sil)
buton.pack

etiket=tk.Label(text='veriler buraya getirilmeli')
etiket.pack()


form.mainloop()