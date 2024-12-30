from tkinter import *
from PIL import ImageTk



window =Tk()
window.geometry('1910x1200')
window.resizable(False,False)
window.title("logo")



backgroundImage=ImageTk.PhotoImage(file='logo.png')
bgLabel=Label(window,image=backgroundImage) 
bgLabel.place(x=0,y=-630)





loginfram=Frame(window)
loginfram.place(x=600,y=650)
logoImage=PhotoImage(file='logo4.png')
logoLabel=Label(loginfram,image=logoImage)
logoLabel.grid(row=0,column=0)




loginButton=Button(window,text='Log In',font=("Goergia"),fg='white',bg='#70BBFE',activebackground='#70BBFE',activeforeground='white')
loginButton.place(x=1600,y=900,width=200,height=70)


signupButton=Button(window,text='Sign up',font=("Goergia"),fg='white',bg='#70BBFE',activebackground='#70BBFE',activeforeground='white')
signupButton.place(x=1350,y=900,width=200,height=70)



window.mainloop()  