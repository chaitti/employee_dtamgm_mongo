from tkinter import *
from pymongo import *
from tkinter.messagebox import *
class add:
    def insert(self):

        myclient=MongoClient("mongodb://localhost:27017/")
        mydb=myclient["employee"]
        mycol=mydb["employee_data"]
        mydict={"eid":self.tf1.get(),"name":self.tf2.get(),"Age":self.tf3.get(),"Post":self.tf4.get(),"salary":self.tf5.get()}
        mycol.insert_one(mydict)
        showinfo("","Employee added!!")
        self.tf1.delete(0,END)
        self.tf2.delete(0, END)
        self.tf3.delete(0, END)
        self.tf4.delete(0, END)
        self.tf5.delete(0, END)

    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Enter Employee details:").grid(row=0,column=1)
        self.lb6 = Label(self.root, text="Employee id").grid(row=1, column=0)
        self.lb2=Label(self.root,text="Name").grid(row=2,column=0)
        self.lb3 = Label(self.root, text="Age").grid(row=3,column=0)
        self.lb4 = Label(self.root, text="Post").grid(row=4,column=0)
        self.lb5 = Label(self.root, text="Salary").grid(row=5,column=0)
        self.tf1=Entry(self.root,text="")
        self.tf2 = Entry(self.root, text="")
        self.tf3 = Entry(self.root, text="")
        self.tf4 = Entry(self.root, text="")
        self.tf5 = Entry(self.root, text="")
        self.tf1.grid(row=1,column=1)
        self.tf2.grid(row=2, column=1)
        self.tf3.grid(row=3, column=1)
        self.tf4.grid(row=4, column=1)
        self.tf5.grid(row=5,column=1)
        self.bt1=Button(self.root,text="Insert",command=self.insert)
        self.bt1.grid(row=6,column=1)
        self.root.mainloop()

