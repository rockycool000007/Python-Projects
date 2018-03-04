import tkinter

# Calculator main window details
m_window = tkinter.Tk()
m_window.title('Calculator')
m_window.geometry('300x300+800+350')

# Results entry box
results = tkinter.Entry(m_window, justify='center', borderwidth=4, relief='sunken')
results.grid(row=0, column=0, sticky='nsew', ipady=4)

# Button frame
b_frame = tkinter.Frame(m_window, borderwidth=4, relief='groove')
b_frame.grid(row=2, column=0, sticky='nsew')

# Button list
b_list = [[('C', 1), ('CE', 1)],
          [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
          [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
          [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
          [('0', 1), ('=', 1), ('/', 1)]]

# Initializing the row for the buttons
b_row = 0

# Loop that creates the buttons on the calculator
for button_row in b_list:
    b_column = 0 # Initializes the columns in the b_frame
    for button in button_row:
        tkinter.Button(b_frame, text=button[0]).grid(row=b_row, column=b_column, columnspan=button[1], sticky=tkinter.E + tkinter.W)
        b_column += button[1] # Adds the columns using the list key
    b_row += 1 # Adds the button rows

# To resize the calculator window
m_window.update()
m_window.minsize(b_frame.winfo_width(), results.winfo_height() + b_frame.winfo_height())
m_window.maxsize(b_frame.winfo_width() + 10, results.winfo_height() + 10 + b_frame.winfo_height())

m_window.mainloop()
