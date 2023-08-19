# Import necessary libraries
from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

# Create the reset window
reset_window = Tk()
reset_window.resizable(0, 0)
reset_window.title('RESET PAGE')
reset_window.geometry('1500x844+10+10')

# Function to clear input fields
def clear():
    username.delete(0, END)
    password.delete(0, END)
    conpassword.delete(0, END)

# Function to reset user's password
def reset_user():
    if username.get() == '' or password.get() == '' or conpassword.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif password.get() != conpassword.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
        conn = pymysql.Connect(host='localhost', user='root', password='praveenmanu')
        mycursor = conn.cursor()

        query = 'use student_registration'
        mycursor.execute(query)
        query1 = 'select * from student_details where username=%s'
        mycursor.execute(query1, (username.get()))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error', 'USER DOES NOT EXIST')
            reset_window.destroy()
            import reset
            return
        else:
            query1 = 'update student_details set password=%s where username=%s'
            mycursor.execute(query1, (password.get(), username.get()))
            messagebox.showinfo('Success', 'Your password has been changed successfully')
            conn.commit()
            conn.close()
            reset_window.destroy()
            import login

# Function to handle event when user clicks on the username entry
def user_enter(event):
    if username.get() == 'USERNAME':
        username.delete(0, END)

# Function to handle event when user clicks on the password entry
def pass_enter(event):
    if password.get() == 'NEW PASSWORD':
        password.delete(0, END)

# Function to handle event when user clicks on the confirm password entry
def newpass_enter(event):
    if conpassword.get() == 'CONFIRM PASSWORD':
        conpassword.delete(0, END)

# Load background image
bg = ImageTk.PhotoImage(file='login20.png')
bglabel = Label(reset_window, image=bg)
bglabel.grid(row=0, column=0)

# Create and place the heading label
heading = Label(reset_window, text='RESET PASSWORD', font=('Microsoft Yahei UI Light', 30, 'bold'),
                bg='white', fg='GREY1')
heading.place(x=110, y=150)

# Create and place the username entry field
username = Entry(reset_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='GREY1')
username.place(x=120, y=280)
username.insert(0, 'USERNAME')
username.bind('<FocusIn>', user_enter)

# Create a frame for underlining the username entry field
frame1 = Frame(reset_window, width=350, height=2, bg='GREY1')
frame1.place(x=120, y=310)

# Create and place the password entry field
password = Entry(reset_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='GREY1')
password.place(x=120, y=380)
password.insert(0, 'NEW PASSWORD')
password.bind('<FocusIn>', pass_enter)

# Create a frame for underlining the password entry field
frame2 = Frame(reset_window, width=350, height=2, bg='GREY1')
frame2.place(x=120, y=410)

# Create and place the confirm password entry field
conpassword = Entry(reset_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='GREY1')
conpassword.place(x=120, y=480)
conpassword.insert(0, 'CONFIRM PASSWORD')
conpassword.bind('<FocusIn>', newpass_enter)

# Create a frame for underlining the confirm password entry field
frame2 = Frame(reset_window, width=350, height=2, bg='GREY1')
frame2.place(x=120, y=510)

# Create and place the "Submit" button
loginbutton = Button(reset_window, text=' SUBMIT ', bd=0, cursor='hand2', activeforeground='white',
                      bg='GREY1', font=('Open Sans', 24, 'bold'), fg='white', width=20,
                      activebackground='GREY1', command=reset_user)
loginbutton.place(x=90, y=580)

# Start the main event loop
reset_window.mainloop()
