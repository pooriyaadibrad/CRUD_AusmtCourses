from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
import messagebox
Client = MongoClient('localhost', 27017)
db=Client['CRUD']
persons=db['persons2']

win=Tk()
win.geometry("850x600")
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
    if btnRegister.cget('state')==NORMAL:
        try:
            person={'name':txtName.get(),'family':txtFamily.get(),'feild':comboBoxFiled.get(),'age':int(txtAge.get())}
            if Exist(person)==False:
                Register(person)
                allData=ReadData()
                CleanTable()
                for data in allData:
                    InsertDataToTable(data)
                CleanTextBoxAfterUseCrud()
                messagebox.showinfo("Success","ثبت نام شما با موفقیت انجام شد!")
            else:
                messagebox.showerror('Error',"شما قبلا ثبت نام کردید!")
        except:
            messagebox.showerror('Error','مقدار داخل فیلد سن باید عددی باشد!')

def Register(person):
    if person['age']>=18:
        persons.insert_one(person)
def ReadData():
    AllData=persons.find()
    return AllData
def InsertDataToTable(person):
    table.insert('','end',values=[person['name'],person['family'],person['feild'],person['age']])
def CleanTable():
    for item in table.get_children():
        table.delete(item)
def CleanTextBoxAfterUseCrud():
    Name.set('')
    Family.set('')

    Age.set('')
    txtName.focus_set()
def ActiveBtn(e):
    #print('ActiveBtn')
    if txtName.get() != '' and txtFamily.get() != '' and comboBoxFiled.get()!= '' and txtAge.get() != '' :
        btnRegister.configure(state=NORMAL)
    else:
        btnRegister.configure(state=DISABLED)
def Exist(person):
    allData=ReadData()
    for data in allData:
        if data['name'] == person['name'] and data['family'] == person['family'] and data['feild'] == person['feild'] and data['age']== person['age']:
            return True
    return False
Name=StringVar()
Family=StringVar()

Age=StringVar()


#txt
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Name,justify='center')
txtName.bind('<KeyRelease>',ActiveBtn)
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Family,justify='center')
txtFamily.bind('<KeyRelease>',ActiveBtn)
txtFamily.place(x=100,y=160)

comboBoxFiled=ttk.Combobox(win,width=15,font=('arial',15,'bold'),foreground='#216ADE',background='white')
comboBoxFiled['values']=['computer','electronics','chemistry','physics']
comboBoxFiled.place(x=100,y=220)

txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Age,justify='center')
txtAge.bind('<KeyRelease>',ActiveBtn)
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
btnRegister.configure(state=DISABLED)
btnRegister.bind('<Enter>',ChangeButtonStyleWithHover)
btnRegister.bind('<Leave>',ChangeButtonStyleWithHoverToSelf)
btnRegister.bind('<Button-1>',onClickRegister)
btnRegister.place(x=125,y=350)

#tbl
columns=('Name','Family','Feild','Age')
table=ttk.Treeview(win,columns=columns,show='headings')
"""
table.heading('name',text='Name')
table.heading('family',text='Family')
table.heading('feild',text='Feild')
table.heading('age',text='Age')
table.column('name',width=100)
table.column('family',width=100)
table.column('feild',width=100)
table.column('age',width=100)
"""
for i in range(len(columns)):
    table.heading(columns[i],text=columns[i])
    table.column(columns[i],width=100,anchor='center')
table.place(x=400,y=100)
win.mainloop()