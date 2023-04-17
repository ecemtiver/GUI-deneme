import tkinter as tk
from tkinter import messagebox


form = tk.Tk()
form.title('Pizza Sipariş Uygulaması')
form.geometry("690x670+400+90")
form.minsize(690,690)
form.maxsize(690,690)
#form.resizable(False,True) Ekran boyutunda oynama yap/yapma, true değeri için 1 girilebilir


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
        form2.geometry("690x670+400+90")
        hosgeldin_label = tk.Label(form2, text='*Bilgileriniz 3D secure ile korunmaktadır*', bg="red" , fg='white', font='Times 28 italic')
        hosgeldin_label.pack()
        
        isim_entry_value = tk.StringVar()
        tc_entry_value = tk.StringVar()
        card_entry_value = tk.StringVar()
        passw_entry_value = tk.StringVar()
        
        
        isim_label = tk.Label(form2, text="Ad Soyad : " , fg='blue' , bg='pink', font='Times 20')
        isim_label.place(relx = 0.05 , rely= 0.1)
        
        isim_entry = tk.Entry(form2, textvariable= isim_entry_value , font='Times 18')
        isim_entry.place(relx= 0.52, rely= 0.1)
        
        
        adres_label = tk.Label(form2, text="TC Kimlik : " , fg='blue' , bg='pink', font='Times 20')
        adres_label.place(relx = 0.05 , rely= 0.2)
        
        tc_entry = tk.Entry(form2, textvariable= tc_entry_value , font='Times 18')
        tc_entry.place(relx= 0.52, rely= 0.2)
        
        
        card_label = tk.Label(form2, text="Kart Numarası : " , fg='blue' , bg='pink', font='Times 20')
        card_label.place(relx = 0.05 , rely= 0.3)
        
        card_entry = tk.Entry(form2, textvariable= card_entry_value , font='Times 18')
        card_entry.place(relx= 0.52, rely= 0.3)
        
        
        passw_label = tk.Label(form2, text="Kart Şifresi : " , fg='blue' , bg='pink', font='Times 20')
        passw_label.place(relx = 0.05 , rely= 0.4)

        passw_entry = tk.Entry(form2, textvariable= passw_entry_value , font='Times 18',show='*')
        passw_entry.place(relx= 0.52, rely= 0.4)
        
        bilgi_onayla_button = tk.Button(form2, text='İptal et' , fg='white',bg='red',activebackground='green',font='Times 18 italic bold', command=siparisOnayla)
        bilgi_onayla_button.place(relx=0.52, rely=0.60)
        
        bilgi_onayla_button = tk.Button(form2, text='Siparişi onayla' , fg='white',bg='green',activebackground='green',font='Times 18 italic bold', command=siparisOnayla)
        bilgi_onayla_button.place(relx=0.52, rely=0.50)
        
     
        
        form2.mainloop()
    else:
        messagebox.showinfo('Uyarı',"Lütfen almak istediğiniz pizzayı seçin.")
    
    
    



hosgeldin_label = tk.Label(form, text='~Pizza Sipariş Uygulamasına Hoş Geldiniz~', bg="purple" , fg='white', font='Times 28 bold')
hosgeldin_label.place(relx = 0.5 , rely = 0.02, anchor='center')
menu_label = tk.Label(form, text='~Menü~' , font = 'Times 20 bold' , fg='white' , bg='green')
menu_label.place(relx=0.45, rely=0.06)

pizza_label = tk.Label(form, text='Pizzalar', font='Times 20 bold italic')
pizza_label.place(relx=0.1, rely=0.11)
sos_label = tk.Label(form, text='Ek Malzemeler', font='Times 20 bold italic')
sos_label.place(relx=0.73, rely=0.11)

pizza_var = tk.IntVar(value=0)
sos_zeytin_var = tk.IntVar(value=0)
sos_mantar_var = tk.IntVar(value=0)
sos_kecipeynir_var = tk.IntVar(value=0)
sos_et_var = tk.IntVar(value=0)
sos_sogan_var = tk.IntVar(value=0)
sos_misir_var = tk.IntVar(value=0)


pizza_klasik_button = tk.Radiobutton(form, text='Klasik Pizza' , fg='black' , bg='pink' , activebackground='green', font='Times 16', variable=pizza_var, value=40)
pizza_klasik_button.place(relx=0.1, rely=0.17)
pizza_margarita_button = tk.Radiobutton(form, text='Margarita Pizza' , fg='black' , activebackground='green', font='Times 16', variable=pizza_var, value=50)
pizza_margarita_button.place(relx=0.1, rely=0.22)
pizza_Turk_button = tk.Radiobutton(form, text='Turk Pizza' , fg='black' , bg='pink' , activebackground='green', font='Times 16', variable=pizza_var, value=45)
pizza_Turk_button.place(relx=0.1, rely=0.27)
pizza_sade_button = tk.Radiobutton(form, text='Sade Pizza' , fg='black' , activebackground='green', font='Times 16', variable=pizza_var, value=48)
pizza_sade_button.place(relx=0.1, rely=0.32)


sos_zeytin_button = tk.Checkbutton(form, text='Zeytin' , fg='black' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_zeytin_var, onvalue=4, offvalue=0)
sos_zeytin_button.place(relx=0.73, rely=0.17)
sos_mantar_button = tk.Checkbutton(form, text='Mantar' , fg='black' , activebackground='green', font='Times 16' , variable=sos_mantar_var, onvalue=5, offvalue=0)
sos_mantar_button.place(relx=0.73, rely=0.22)
sos_kecipeynir_button = tk.Checkbutton(form, text='Keci peyniri' , fg='black' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_kecipeynir_var, onvalue=7, offvalue=0)
sos_kecipeynir_button.place(relx=0.73, rely=0.27)
sos_et_button = tk.Checkbutton(form, text='Et' , fg='black' , activebackground='green', font='Times 16' , variable=sos_et_var, onvalue=12, offvalue=0)
sos_et_button.place(relx=0.73, rely=0.32)
sos_sogan_button = tk.Checkbutton(form, text='Sogan' , fg='black' , bg='pink' , activebackground='green', font='Times 16' , variable=sos_sogan_var, onvalue=2, offvalue=0)
sos_sogan_button.place(relx=0.73, rely=0.37)
sos_misir_button = tk.Checkbutton(form, text='Misir' , fg='black' , activebackground='green', font='Times 16' , variable=sos_misir_var, onvalue=3, offvalue=0)
sos_misir_button.place(relx=0.73, rely=0.42)


# calculate_button = tk.Button(form, text='Fiyat Hesapla' , fg='red',bg='blue',activebackground='green',font='Times 18', command=lambda : (calculate_price(), description()))
calculate_button = tk.Button(form, text='Fiyat Hesapla' , fg='white',bg='green',activebackground='green',font='Times 18 bold italic', command=calculate_price)
calculate_button.place(relx=0.20, rely=0.60)
fiyat_label = tk.Label(form,text='0 tl' ,fg='white', bg='green' , font="Times 16 bold italic")
fiyat_label.place(relx=0.20, rely=0.70)
# description_label = tk.Label(form,text='Henüz bir şey seçmediniz' ,fg='purple', bg='green' , font="Times 16")
# description_label.place(relx=0.45,rely=0.55)
onayla_button = tk.Button(form, text='Sipariş ver' , fg='white',bg='green',activebackground='green',font='Times 18 bold italic', command=siparisVer)
onayla_button.place(relx=0.65, rely=0.60)

onayla_button = tk.Button(form, text='Çıkış' , fg='white',bg='red',activebackground='green',font='Times 18 bold italic', command=siparisVer)
onayla_button.place(relx=0.65, rely=0.70)

form.mainloop()