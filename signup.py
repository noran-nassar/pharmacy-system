from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

window = Tk()
window.geometry('1900x1200')
window.resizable(False, False)
window.title("Sign Up")



# Background Image
backgroundImage = ImageTk.PhotoImage(file='n.png')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)






# Username Entry
user_label = Label(window, text='User Name', font=('Georgia', 15), fg='Gray')
user_label.place(x=150, y=130)
entry_username = Entry(window, bd=2, font=("Georgia", 15))
entry_username.place(x=150, y=180, width=650, height=50)





# Email Entry
label_email = Label(window, text='Email', font=('Georgia', 15), fg='Gray')
label_email.place(x=150, y=270)
entry_email = Entry(window, bd=2, font=("Georgia", 15))
entry_email.place(x=150, y=330, width=650, height=50)





# Phone Number Entry
label_phone = Label(window, text='Phone Number', font=('Georgia', 15), fg='Gray')
label_phone.place(x=150, y=420)
entry_phonenumber = Entry(window, bd=2, font=("Georgia", 15))
entry_phonenumber.place(x=150, y=470, width=650, height=50)




# Password Entry
label_password = Label(window, text='Password', font=('Georgia', 15), fg='Gray')
label_password.place(x=150, y=560)
entry_password = Entry(window, bd=2, font=("Georgia", 15), show="*")
entry_password.place(x=150, y=610, width=650, height=50)






# Confirm Password Entry
label_confirmpassword = Label(window, text='Confirm Password', font=('Georgia', 15), fg='Gray')
label_confirmpassword.place(x=150, y=700)
entry_confirmpassword = Entry(window, bd=2, font=("Georgia", 15), show="*")
entry_confirmpassword.place(x=150, y=750, width=650, height=50)






# Sign Up Button


def signup():
    username = entry_username.get()
    email = entry_email.get()
    phone = entry_phonenumber.get()
    password = entry_password.get()
    confirm_password = entry_confirmpassword.get()
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
    elif not (username and email and phone and password and confirm_password):
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", "Sign-Up Successful!")



signupButton = Button(window, text='Sign Up', font=("Georgia", 15), fg='white', bg='gray',
                      activebackground='gray', activeforeground='white')
signupButton.place(x=640, y=900, width=250, height=50)



window.mainloop()
