# Import necessary libraries
from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

# Function to handle the "Forgot Password" functionality
def forget():
    login_window.destroy()
    import reset

# Function to handle user login
def login_user():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            # Establish a database connection
            conn = pymysql.Connect(host='localhost', user='root', password='praveenmanu')
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error', 'Connection is Not Established. Try Again')
            return

        # Use the student_registration database
        query = 'USE student_registration'
        mycursor.execute(query)

        # Check if the provided username and password are valid
        query1 = 'SELECT * FROM student_details WHERE username=%s AND password=%s'
        mycursor.execute(query1, (username.get(), password.get()))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror('Error', 'Invalid Username Or Password')
        else:
            messagebox.showinfo('Success', 'Login is Successful')
            conn.close()
            login_window.destroy()
            import thankyou

# Function to handle the "Sign Up" functionality
def sign_up():
    login_window.destroy()
    import main

# Function to handle event when user clicks on the username entry
def user_enter(event):
    if username.get() == 'USERNAME':
        username.delete(0, END)

# Function to handle event when user clicks on the password entry
def pass_enter(event):
    if password.get() == 'PASSWORD':
        password.delete(0, END)

# Function to hide the password
def hide():
    openeye.config(file='closeye.png')
    password.config(show='*')
    eyebutton.config(command=show)

# Function to show the password
def show():
    openeye.config(file='openeye.png')
    password.config(show='')
    eyebutton.config(command=hide)

# Create the main login window
login_window = Tk()
login_window.resizable(0, 0)
login_window.title('SIGN UP PAGE')
login_window.geometry('1500x844+10+10')

# Load background image
bg = ImageTk.PhotoImage(file='login20.png')
bglabel = Label(login_window, image=bg)
bglabel.grid(row=0, column=0)

# Create and place the heading label
heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='white', fg='firebrick1')
heading.place(x=170, y=150)

# Create and place the username entry field
username = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
username.place(x=120, y=280)
username.insert(0, 'USERNAME')
username.bind('<FocusIn>', user_enter)

# Create a frame for underlining the username entry field
frame1 = Frame(login_window, width=350, height=2, bg='firebrick1')
frame1.place(x=120, y=310)

# Create and place the password entry field
password = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
password.place(x=120, y=380)
password.insert(0, 'PASSWORD')
password.bind('<FocusIn>', pass_enter)

# Create a frame for underlining the password entry field
frame2 = Frame(login_window, width=350, height=2, bg='firebrick1')
frame2.place(x=120, y=410)

# Load images for the open eye and close eye icons
openeye = PhotoImage(file="openeye.png")

# Create a button to toggle password visibility
eyebutton = Button(login_window, image=openeye, bd=0, cursor='hand2', activebackground='white', bg='white', command=hide)
eyebutton.place(x=430, y=380)

# Create and place the "Forgot Password" button
forgetbutton = Button(login_window, text=' Forgot Password?', bd=0, cursor='hand2', activeforeground='firebrick1',
                      bg='white', activebackground='white', font=('Microsoft Yahei UI Light', 11, 'bold'),
                      fg='firebrick1', command=forget)
forgetbutton.place(x=320, y=420)

# Create and place the "Login" button
loginbutton = Button(login_window, text=' Login ', bd=0, cursor='hand2', activeforeground='white', bg='firebrick1',
                     font=('Open Sans', 24, 'bold'), fg='white', width=20, activebackground='firebrick1', command=login_user)
loginbutton.place(x=90, y=500)

# Create and place the separator label
orlabel = Label(login_window, text='<<<<<<<<<<<  OR  >>>>>>>>>>>', font=('Open Sans', 16), fg='firebrick1', bg='white')
orlabel.place(x=110, y=590)

# Load images for social media icons
fimage = PhotoImage(file='facebook.png')
gimage = PhotoImage(file='google (1).png')
timage = PhotoImage(file='twitter.png')

# Place the social media icons
Label(login_window, image=fimage, bg='white').place(x=200, y=650)
Label(login_window, image=gimage, bg='white').place(x=260, y=650)
Label(login_window, image=timage, bg='white').place(x=320, y=650)

# Create and place the "Don't have an account?" label
Label(login_window, text="Don't have an account?", font=('Microsoft Yahei UI Light', 15, 'bold'),
      fg='firebrick1', bg='white').place(x=110, y=730)

# Create and place the "Sign Up" button
signupbutton = Button(login_window, text='Sign Up', font=('Microsoft Yahei UI Light', 15, 'bold'),
                      fg='blue2', activeforeground='blue2', bg='white', activebackground='white', bd=0,
                      cursor='hand2', command=sign_up)
signupbutton.place(x=360, y=725)

# Start the main event loop
login_window.mainloop()
