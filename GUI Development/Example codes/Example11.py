'''
Example to learn about image on label
'''

from tkinter import *

window = Tk()

# to change the title of window
window.title('My GUI')

# create a image
twitter = PhotoImage(file='/home/pi/Downloads/twitter.png')
 

# to create a label
w1 = Label(window, image=twitter)
w1.grid(row=0, column=0)

w2 = Label(window, text='My Label for testing',font=('Helvetica',12), bg='red', fg='white')
w2.grid(row=0, column=1)

w3 = Label(window, text='Label 3',font=('Helvetica',12), bg='blue', fg='white')
w3.grid(row=0, column=2)

window.mainloop()










