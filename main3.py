import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

import requests
from playsound import playsound

window = Tk()
window.title('Claim Prize')
window.geometry('500x600')
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

amount = IntVar()
response = requests.get('https://v6.exchangerate-api.com/v6/8c633d337bbc46fc80ef7fa7/latest/ZAR')
response_j = response.json()

conv_rates = response_j['conversion_rates']

curr_options = []
for i in conv_rates.keys():
    curr_options.append(i)

currency_combo = Combobox(window)
currency_combo['values'] = curr_options
currency_combo['state'] = 'readonly'
currency_combo.set('Select foreign currency')
currency_combo.place(x=5, y=360)


def currency_convert():
    number = float(winnings_entry.get())
    messagebox.showinfo("money", response_j['conversion_rates'][currency_combo.get()])
    answer = number * response_j['conversion_rates'][currency_combo.get()]
    convert_result['text'] = answer


winnings = Label(window, text='Enter Amount Won', bg='yellow')
winnings.place(x=5, y=300)
winnings_entry = Entry(window)
winnings_entry.place(x=300, y=300)
convert_result = Label(window, text='Result after conversion: ', bg='yellow')
convert_result.place(x=5, y=420)

convert_zar = Button(window, text='Convert amount', command=currency_convert)
convert_zar.place(x=300, y=360)


def exit_program():
    playsound('87637918.mp3')
    window.destroy()


exit_btn = Button(window, text='exit', bg='red', command=exit_program)
exit_btn.place(x=440, y=560)

window.mainloop()
