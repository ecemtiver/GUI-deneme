import tkinter as tk

form=tk.Tk() #tkinter içindeki Tk sınıfını çağır
form.title('Tkinter Dersleri-1') #başlık tk idi
etiket=tk.Label(text='Tkinter Python')
etiket.pack() #etiketimizi paketlemezsek yenileri form üzerinde görünmez
etiket2=tk.Label(form,text='Python Tkinter Dersleri' #form nesnesinin üzerinde konumlandı
etiket2.pack()

form.mainloop()