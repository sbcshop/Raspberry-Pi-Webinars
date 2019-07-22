'''
Example to learn more about pack - side
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')

# to create a label
w1 = Label(window, text='Label 1', bg='black', font=('Helvetica',12), fg='white')
w1.pack(fill='x', padx=10, side='left')

w2 = Label(window, text='My Label for testing',font=('Helvetica',12), bg='red', fg='white')
w2.pack(fill='x', padx=10, side='top')

w3 = Label(window, text='Label 3',font=('Helvetica',12), bg='blue', fg='white')
w3.pack(fill='x', padx=10, side='right')

window.mainloop()










