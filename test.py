from tkinter import *
from tkinter import ttk

win=Tk()
win.geometry('800x400')
"""
def sayHello():
    print("Hello")

sayHello()

def ChangeButtonStyleWithHover(e):
    btnRegister.configure(fg='#822FC1',background='white')
def ChangeButtonStyleWithHoverToSelf(e):
    btnRegister.configure(fg='white',background='#822FC1')
"""
def CleanTable():
    for item in table.get_children():
        table.delete(item)
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
    table.column(columns[i],width=100)
table.place(x=400,y=100)
table.insert('','end',values=['Name','Family','Feild','age'])
table.insert('','end',values=['Name','Family','Feild','age'])
table.insert('','end',values=['Name','Family','Feild','age'])

CleanTable()

txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),fg='#216ADE',bg='white',justify='center')
txtName.place(x=100,y=100)
print(txtName.cget('width'))
win.mainloop()

"""
import tkinter as tk

def on_button_click(event):
    print(f"{event.widget['text']} clicked")

root = tk.Tk()

buttons = []
button_texts = ["Button 1", "Button 2", "Button 3"]

for text in button_texts:
    button = tk.Button(root, text=text)
    button.pack()
    button.bind("<Button-1>", on_button_click)
    buttons.append(button)

root.mainloop()"""