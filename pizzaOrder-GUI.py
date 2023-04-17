import tkinter as tk
from tkinter import messagebox


form = tk.Tk()
form.title('Pizza Sipariş Uygulaması')
form.geometry("720x720")


def calculate_price():
    pizza_price = pizza_var.get()
    sos_price = sos_zeytin_var.get() + sos_mantar_var.get() + sos_kecipeynir_var.get() + sos_et_var.get() + sos_sogan_var.get() + sos_misir_var.get()
    total_price = pizza_price + sos_price
    fiyat_label.config(text=f'Toplam Fiyat: {total_price} TL')
    
# def description():
#     pizza_name = pizza_klasik_button['text']
#     sos_names = sos_zeytin_button['text'] + sos_mantar_button['text'] + sos_kecipeynir_button['text'] + sos_et_button['text'] + sos_sogan_button['text'] + sos_misir_button['text']
#     full_names = pizza_name + sos_names
#     description_label.config(text=f'Alınan ürün : {full_names}')

def siparisOnayla():
    messagebox.showinfo("Ödeme Onayı", "Siparişiniz onaylandı, Afiyet olsun...") 
    # .csv dosyasına yazmaya bak.
    # Pizza boyutu ekle
    

def siparisVer():
    if pizza_var.get() != 0 :
        messagebox.showinfo("Ödeme Sayfası", "Ödeme sayfasına yönlendiriliyorsunuz...")
        form2 = tk.Toplevel()
        form2.title("Ödeme Sayfası")
        form2.geometry("720x720")
        hosgeldin_label = tk.Label(form2, text='Bilgileriniz 3D secure ile korunmaktadır.', bg="yellow" , fg='red', font='Times 28 italic')
        hosgeldin_label.pack()
        
        isim_entry_value = tk.StringVar()
        tc_entry_value = tk.StringVar()
        card_entry_value = tk.StringVar()
        passw_entry_value = tk.StringVar()
        
        
        isim_label = tk.Label(form2, text="İsminiz : " , fg='blue' , bg='green', font='Times 20')
        isim_label.place(relx = 0.05 , rely= 0.1)
        
        isim_entry = tk.Entry(form2, textvariable= isim_entry_value , font='Times 18')
        isim_entry.place(relx= 0.25, rely= 0.1)
        
        
        tc_label = tk.Label(form2, text="Tc Kimlik : " , fg='blue' , bg='green', font='Times 20')
        tc_label.place(relx = 0.05 , rely= 0.2)
        
        tc_entry = tk.Entry(form2, textvariable= tc_entry_value , font='Times 18')
        tc_entry.place(relx= 0.25, rely= 0.2)
        
        
        card_label = tk.Label(form2, text="Card No : " , fg='blue' , bg='green', font='Times 20')
        card_label.place(relx = 0.05 , rely= 0.3)
        
        card_entry = tk.Entry(form2, textvariable= card_entry_value , font='Times 18')
        card_entry.place(relx= 0.25, rely= 0.3)
        
        
        passw_label = tk.Label(form2, text="Card Password : " , fg='blue' , bg='green', font='Times 20')
        passw_label.place(relx = 0.05 , rely= 0.4)
        
        passw_entry = tk.Entry(form2, textvariable= passw_entry_value , font='Times 18')
        passw_entry.place(relx= 0.25, rely= 0.4)
        
        
        bilgi_onayla_button = tk.Button(form2, text='Siparişi onayla' , fg='green',bg='purple',activebackground='green',font='Times 18', command=siparisOnayla)
        bilgi_onayla_button.place(relx=0.25, rely=0.5)
        
        
        form2.mainloop()
    else:
        messagebox.showinfo('Uyarı',"Lütfen almak istediğiniz pizzayı seçin.")
    
    
    



hosgeldin_label = tk.Label(form, text='Pizza Sipariş Uygulamasına Hoş geldiniz', bg="yellow" , fg='red', font='Times 28 italic')
hosgeldin_label.place(relx = 0.5 , rely = 0.02, anchor='center')
menu_label = tk.Label(form, text='Menü' , font = 'Times 22' , fg='black' , bg='green')
menu_label.place(relx=0.5, rely=0.06)

pizza_label = tk.Label(form, text='Pizzalar', font='Times 20 bold')
pizza_label.place(relx=0.1, rely=0.11)
sos_label = tk.Label(form, text='Soslar', font='Times 20 bold')
sos_label.place(relx=0.75, rely=0.11)

pizza_var = tk.IntVar(value=0)
sos_zeytin_var = tk.IntVar(value=0)
sos_mantar_var = tk.IntVar(value=0)
sos_kecipeynir_var = tk.IntVar(value=0)
sos_et_var = tk.IntVar(value=0)
sos_sogan_var = tk.IntVar(value=0)
sos_misir_var = tk.IntVar(value=0)


pizza_klasik_button = tk.Radiobutton(form, text='Klasik Pizza' , fg='blue' , bg='pink' , activebackground='green', font='Times 16', variable=pizza_var, value=40)
pizza_klasik_button.place(relx=0.1, rely=0.17)
pizza_margarita_button = tk.Radiobutton(form, text='Margarita Pizza' , fg='blue' , bg='pink' , activebackground='green', font='Times 16', variable=pizza_var, value=50)
pizza_margarita_button.place(relx=0.1, rely=0.22)
pizza_Turk_button = tk.Radiobutton(form, text='Turk Pizza' , fg='blue' , bg='pink' , activebackground='green', font='Times 16', variable=pizza_var, value=45)
pizza_Turk_button.place(relx=0.1, rely=0.27)
pizza_sade_button = tk.Radiobutton(form, text='Sade Pizza' , fg='blue' , bg='pink' , activebackground='green', font='Times 16', variable=pizza_var, value=48)
pizza_sade_button.place(relx=0.1, rely=0.32)


sos_zeytin_button = tk.Checkbutton(form, text='Zeytin' , fg='blue' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_zeytin_var, onvalue=4, offvalue=0)
sos_zeytin_button.place(relx=0.75, rely=0.17)
sos_mantar_button = tk.Checkbutton(form, text='Mantar' , fg='blue' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_mantar_var, onvalue=5, offvalue=0)
sos_mantar_button.place(relx=0.75, rely=0.22)
sos_kecipeynir_button = tk.Checkbutton(form, text='Keci peyniri' , fg='blue' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_kecipeynir_var, onvalue=7, offvalue=0)
sos_kecipeynir_button.place(relx=0.75, rely=0.27)
sos_et_button = tk.Checkbutton(form, text='Et' , fg='blue' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_et_var, onvalue=12, offvalue=0)
sos_et_button.place(relx=0.75, rely=0.32)
sos_sogan_button = tk.Checkbutton(form, text='Sogan' , fg='blue' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_sogan_var, onvalue=2, offvalue=0)
sos_sogan_button.place(relx=0.75, rely=0.37)
sos_misir_button = tk.Checkbutton(form, text='Misir' , fg='blue' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_misir_var, onvalue=3, offvalue=0)
sos_misir_button.place(relx=0.75, rely=0.42)


# calculate_button = tk.Button(form, text='Fiyat Hesapla' , fg='red',bg='blue',activebackground='green',font='Times 18', command=lambda : (calculate_price(), description()))
calculate_button = tk.Button(form, text='Fiyat Hesapla' , fg='red',bg='blue',activebackground='green',font='Times 18', command=calculate_price)
calculate_button.place(relx=0.45, rely=0.45)
fiyat_label = tk.Label(form,text='0 TL' ,fg='purple', bg='green' , font="Times 16")
fiyat_label.place(relx=0.45, rely=0.52)
# description_label = tk.Label(form,text='Henüz bir şey seçmediniz' ,fg='purple', bg='green' , font="Times 16")
# description_label.place(relx=0.45,rely=0.55)
onayla_button = tk.Button(form, text='Sipariş ver' , fg='yellow',bg='purple',activebackground='green',font='Times 18', command=siparisVer)
onayla_button.place(relx=0.45, rely=0.57)


form.mainloop()
