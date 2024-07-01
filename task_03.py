#Password generator
import customtkinter
import random

root = customtkinter.CTk()
root.title('Password Generator')
root.geometry('400x300')

customtkinter.set_appearance_mode('default')
customtkinter.set_default_color_theme('green')

def generate_pass():

    pass_characters = "abcdefghijklmnopqrstuvw@#$&%*"
    length = int(length_entry.get())

    passgen = ''.join(random.choice(pass_characters) for _ in range(length))
    password_result.configure(text= f'{passgen}')


lengthlbl = customtkinter.CTkLabel(master= root, text='Enter length of password')
lengthlbl.pack(pady = 15)

length_entry = customtkinter.CTkEntry(root, placeholder_text= 'Enter length')
length_entry.pack(pady = 10)

enterbtn = customtkinter.CTkButton(root, text='Enter', command= generate_pass)
enterbtn.pack(pady = 15)

password_result = customtkinter.CTkLabel(root, text= 'Password: ')
password_result.pack(pady = 10)

password_result = customtkinter.CTkLabel(root, text='')
password_result.pack(pady = 10)

root.mainloop()