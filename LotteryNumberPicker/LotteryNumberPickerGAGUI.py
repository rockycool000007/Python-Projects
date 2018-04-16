"""
Title: Lottery Number Picker GUI Version
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: Generate hopefully winning lottery numbers for GA Lottery games
"""

import random
import tkinter


# Cash 3 Rules:
# You pick 3 numbers from 0 to 9.
# Duplicate numbers are allowed
def cash_3():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    # The frame for the generated lottery numbers
    global numbers_frame
    numbers_frame.destroy()
    numbers_frame = tkinter.Frame(m_window, background='black')
    numbers_frame.grid(row=3, column=0)
    generated_num = tkinter.StringVar()
    numbers = tkinter.Label(numbers_frame, textvariable=generated_num, background='black',
                            foreground='white', font='bold')
    generated_num.set('Your Cash 3 Numbers:\n{}{}{}'.format(num1, num2, num3))
    numbers.grid(row=1, column=0)


# Cash 4 Rules:
# You pick 4 numbers from 0 to 9.
# Duplicate numbers are allowed
def cash_4():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    # The frame for the generated lottery numbers
    global numbers_frame
    numbers_frame.destroy()
    numbers_frame = tkinter.Frame(m_window, background='black')
    numbers_frame.grid(row=3, column=0)
    generated_num = tkinter.StringVar()
    numbers = tkinter.Label(numbers_frame, textvariable=generated_num, background='black',
                            foreground='white', font='bold')
    generated_num.set('Your Cash 4 Numbers:\n{}{}{}{}'.format(num1, num2, num3, num4))
    numbers.grid(row=1, column=0)


# Fantasy 5 Rules:
# You pick 5 numbers from 1 to 42
# Duplicate numbers are not allowed
def fantasy_5():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 9)
    num2 = random.randint(10, 19)
    num3 = random.randint(20, 29)
    num4 = random.randint(30, 36)
    num5 = random.randint(37, 42)
    num_list = sorted([num1, num2, num3, num4, num5])
    # The frame for the generated lottery numbers
    global numbers_frame
    numbers_frame.destroy()
    numbers_frame = tkinter.Frame(m_window, background='black')
    numbers_frame.grid(row=3, column=0)
    generated_num = tkinter.StringVar()
    numbers = tkinter.Label(numbers_frame, textvariable=generated_num, background='black',
                            foreground='white', font='bold')
    generated_num.set('Your Fantasy 5 Numbers:\n{} {} {} {} {}'.format(num_list[0], num_list[1], num_list[2],
                                                                       num_list[3], num_list[4]))
    numbers.grid(row=1, column=0)


# Mega Millions Rules:
# You pick 5 numbers from 1 to 70
# You pick 1 MEGA BALL from 1 to 25
# Duplicate numbers are not allowed
def mega_millions():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 14)
    num2 = random.randint(15, 29)
    num3 = random.randint(30, 44)
    num4 = random.randint(45, 59)
    num5 = random.randint(60, 70)
    mega_ball = random.randint(1, 25)
    num_list = sorted([num1, num2, num3, num4, num5])
    # The frame for the generated lottery numbers
    global numbers_frame
    numbers_frame.destroy()
    numbers_frame = tkinter.Frame(m_window, background='black')
    numbers_frame.grid(row=3, column=0)
    generated_num = tkinter.StringVar()
    numbers = tkinter.Label(numbers_frame, textvariable=generated_num, background='black',
                            foreground='white', font='bold')
    generated_num.set('Your Mega Millions Numbers:\n{} {} {} {} {} [{}]'.format(num_list[0], num_list[1], num_list[2],
                                                                                num_list[3], num_list[4], mega_ball))
    numbers.grid(row=1, column=0)


# Powerball Rules:
# You pick 5 numbers from 1 to 69
# You pick 1 MEGA BALL from 1 to 26
# Duplicate numbers are not allowed
def powerball():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 13)
    num2 = random.randint(14, 27)
    num3 = random.randint(28, 39)
    num4 = random.randint(40, 57)
    num5 = random.randint(58, 69)
    power_ball = random.randint(1, 26)
    num_list = sorted([num1, num2, num3, num4, num5])
    # The frame for the generated lottery numbers
    global numbers_frame
    numbers_frame.destroy()
    numbers_frame = tkinter.Frame(m_window, background='black')
    numbers_frame.grid(row=3, column=0)
    generated_num = tkinter.StringVar()
    numbers = tkinter.Label(numbers_frame, textvariable=generated_num, background='black',
                            foreground='white', font='bold')
    generated_num.set('Your Powerball Numbers:\n{} {} {} {} {} [{}]'.format(num_list[0], num_list[1], num_list[2],
                                                                            num_list[3], num_list[4], power_ball))
    numbers.grid(row=1, column=0)


# Jumbo Bucks Lotto Rules:
# You pick 6 numbers from 1 to 47
# Duplicate numbers are not allowed
def jumbo_bucks_lotto():
    # I divided up the ranges like this to keep from getting duplicate numbers
    num1 = random.randint(1, 8)
    num2 = random.randint(9, 18)
    num3 = random.randint(19, 27)
    num4 = random.randint(28, 35)
    num5 = random.randint(36, 41)
    num6 = random.randint(42, 47)
    num_list = sorted([num1, num2, num3, num4, num5, num6])
    # The frame for the generated lottery numbers
    global numbers_frame
    numbers_frame.destroy()
    numbers_frame = tkinter.Frame(m_window, background='black')
    numbers_frame.grid(row=3, column=0)
    generated_num = tkinter.StringVar()
    numbers = tkinter.Label(numbers_frame, textvariable=generated_num, background='black',
                            foreground='white', font='bold')
    generated_num.set('Your Jumbo Bucks Lotto Numbers:\n{} {} {} {} {} {}'.format(num_list[0], num_list[1], num_list[2],
                                                                                  num_list[3], num_list[4],
                                                                                  num_list[5]))
    numbers.grid(row=1, column=0)


m_window = tkinter.Tk()

# Setup the main window and frames for the player and computer player
m_window.title('Lottery Number Picker: Georgia')
m_window.geometry('350x300-800-400')  # Creates an offset to put the window in the middle of the monitor
m_window.configure(background='black')
m_window['padx'] = 5

# The frame for the message section
label_frame = tkinter.Frame(m_window)
label_frame.grid(row=0, column=0)

# The label section at the top that displays the how to use the program
label = tkinter.Label(label_frame, background='black', foreground='white', pady=10,
                      text='Click the button to generate your winning numbers!')
label.grid(row=0, column=0)

# The frame for the buttons
button_frame = tkinter.Frame(m_window, background='black')
button_frame.grid(row=2, column=0)

# Lottery games buttons
cash3_button = tkinter.Button(button_frame, text='Cash 3', command=cash_3)
cash3_button.grid(row=1, column=0)
cash4_button = tkinter.Button(button_frame, text='Cash 4', command=cash_4)
cash4_button.grid(row=1, column=1)
fantasy5_button = tkinter.Button(button_frame, text='Fantasy 5', command=fantasy_5)
fantasy5_button.grid(row=1, column=2)
mega_millions_button = tkinter.Button(button_frame, text='Mega Millions', command=mega_millions)
mega_millions_button.grid(row=2, column=0)
powerball_button = tkinter.Button(button_frame, text='Powerball', command=powerball)
powerball_button.grid(row=2, column=1)
jumbo_bucks_lotto_button = tkinter.Button(button_frame, text='Jumbo Bucks Lotto', command=jumbo_bucks_lotto)
jumbo_bucks_lotto_button.grid(row=2, column=2)

# The frame for the generated lottery numbers
numbers_frame = tkinter.Frame(m_window, background='black')
numbers_frame.grid(row=3, column=0)

m_window.mainloop()
