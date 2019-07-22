'''
Example code to control GPIO pin 17 using cget
'''


from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)


# function bind with button
def led():

    if b.cget('text') == 'LED ON':
        print('LED OFF')
        GPIO.output(17, GPIO.HIGH)
        b.config(text='LED OFF', bg='red',fg='white', relief=RAISED)
        
    else:
        print('LED ON')
        GPIO.output(17, GPIO.LOW)
        b.config(text='LED ON', bg='green',fg='black', relief=SUNKEN)
        

window = Tk()

# to change the title of window
window.title('GPIO Control')

# to create a button
b = Button(window, text='LED ON', bg='green',height=4, width=10, command=led)
b.grid(row=0, column=0)

w = Button(window, text='Quit', height=4, width=10, command=window.destroy)
w.grid(row=0, column=1)


window.mainloop()


