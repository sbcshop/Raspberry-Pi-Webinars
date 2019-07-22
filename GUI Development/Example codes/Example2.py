'''
Example to learn how to change the size and title of window
'''

import tkinter

# create tkinter parent window
window = tkinter.Tk()

# to change the title of window
window.title('My GUI')

# to change the size of the window (width x height)
window.geometry('600x320')

window.mainloop()
