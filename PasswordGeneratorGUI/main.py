import random
from tkinter import *
from tkinter import messagebox
# Password Generator
def generate_password():
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    rakamlar = ["1","2","3","4","5","6","7","8","9"]
    ozelKarakterler = ["!","&","/","#","=","$","(",")"]

    harfSayisi = random.randint(8,10)
    rakamSayisi = random.randint(2,4)
    ozelKarakterSayisi = random.randint(2,4)

    sifreHarfleri = [random.choice(alfabe) for i in range(harfSayisi)]
    sifreRakamlari = [random.choice(rakamlar) for i in range(rakamSayisi)]
    sifreOzelKarakterleri = [random.choice(ozelKarakterler) for i in range(ozelKarakterSayisi)]

    sifreListesi = sifreHarfleri+sifreRakamlari+sifreOzelKarakterleri
    random.shuffle(sifreListesi)

    # tüm liste elemanlarını boşluksuz bir şekilde birleştirecek
    password = "".join(sifreListesi)

    password_entry.insert(0,password)



# Şifreyi Kaydet
def save():
    website= website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(email) > 0 and len(password) > 0:
        is_okey = messagebox.askyesno(title=website,message=f"Bilgileriniz detayları\nEmail: {email}\nPassword: {password}")
        if is_okey==True:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)
    else:
        messagebox.showinfo(title="OOPPS",message="Tüm Alanları Doldurun.")

# Kullanıcı Arayüzü
window = Tk()
window.title("Password Generator")
window.config(padx=100, pady=100)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)


web_site_label = Label(text="Website")
web_site_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

# kullanıcı girişi
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0,"davut1234qq@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)


# button
generate_password_button = Button(text="Generate Password",width=35,command=generate_password)
generate_password_button.grid(row=4,column=1)
add_button = Button(text="Add",width=35, command=save)
add_button.grid(row=5,column=1,columnspan=2)







window.mainloop()