'''
Example to learn about place geometry
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')

window.geometry('400x320')

# to create a label
w1 = Label(window, text='Label 1', bg='black', font=('Helvetica',12), fg='white')
w1.place(x=10, y=20)

w2 = Label(window, text='My Label for testing',font=('Helvetica',12), bg='red', fg='white')
w2.place(x=100, y=200)

w3 = Label(window, text='Label 3',font=('Helvetica',12), bg='blue', fg='white')
w3.place(x=270, y=150)

window.mainloop()










