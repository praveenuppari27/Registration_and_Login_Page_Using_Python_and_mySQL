# Import necessary libraries
from PIL import ImageTk
from pymysql import *
from tkinter import *
from tkinter import messagebox

# Create the Thank You window
Thankyou_window = Tk()
Thankyou_window.title('Thank You')
Thankyou_window.geometry('1500x937+10+10')

# Load the background image
bg = ImageTk.PhotoImage(file='thankyou.jpg')

# Create a label to display the background image
bglabel = Label(Thankyou_window, image=bg)
bglabel.pack()

# Start the main event loop
Thankyou_window.mainloop()
