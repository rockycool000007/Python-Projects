import tkinter

# Calculator main window details
m_window = tkinter.Tk()
m_window.title('Calculator')
m_window.geometry('300x300+800+350')

# Results entry box
results = tkinter.Entry(m_window, justify='center', borderwidth=4, relief='sunken')
results.grid(row=0, column=0, columnspan=3, padx=60, pady=5, ipady=5)

# Button frame
b_frame = tkinter.Frame(m_window, borderwidth=4, relief='groove')
b_frame.grid(row=2, column=0, padx=10, pady=10)

# Buttons
button = tkinter.Button(b_frame, text='test')
button.grid(row=0, column=0, sticky='w')
button1 = tkinter.Button(b_frame, text='test')
button1.grid(row=0, column=1, sticky='w')

m_window.mainloop()
