'''
Example to learn more about pack - fill
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')

# to create a label
w1 = Label(window, text='Label 1', bg='black', font=('Helvetica',16), fg='white')
w1.pack(fill='x')

w2 = Label(window, text='My Label for testing',font=('Helvetica',12), bg='red', fg='white')
w2.pack()

w3 = Label(window, text='Label 3',font=('Helvetica',12), bg='blue', fg='white')
w3.pack(fill='x')

window.mainloop()
