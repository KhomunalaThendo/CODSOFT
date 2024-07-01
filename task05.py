import customtkinter
import tkinter as tk
from tkinter import ttk
import json
import os

root = customtkinter.CTk()
root.title("Contact Book")
root.geometry("1150x550")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

contacts_file = "mycontacts.json"

def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            return json.load(file)
    return []

def save_contacts():
    with open(contacts_file, "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

def add_contacts():
    name_val = names.get()
    number_val = phone_number.get()
    email_val = email.get()
    address_val = address.get()

    table.insert('', 'end', values=(name_val, number_val, email_val, address_val))
    contacts.append({'name': name_val, 'number': number_val, 'email': email_val, 'address': address_val})

    names.delete(0, 'end')
    phone_number.delete(0, 'end')
    email.delete(0, 'end')
    address.delete(0, 'end')

    save_contacts()

def delete_contacts():
    selected_items = table.selection() 

    if selected_items:
        for item in selected_items:
            values = table.item(item, 'values')
            
            contacts[:] = [contact for contact in contacts if contact['name'] != values[0] or contact['number'] != values[1] or contact['email'] != values[2] or contact['address'] != values[3]]
            table.delete(item)
        
        save_contacts() 

def edit_contacts():
    selected_item = table.selection()
    if selected_item:
        item = table.item(selected_item)
        values = item['values']

        names.delete(0, 'end')
        names.insert(0, values[0])
        phone_number.delete(0, 'end')
        phone_number.insert(0, values[1])
        email.delete(0, 'end')
        email.insert(0, values[2])
        address.delete(0, 'end')
        address.insert(0, values[3])

        table.delete(selected_item)

        contacts[:] = [contact for contact in contacts if contact['name'] != values[0] or contact['number'] != values[1] or contact['email'] != values[2] or contact['address'] != values[3]]

        save_contacts()



left_frame = customtkinter.CTkFrame(master=root, width=300, height=400)
left_frame.pack(side="left", fill="y", padx=10, pady=10)
left_frame.pack_propagate(False)

right_frame = customtkinter.CTkFrame(master=root, width=1050, height=400)
right_frame.pack(side="right", fill="y", padx=10, pady=10)
right_frame.pack_propagate(False)

heading_lbl = customtkinter.CTkLabel(master=right_frame, text="CONTACTS")
heading_lbl.pack(pady=10)

headlbl = customtkinter.CTkLabel(master=left_frame, text="FullNames")
headlbl.pack(padx=15)

names = customtkinter.CTkEntry(master=left_frame, placeholder_text="FullNames")
names.pack(pady=10)

phone_numberlbl = customtkinter.CTkLabel(master=left_frame, text="Phone Number")
phone_numberlbl.pack(padx=15)

phone_number = customtkinter.CTkEntry(master=left_frame, placeholder_text="Phone Number")
phone_number.pack(pady=10)

emaillbl = customtkinter.CTkLabel(master=left_frame, text="Email Address")
emaillbl.pack(padx=15)

email = customtkinter.CTkEntry(master=left_frame, placeholder_text="Email Address")
email.pack(pady=10)

addresslbl = customtkinter.CTkLabel(master=left_frame, text="Address")
addresslbl.pack(padx=15)

address = customtkinter.CTkEntry(master=left_frame, placeholder_text="Address")
address.pack(pady=10)

addbtn = customtkinter.CTkButton(master=left_frame, text="ADD", command=add_contacts)
addbtn.pack(pady=20)

table = ttk.Treeview(right_frame, columns=('name', 'number', 'email', 'address'), show="headings")
table.heading('name', text="FullNames")
table.heading('number', text="Phone Number")
table.heading('email', text="Email Address")
table.heading('address', text="Address")
table.pack(fill="both", expand=True)

btnframe = customtkinter.CTkFrame(master= right_frame)
btnframe.pack(pady=10)

deletebtn = customtkinter.CTkButton(master=btnframe, text="REMOVE", command=delete_contacts)
deletebtn.grid(row=0, column=1, padx=5)

editbtn = customtkinter.CTkButton(master=btnframe, text="EDIT", command=edit_contacts)
editbtn.grid(row=0, column=2, padx=5)

for contact in contacts:
    table.insert('', 'end', values=(contact['name'], contact['number'], contact['email'], contact['address']))

root.mainloop()
 