'''
Example to learn about button widget
'''

from tkinter import *

# function bind with button
def press():
    print('Button pressed')
    

window = Tk()

# to change the title of window
window.title('My GUI')

# to create a button
b = Button(window, text='Button', height=4, width=4, command=press)
b.grid(row=0, column=0)


window.mainloop()










