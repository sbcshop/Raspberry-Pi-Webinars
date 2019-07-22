'''
Example code to control GPIO pin 17
'''


from tkinter import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

index = 0


# function bind with button
def led():
    global index

    if index:
        print('LED OFF')
        GPIO.output(17, GPIO.LOW)
        b.config(text='LED ON', bg='red',fg='black', relief=SUNKEN)
    else:
        print('LED ON')
        GPIO.output(17, GPIO.HIGH)
        b.config(text='LED OFF', bg='green',fg='white', relief=RAISED)

    index = not index



window = Tk()

# to change the title of window
window.title('GPIO Control')

# to create a button
b = Button(window, text='LED ON', bg='red',bd=5,height=4, width=10, command=led)
b.grid(row=0, column=0)

w = Button(window, text='Quit', height=4,bd=5, width=10, command=window.destroy)
w.grid(row=0, column=1)


window.mainloop()


