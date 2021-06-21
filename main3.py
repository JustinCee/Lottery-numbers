# below is the modules that i needed to import
import smtplib
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import requests
from playsound import playsound

# below is the configuration of the tkinter window
window = Tk()
window.title('Claim Prize')
window.geometry('500x600')
window.config(bg='yellow')
# below is the top label
top_label = Label(window, text='Please enter your details below:', bg='yellow', font=("Comic Sans MS", 20))
top_label.place(x=100, y=5)
# below is the label and entry for the account holder name
holder_name = Label(window, text='Account Holder Name & Surname:', bg='yellow')
holder_name.place(x=5, y=70)
holder_name_entry = Entry(window)
holder_name_entry.place(x=300, y=70)
# below is the label and entry for account number
acc_number = Label(window, text='Enter your Account Number:', bg='yellow')
acc_number.place(x=5, y=140)
acc_number_entry = Entry(window)
acc_number_entry.place(x=300, y=140)
# below is the option list for you to pick who you bank wih
options_list = ['Standard Bank', 'FNB', 'ABSA', 'Capitec']
value_inside = tkinter.StringVar(window)
value_inside.set("Select your bank")
bank_menu = tkinter.OptionMenu(window, value_inside, *options_list)
bank_menu.pack()
bank_menu.place(x=300, y=210)
bank_option = Label(window, text='Please select your bank:', bg='yellow')
bank_option.place(x=5, y=210)
# below is the configuration of the API needed for the currency converter
amount = IntVar()
response = requests.get('https://v6.exchangerate-api.com/v6/8c633d337bbc46fc80ef7fa7/latest/ZAR')
response_j = response.json()

conv_rates = response_j['conversion_rates']

curr_options = []
for i in conv_rates.keys():
    curr_options.append(i)
# below is the information needed for you to pick what you want to convert to
currency_combo = Combobox(window)
currency_combo['values'] = curr_options
currency_combo['state'] = 'readonly'
currency_combo.set('Select foreign currency')
currency_combo.place(x=5, y=360)


# below is the function for the currency converter
def currency_convert():
    number = float(winnings_entry.get())
    messagebox.showinfo("money", response_j['conversion_rates'][currency_combo.get()])
    answer = number * response_j['conversion_rates'][currency_combo.get()]
    convert_result['text'] = answer


# below is the winnings displayed and the results after converting
winnings = Label(window, text='Enter Amount Won', bg='yellow')
winnings.place(x=5, y=300)
winnings_entry = Entry(window)
winnings_entry.place(x=300, y=300)
convert_result = Label(window, text='Result after conversion: ', bg='yellow')
convert_result.place(x=5, y=420)

convert_zar = Button(window, text='Convert amount', command=currency_convert)
convert_zar.place(x=300, y=360)


# below is the function needed to send the email
def email_sent():
    sender = 'pythondummy005@gmail.com'
    receiver = email_entry.get()

    message = """From: From Justin <pythondummy005@gmail.com>
    To: To Player
    Subject: Lotto Confirmation
    
    Good Day User,
    
    This Email confirms that you have played lotto and a winner
    """

    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.sendmail(sender, receiver, message)
        messagebox.showinfo('Status', 'Email being Sent')
    except smtplib.SMTPException:
        print("Unable to send email")


# below is the button, label and entry needed for the emails
email_send = Button(window, text='Send Email', command=email_sent)
email_send.place(x=5, y=560)
email_label = Label(window, text='Please enter your email address:', bg='yellow')
email_label.place(x=5, y=480)
email_entry = Entry(window)
email_entry.place(x=300, y=480)


# below is the exit program function
def exit_program():
    playsound('87637918.mp3')
    window.destroy()


# below is the exit button
exit_btn = Button(window, text='exit', bg='red', command=exit_program)
exit_btn.place(x=440, y=560)

window.mainloop()
