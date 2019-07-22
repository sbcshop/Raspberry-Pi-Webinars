'''
Example to learn more about label with option values
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')

# to create a label
w = Label(window, text='My first Label', height=10, width=5,
          bg='black', fg='white')
w.pack()

window.mainloop()
