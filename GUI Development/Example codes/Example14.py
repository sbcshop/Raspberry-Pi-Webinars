'''
Example to learn about toggle button
'''

from tkinter import *


index = 0


# function bind with button
def press():
    global index

    if not index:
        print('Button pressed')
        b.config(text='OFF', bg='red',fg='white', relief=SUNKEN)
    else:
        print('Button Released')
        b.config(text='ON', bg='green',fg='black', relief=RAISED)

    index = not index
        
    
window = Tk()


# to change the title of window
window.title('My GUI')

# to create a button
b = Button(window, text='ON', bg='green',bd=4, height=4, width=10, command=press)
b.grid(row=0, column=0)

w = Button(window, text='Quit', height=4,bd=4, width=10, command=window.destroy)
w.grid(row=0, column=1)


window.mainloop()










