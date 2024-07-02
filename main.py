from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
import messagebox
Client = MongoClient('localhost', 27017)
db=Client['CRUD']
persons=db['persons3']

win=Tk()
#win.geometry("850x600")
win.title('CRUD')
win.iconbitmap('icons/Mainicon.ico')
win.attributes("-fullscreen", True)
win.configure(background='#216ADE')
#def
def ChangeButtonStyleWithHoverRegister(e):
    btnRegister.configure(fg='#822FC1',background='white')
def ChangeButtonStyleWithHoverToSelfRegister(e):
    btnRegister.configure(fg='white',background='#822FC1')
def ChangeButtonStyleWithHoverSearch(e):
    btnSearch.configure(fg='#822FC1',background='white')
def ChangeButtonStyleWithHoverToSelfSearch(e):
    btnSearch.configure(fg='white',background='#822FC1')
def ChangeButtonStyleWithHover(e):
    if e.widget['text'] == 'Delete':
        btnDelete.configure(fg='white', background='#D00A0A')
    elif e.widget['text'] == 'Update':
        btnUpdate.configure(fg='#822FC1', background='white')

def ChangeButtonStyleWithHoverToSelf(e):
    if e.widget['text']=='Delete':
        btnDelete.configure(fg='white', background='red')
    elif e.widget['text'] == 'Update':
        btnUpdate.configure(fg='white', background='#822FC1')

def onClickRegister(e):
    if btnRegister.cget('state')==NORMAL:
        try:
            person={'name':txtName.get(),'family':txtFamily.get(),'field':comboBoxField.get(),'age':int(txtAge.get())}
            if Exist(person)==False:
                Register(person)
                CleanTable()
                Load()
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
    table.insert('','end',values=[person['name'],person['family'],person['field'],person['age']])
def CleanTable():
    for item in table.get_children():
        table.delete(item)
def CleanTextBoxAfterUseCrud():
    Name.set('')
    Family.set('')
    comboBoxField.set('computer')
    Age.set('')
    txtName.focus_set()
def ActiveBtn(e):
    #print('ActiveBtn')
    if txtName.get() != '' and txtFamily.get() != '' and comboBoxField.get()!= '' and txtAge.get() != '' :
        btnRegister.configure(state=NORMAL)
    else:
        btnRegister.configure(state=DISABLED)
def Exist(person):
    allData=ReadData()
    for data in allData:
        if data['name'] == person['name'] and data['family'] == person['family'] and data['field'] == person['field'] and data['age']== person['age']:
            return True
    return False
def onClickSearch(e):
    searchRaquestUser=txtSearch.get()
    if searchRaquestUser=='':
        CleanTable()
        Load()
    else:
        result=search(searchRaquestUser)
        CleanTable()
        for data in result:
            InsertDataToTable(data)
def search(searchRaquestUser):
    resultSearch=[]
    alldata=ReadData()
    for data in alldata:
        if data['name'] == searchRaquestUser or data['family'] == searchRaquestUser or data['field'] == searchRaquestUser or str(data['age'])== searchRaquestUser:
            resultSearch.append(data)
    return resultSearch
def Load():
    alldata=ReadData()
    for data in alldata:
        InsertDataToTable(data)
def onClickDelete(e):
    dialog=messagebox.askyesno('Delete Data!','آیا از حذف دیتا خودتون مطمِنید؟')
    if dialog:
        select = table.selection()
        if select != ():
            Data = table.item(select)['values']
            person = {'name': Data[0], 'family': Data[1], 'field': Data[2],'age': int(Data[3])}
            Delete(person)
            table.delete(select)
def Delete(person):
    result=FindData(person)
    if result !=False:
        persons.delete_one(person)

def Selection(e):
    select=table.selection()
    if select !=():
        data=table.item(select)['values']
        Name.set(data[0])
        Family.set(data[1])
        comboBoxField.set(data[2])
        Age.set(data[3])
def onClickUpdate(e):
    dialog = messagebox.askyesno('Update Data!', 'آیا از تغییرات دیتا خودتون مطمِنید؟')
    if dialog:
        select = table.selection()
        if select != ():
            Data = table.item(select)['values']
            OldPerson = {'name': Data[0], 'family': Data[1], 'field': Data[2], 'age': int(Data[3])}
            NewPerson={'name':txtName.get(),'family':txtFamily.get(),'field':comboBoxField.get(),'age':int(txtAge.get())}
            Update(OldPerson,NewPerson)
            CleanTable()
            Load()
def Update(OldPerson,NewPerson):
    result=FindData(OldPerson)
    if result!=False:
        newData={'$set':NewPerson}
        persons.update_one(OldPerson,newData)

def FindData(Data):
    alldata = ReadData()
    for data in alldata:
        if data['name'] == Data['name'] and data['family'] == Data['family'] and data['field'] == Data['field'] and data['age'] == Data['age']:
            return data
    return False
def DestroyWindow(e):
    win.destroy()
#TextVariable
Name=StringVar()
Family=StringVar()
Age=StringVar()
Search=StringVar()
#image
closeImage=PhotoImage(file='images/closeImage.png')
#txt
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Name,justify='center')
txtName.bind('<KeyRelease>',ActiveBtn)
txtName.place(x=100,y=100)

txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Family,justify='center')
txtFamily.bind('<KeyRelease>',ActiveBtn)
txtFamily.place(x=100,y=160)

comboBoxField=ttk.Combobox(win,width=15,font=('arial',15,'bold'),foreground='#216ADE',background='white')
comboBoxField['values']=['computer','electronics','chemistry','physics']
comboBoxField.place(x=100,y=220)

txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Age,justify='center')
txtAge.bind('<KeyRelease>',ActiveBtn)
txtAge.place(x=100,y=280)

txtSearch=Entry(win,width=20,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',textvariable=Search,justify='center')

txtSearch.place(x=550,y=50)
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
btnRegister.bind('<Enter>',ChangeButtonStyleWithHoverRegister)
btnRegister.bind('<Leave>',ChangeButtonStyleWithHoverToSelfRegister)
btnRegister.bind('<Button-1>',onClickRegister)
btnRegister.place(x=125,y=350)

btnSearch=Button(win,text='Serach',width=10,font=('arial',15,'bold'),fg='white',background='#822FC1')

btnSearch.bind('<Enter>',ChangeButtonStyleWithHoverSearch)
btnSearch.bind('<Leave>',ChangeButtonStyleWithHoverToSelfSearch)
btnSearch.bind('<Button-1>',onClickSearch)
btnSearch.place(x=400,y=50)

btnDelete=Button(win,text='Delete',width=7,font=('arial',17,'bold'),fg='white',background='red')
btnDelete.bind('<Enter>',ChangeButtonStyleWithHover)
btnDelete.bind('<Leave>',ChangeButtonStyleWithHoverToSelf)
btnDelete.bind('<Button-1>',onClickDelete)
btnDelete.place(x=690,y=330)

btnUpdate=Button(win,text='Update',width=7,font=('arial',17,'bold'),fg='white',background='#822FC1')
btnUpdate.bind('<Enter>',ChangeButtonStyleWithHover)
btnUpdate.bind('<Leave>',ChangeButtonStyleWithHoverToSelf)
btnUpdate.bind('<Button-1>',onClickUpdate)
btnUpdate.place(x=400,y=330)

CloseBtn=Button(win,image=closeImage,height=50,width=100)
CloseBtn.bind('<Button-1>',DestroyWindow)
CloseBtn.place(x=10,y=10)

#tbl
columns=('Name','Family','field','Age')
table=ttk.Treeview(win,columns=columns,show='headings')
"""
table.heading('name',text='Name')
table.heading('family',text='Family')
table.heading('field',text='field')
table.heading('age',text='Age')
table.column('name',width=100)
table.column('family',width=100)
table.column('field',width=100)
table.column('age',width=100)
"""
for i in range(len(columns)):
    table.heading(columns[i],text=columns[i])
    table.column(columns[i],width=100,anchor='center')
table.bind('<Button-1>',Selection)
table.place(x=400,y=100)
Load()
win.mainloop()