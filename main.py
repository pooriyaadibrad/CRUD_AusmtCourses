from tkinter import *

win=Tk()
win.geometry("800x600")
win.title('CRUD')
win.iconbitmap('icons/Mainicon.ico')
#win.attributes("-fullscreen", True)
win.configure(background='#216ADE')
#txt
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtFamily.place(x=100,y=160)

txtFiled=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtFiled.place(x=100,y=220)

txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtAge.place(x=100,y=280)
win.mainloop()