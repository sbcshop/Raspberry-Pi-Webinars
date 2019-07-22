'''
Example to create a Label
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')

# to change the size of the window (width x height)
#window.geometry('400x320')

# to create a label
w = Label(window, text='My first Label')
w.pack()

window.mainloop()
