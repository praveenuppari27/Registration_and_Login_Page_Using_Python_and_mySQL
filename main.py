# Import necessary libraries
from tkinter import *
import pymysql
from PIL import ImageTk
from tkinter import messagebox
from pymysql import *

# Create the main window
main_window = Tk()
main_window.resizable(0, 0)
main_window.title('SIGN UP PAGE')
main_window.geometry('1500x844+10+10')

# Function to clear input fields
def clear():
    Email.delete(0, END)
    username.delete(0, END)
    password.delete(0, END)
    conformpass.delete(0, END)
    check.set(0)

# Function to connect to the database and register user
def connect_database():
    if Email.get() == '' or username.get() == '' or password.get() == '' or conformpass.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif password.get() != conformpass.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Accept Terms And Conditions')
    else:
        try:
            conn = pymysql.Connect(host='localhost', user='root', password='praveenmanu')
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection is Not established. Try Again')
            return

        try:
            query1 = 'create database student_registration'
            mycursor.execute(query1)
            query2 = 'use student_registration'
            mycursor.execute(query2)
            query3 = 'create table student_details(std_Id int auto_increment primary key not null,Email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query3)
        except:
            mycursor.execute('use student_registration')

        query5 = 'select * from student_details where username=%s'
        mycursor.execute(query5, (username.get()))
        row = mycursor.fetchone()

        if row != None:
            messagebox.showerror('Error', 'User Already Exists')
        else:
            query4 = 'insert into student_details(Email,username,password) values(%s,%s,%s)'
            mycursor.execute(query4, (Email.get(), username.get(), password.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()
            main_window.destroy()
            import login

# Function to navigate to the login page
def login_page():
    main_window.destroy()
    import login

# Function to handle event when user clicks on the email entry
def Email_enter(event):
    if Email.get() == 'EMAIL':
        Email.delete(0, END)

# Function to handle event when user clicks on the username entry
def user_enter(event):
    if username.get() == 'USERNAME':
        username.delete(0, END)

# Function to handle event when user clicks on the password entry
def pass_enter(event):
    if password.get() == 'PASSWORD':
        password.delete(0, END)

# Function to handle event when user clicks on the confirm password entry
def conformpass_enter(event):
    if conformpass.get() == 'CONFORM PASSWORD':
        conformpass.delete(0, END)

# Load background image
bg = ImageTk.PhotoImage(file='login20.png')
bglabel = Label(main_window, image=bg)
bglabel.grid(row=0, column=0)

# Create and place the heading label
heading = Label(main_window, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 25, 'bold'),
                bg='white', fg='firebrick1')
heading.place(x=90, y=150)

# Create and place the email entry field
Email = Entry(main_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
Email.place(x=100, y=250)
Email.insert(0, 'EMAIL')
Email.bind('<FocusIn>', Email_enter)

# Create a frame for underlining the email entry field
frame1 = Frame(main_window, width=350, height=2, bg='firebrick1')
frame1.place(x=100, y=280)

# Create and place the username entry field
username = Entry(main_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
username.place(x=100, y=345)
username.insert(0, 'USERNAME')
username.bind('<FocusIn>', user_enter)

# Create a frame for underlining the username entry field
frame2 = Frame(main_window, width=350, height=2, bg='firebrick1')
frame2.place(x=100, y=375)

# Create and place the password entry field
password = Entry(main_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
password.place(x=100, y=440)
password.insert(0, 'PASSWORD')
password.bind('<FocusIn>', pass_enter)

# Create a frame for underlining the password entry field
frame3 = Frame(main_window, width=350, height=2, bg='firebrick1')
frame3.place(x=100, y=470)

# Create and place the confirm password entry field
conformpass = Entry(main_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
conformpass.place(x=100, y=535)
conformpass.insert(0, 'CONFORM PASSWORD')
conformpass.bind('<FocusIn>', conformpass_enter)

# Create a frame for underlining the confirm password entry field
frame4 = Frame(main_window, width=350, height=2, bg='firebrick1')
frame4.place(x=100, y=565)

# Create and place the terms and conditions checkbox
check = IntVar()
checkbutton = Checkbutton(main_window, text='I agree to the terms and conditions', font=('Microsoft Yahei UI Light', 12, 'bold'),
                          bd=0, bg='white', fg='firebrick1', activebackground='white', activeforeground='firebrick1',
                          variable=check)
checkbutton.place(x=110, y=585)

# Create and place the "Sign Up" button
mainbutton = Button(main_window, text=' Sign Up ', bd=0, cursor='hand2', activeforeground='white', bg='firebrick1',
                    font=('Open Sans', 18, 'bold'), fg='white', width=26, height=1, activebackground='firebrick1',
                    command=connect_database)
mainbutton.place(x=90, y=635)

# Create a label asking if user has an account
Label(main_window, text='Do you have an account ?', font=('Microsoft Yahei UI Light', 15, 'bold'),
      fg='firebrick1', bg='white').place(x=100, y=710)

# Create and place the "Login" button
loginbutton = Button(main_window, text='Login ', font=('Microsoft Yahei UI Light', 15, 'bold'), fg='blue2',
                     activeforeground='blue2', bg='white', activebackground='white', bd=0, cursor='hand2',
                     command=login_page)
loginbutton.place(x=370, y=705)

# Start the main event loop
main_window.mainloop()
