from tkinter import *
from PIL import ImageTk, Image
from datetime import *
from tkinter import messagebox

window = Tk()
window.title("Lotto Login")
window.geometry("700x800")
window.config(bg="Yellow")

canvas = Canvas(window, width=500, height=300, bg="Yellow", borderwidth=0, highlightthickness=0)
canvas.place(x=90, y=20)
img = ImageTk.PhotoImage(Image.open('17-Lottery1.jpg'))
canvas.create_image(20, 20, anchor=NW, image=img)


def age_calculation(self):
    date_time = datetime.today
    try:
        for x in range(int(self.id_entry.get())):
            age = int(self.id_entry.get()[0:3]) - int(date_time.strftime("%y"))
            if age >= 18:
                messagebox.showinfo('Status', "You are Old enough to Play Lotto!!")
                import main2
                window.destroy()
                break
            elif len(self.id_entry.get()) < 13:
                messagebox.showerror('Error', 'Not a valid ID Number')
            elif len(self.id_entry.get()) > 13:
                messagebox.showerror('Error', 'This is not a valid ID Number')
            else:
                messagebox.showerror('Error', 'You are too young to play Lotto')
                break
    except ValueError:
        if self.id_entry.get() != int:
            messagebox.showerror('Error', 'The ID number must be an integer')


label1 = Label(window, text="Ithuba National Lottery", font=("Comic Sans MS", 20), bg='Yellow')
label1.place(x=240, y=5)

frame = Frame(window, width=500, height=400, relief='raised', bg='#42f5a7')
frame.place(x=100, y=350)

top = Label(frame, text='Please enter your details Below', bg='#42f5a7')
top.place(x=140, y=5)

name = Label(frame, text="Name & Surname:", bg='#42f5a7')
name.place(x=10, y=50)
name_entry = Entry(frame)
name_entry.place(x=200, y=50)

email = Label(frame, text="Email Address:", bg='#42f5a7')
email.place(x=10, y=100)
email_entry = Entry(frame)
email_entry.place(x=200, y=100)

address = Label(frame, text='Postal Address:', bg='#42f5a7')
address.place(x=10, y=150)
address_entry = Entry(frame, width=35)
address_entry.place(x=200, y=150)

identity = Label(frame, text='ID Number:', bg='#42f5a7')
identity.place(x=10, y=200)
identity_entry = Entry(frame)
identity_entry.place(x=200, y=200)

submit = Button(frame, text='Enter', bg='yellow', width=20, command=age_calculation)
submit.place(x=305, y=350)


def clear_fields():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    identity_entry.delete(0, END)


clear = Button(frame, text='Clear', bg='yellow', width=20, command=clear_fields)
clear.place(x=5, y=350)


def exit_program():
    window.destroy()


exit_btn = Button(window, text='Exit', width=10, bg='black', fg='red', command=exit_program)
exit_btn.place(x=580, y=760)
window.mainloop()
