from tkinter import *
from PIL import ImageTk



window =Tk()
window.geometry('1910x1200')
window.resizable(False,False)
window.title("logo")



backgroundImage=ImageTk.PhotoImage(file='Dd.png')
bgLabel=Label(window,image=backgroundImage) 
bgLabel.place(x=0,y=0)









loginButton=Button(window,text='Log In',font=("Goergia"),fg='white',bg='#100E32',activebackground='#100E32',activeforeground='white')
loginButton.place(x=1500,y=900,width=250,height=50)


signupButton=Button(window,text='Sign up',font=("Goergia"),fg='white',bg='#100E32',activebackground='#100E32',activeforeground='white')
signupButton.place(x=1150,y=900,width=250,height=50)



window.mainloop()  