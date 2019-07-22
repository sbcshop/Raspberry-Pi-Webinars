'''
Example to learn about button widget
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')
 

# to create a button
b1 = Button(window, text='Button', activebackground='green', bg='red',fg='black', height=4, width=10)
b1.grid(row=0, column=0)

b2 = Button(window, text='Button', bg='red',fg='black', height=4, width=10)
b2.grid(row=0, column=1)

b3 = Button(window, text='Button', bg='red',fg='black', height=4, width=10)
b3.grid(row=0, column=2)

window.mainloop()










