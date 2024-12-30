from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


window = Tk()

window.geometry('1920x1200')
window.resizable(False, False)
window.title("Pharmacy")




########################################################## Background Image #############################################################################################################

backgroundImage = ImageTk.PhotoImage(file='background login.png')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=-67)

######################################################################################################################################################################################


# Login Function
def loginButton():
    if entry_user.get() == 'noran nassar' and entry_ID.get() == '241001233':
        messagebox.showinfo('Success', 'Login is successful')
    else:
        messagebox.showerror('Error', 'Incorrect name or ID')



# Logo Image
logoImage = PhotoImage(file='pharmacist.png')
logoLabel = Label(window, image=logoImage, bg="white")
logoLabel.place(x=850, y=50)

# Log In Button
loginButton = Button(
    window, text='Log In', font=("Georgia", 15), fg='white', bg='cornflowerblue',
    activebackground='cornflowerblue', activeforeground='white', command=loginButton
)
loginButton.place(x=1200, y=850, width=300, height=60)
########################################################################################################################################################################################


############################################################# Employee Name Entry###########################################################################################################


user_label = Label(window, text='Employee Name', font=('Georgia', 20), fg='Gray')
user_label.place(x=600, y=450)

entry_user = Entry(window, bd=0, font=("Georgia", 20))
entry_user.place(x=600, y=500, width=670, height=50)




################################################################# Employee ID Entry####################################################################################################

label1 = Label(window, text='Employee ID', font=('Georgia', 20), fg='Gray')
label1.place(x=600, y=650)

entry_ID = Entry(window, bd=0, font=("Georgia", 20))
entry_ID.place(x=600, y=700, width=670, height=50)


window.mainloop()
