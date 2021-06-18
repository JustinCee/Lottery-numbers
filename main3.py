import tkinter
from tkinter import *

window = Tk()
window.title('Claim Prize')
window.geometry('500x500')
window.config(bg='yellow')

top_label = Label(window, text='Please enter your details below:', bg='yellow', font=("Comic Sans MS", 20))
top_label.place(x=100, y=5)

holder_name = Label(window, text='Account Holder Name & Surname:', bg='yellow')
holder_name.place(x=5, y=70)
holder_name_entry = Entry(window)
holder_name_entry.place(x=300, y=70)

acc_number = Label(window, text='Enter your Account Number:', bg='yellow')
acc_number.place(x=5, y=140)
acc_number_entry = Entry(window)
acc_number_entry.place(x=300, y=140)

options_list = ['Standard Bank', 'FNB', 'ABSA', 'Capitec']
value_inside = tkinter.StringVar(window)
value_inside.set("Select your bank")
bank_menu = tkinter.OptionMenu(window, value_inside, *options_list)
bank_menu.pack()
bank_menu.place(x=300, y=210)
bank_option = Label(window, text='Please select your bank:', bg='yellow')
bank_option.place(x=5, y=210)



window.mainloop()
