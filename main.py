from tkinter import *
from pymongo import MongoClient
Client = MongoClient('localhost', 27017)
db=Client['CRUD']
persons=db['persons']

win=Tk()
win.geometry("800x600")
win.title('CRUD')
win.iconbitmap('icons/Mainicon.ico')
#win.attributes("-fullscreen", True)
win.configure(background='#216ADE')
#def
def ChangeButtonStyleWithHover(e):
    btnRegister.configure(fg='#822FC1',background='white')
def ChangeButtonStyleWithHoverToSelf(e):
    btnRegister.configure(fg='white',background='#822FC1')
def onClickRegister(e):
    person={'name':txtName.get(),'family':txtFamily.get(),'feild':txtFiled.get(),'age':txtAge.get()}
    Register(person)
def Register(person):
    persons.insert_one(person)

#txt
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtFamily.place(x=100,y=160)
#justfy
txtFiled=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtFiled.place(x=100,y=220)

txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white')
txtAge.place(x=100,y=280)
#lbl
lblName=Label(win,text='Name',font=('arial',15,'bold'),fg='white',background='#216ADE')
lblName.place(x=20,y=100)

lblFamily=Label(win,text='Family',font=('arial',15,'bold'),fg='white',background='#216ADE')
lblFamily.place(x=20,y=160)

lblFiled=Label(win,text='Filed',font=('arial',15,'bold'),fg='white',background='#216ADE')
lblFiled.place(x=20,y=220)

lblAge=Label(win,text='Age',font=('arial',15,'bold'),fg='white',background='#216ADE')
lblAge.place(x=20,y=280)

#btn
btnRegister=Button(win,text='Register',width=10,font=('arial',15,'bold'),fg='white',background='#822FC1')
btnRegister.bind('<Enter>',ChangeButtonStyleWithHover)
btnRegister.bind('<Leave>',ChangeButtonStyleWithHoverToSelf)
btnRegister.bind('<Button-1>',onClickRegister)
btnRegister.place(x=125,y=350)
win.mainloop()