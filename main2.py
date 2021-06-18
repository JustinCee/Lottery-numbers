from itertools import chain
from random import sample
from tkinter import *

from PIL import ImageTk, Image

window = Tk()
window.title('Lets Play')
window.geometry('500x1000')
window.config(bg='yellow')

canvas = Canvas(window, width=400, height=200, bg="Yellow", borderwidth=0, highlightthickness=0)
canvas.place(x=115, y=10)
img = ImageTk.PhotoImage(Image.open('download.png'))
canvas.create_image(20, 20, anchor=NW, image=img)

top_label = Label(window, text='Do you feel Lucky?', font=("Comic Sans MS", 20), bg='yellow')
top_label.place(x=150, y=5)


def play_again():
    first_list.clear()
    second_list.clear()
    third_list.clear()
    lotto_list.clear()


play_twice = Button(window, text='Try Your Luck Again', bg='powder blue', command=play_again)
play_twice.place(x=170, y=700)

first_list = []
second_list = []
third_list = []


def button_display(num):
    if len(first_list) < 6:
        first_list.append(num)
        first_set.config(text=first_list)
    elif len(first_list) == 6 and len(second_list) < 6:
        second_list.append(num)
        second_set.config(text=second_list)
    elif len(first_list) == 6 and len(second_list) == 6 and len(third_list) < 6:
        third_list.append(num)
        third_set.config(text=third_list)


number_label = Label(window, text='Please select your numbers Below: ', font=("Comic Sans MS", 20), bg='yellow')
number_label.place(x=90, y=250)
number1 = Button(window, width=2, text=1, command=lambda: button_display(1))
number1.place(x=20, y=300)
number2 = Button(window, width=2, text=2, command=lambda: button_display(2))
number2.place(x=80, y=300)
number3 = Button(window, width=2, text=3, command=lambda: button_display(3))
number3.place(x=140, y=300)
number4 = Button(window, width=2, text=4, command=lambda: button_display(4))
number4.place(x=200, y=300)
number5 = Button(window, width=2, text=5, command=lambda: button_display(5))
number5.place(x=260, y=300)
number6 = Button(window, width=2, text=6, command=lambda: button_display(6))
number6.place(x=320, y=300)
number7 = Button(window, width=2, text=7, command=lambda: button_display(7))
number7.place(x=380, y=300)
number8 = Button(window, width=2, text=8, command=lambda: button_display(8))
number8.place(x=440, y=300)
number9 = Button(window, width=2, text=9, command=lambda: button_display(9))
number9.place(x=20, y=340)
number10 = Button(window, width=2, text=10, command=lambda: button_display(10))
number10.place(x=80, y=340)
number11 = Button(window, width=2, text=11, command=lambda: button_display(11))
number11.place(x=140, y=340)
number12 = Button(window, width=2, text=12, command=lambda: button_display(12))
number12.place(x=200, y=340)
number13 = Button(window, width=2, text=13, command=lambda: button_display(13))
number13.place(x=260, y=340)
number14 = Button(window, width=2, text=14, command=lambda: button_display(14))
number14.place(x=320, y=340)
number15 = Button(window, width=2, text=15, command=lambda: button_display(15))
number15.place(x=380, y=340)
number16 = Button(window, width=2, text=16, command=lambda: button_display(16))
number16.place(x=440, y=340)
number17 = Button(window, width=2, text=17, command=lambda: button_display(17))
number17.place(x=20, y=380)
number18 = Button(window, width=2, text=18, command=lambda: button_display(18))
number18.place(x=80, y=380)
number19 = Button(window, width=2, text=19, command=lambda: button_display(19))
number19.place(x=140, y=380)
number20 = Button(window, width=2, text=20, command=lambda: button_display(20))
number20.place(x=200, y=380)
number21 = Button(window, width=2, text=21, command=lambda: button_display(21))
number21.place(x=260, y=380)
number22 = Button(window, width=2, text=22, command=lambda: button_display(22))
number22.place(x=320, y=380)
number23 = Button(window, width=2, text=23, command=lambda: button_display(23))
number23.place(x=380, y=380)
number24 = Button(window, width=2, text=24, command=lambda: button_display(24))
number24.place(x=440, y=380)
number25 = Button(window, width=2, text=25, command=lambda: button_display(25))
number25.place(x=20, y=420)
number26 = Button(window, width=2, text=26, command=lambda: button_display(26))
number26.place(x=80, y=420)
number27 = Button(window, width=2, text=27, command=lambda: button_display(27))
number27.place(x=140, y=420)
number28 = Button(window, width=2, text=28, command=lambda: button_display(28))
number28.place(x=200, y=420)
number29 = Button(window, width=2, text=29, command=lambda: button_display(29))
number29.place(x=260, y=420)
number30 = Button(window, width=2, text=30, command=lambda: button_display(30))
number30.place(x=320, y=420)
number31 = Button(window, width=2, text=31, command=lambda: button_display(31))
number31.place(x=380, y=420)
number32 = Button(window, width=2, text=32, command=lambda: button_display(32))
number32.place(x=440, y=420)
number33 = Button(window, width=2, text=33, command=lambda: button_display(33))
number33.place(x=20, y=460)
number34 = Button(window, width=2, text=34, command=lambda: button_display(34))
number34.place(x=80, y=460)
number35 = Button(window, width=2, text=35, command=lambda: button_display(35))
number35.place(x=140, y=460)
number36 = Button(window, width=2, text=36, command=lambda: button_display(36))
number36.place(x=200, y=460)
number37 = Button(window, width=2, text=37, command=lambda: button_display(37))
number37.place(x=260, y=460)
number38 = Button(window, width=2, text=38, command=lambda: button_display(38))
number38.place(x=320, y=460)
number39 = Button(window, width=2, text=39, command=lambda: button_display(39))
number39.place(x=380, y=460)
number40 = Button(window, width=2, text=40, command=lambda: button_display(40))
number40.place(x=440, y=460)
number41 = Button(window, width=2, text=41, command=lambda: button_display(41))
number41.place(x=20, y=500)
number42 = Button(window, width=2, text=42, command=lambda: button_display(42))
number42.place(x=80, y=500)
number43 = Button(window, width=2, text=43, command=lambda: button_display(43))
number43.place(x=140, y=500)
number44 = Button(window, width=2, text=44, command=lambda: button_display(44))
number44.place(x=200, y=500)
number45 = Button(window, width=2, text=45, command=lambda: button_display(45))
number45.place(x=260, y=500)
number46 = Button(window, width=2, text=46, command=lambda: button_display(46))
number46.place(x=320, y=500)
number47 = Button(window, width=2, text=47, command=lambda: button_display(47))
number47.place(x=380, y=500)
number48 = Button(window, width=2, text=48, command=lambda: button_display(48))
number48.place(x=440, y=500)
number49 = Button(window, width=2, text=49, command=lambda: button_display(49))
number49.place(x=20, y=540)

results = Label(window, bg='yellow', text="Your Results will be Shown here")
results.place(x=50, y=800)

lotto_list = sample(range(50), 6)


def lotto_draw():
    try:
        user_inputs = list(chain(first_list, second_list, third_list))

        j = set(user_inputs).intersection(lotto_list)

        if len(j) == 0:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You do not win anything')

        elif len(j) == 1:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You do not win anything')
        elif len(j) == 2:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You win a R20')
        elif len(j) == 3:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You win a R100.50')
        elif len(j) == 4:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You win a R2384')
        elif len(j) == 5:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You win a R8584')
        elif len(j) == 6:
            results.config(
                text='Your Numbers chosen were: ' + '\n' + str(user_inputs) + '\n' + 'The winning numbers are: ' +
                     str(lotto_list) + "\n" + 'You win a R10 000 000')
        else:
            results.config(text='You won nothing, you can exit the program now')
    finally:
        return 'nothing'


first_set = Label(window, text=' ', bg='yellow', width=30, borderwidth=3, relief='sunken')
first_set.place(x=130, y=600)
second_set = Label(window, text=' ', bg='yellow', width=30, borderwidth=3, relief='sunken')
second_set.place(x=130, y=630)
third_set = Label(window, text=' ', bg='yellow', width=30, borderwidth=3, relief='sunken')
third_set.place(x=130, y=660)

play_lotto = Button(window, text='Play Lotto', command=lotto_draw, bg='green')
play_lotto.place(x=20, y=700)


def claiming():
    window.destroy()
    import main3


claim_prize = Button(window, text='Claim Prize', bg='light green')
claim_prize.place(x=385, y=700)


def exit_program():
    window.destroy()


exiting = Button(window, text='Exit', bg='red', command=exit_program)
exiting.place(x=440, y=965)

window.mainloop()
