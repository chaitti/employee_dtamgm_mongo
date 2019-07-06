from tkinter import *
from pymongo import *
from tkinter.messagebox import *
class delete:
    def search(self):
        if self.tf5.get()=="":
            showinfo("","Enter Employye id")
        else:
            myclient = MongoClient("mongodb://localhost:27017/")
            mydb = myclient["employee"]
            mycol = mydb["employee_data"]
            myquery = {"eid": self.tf5.get()}
            result=mycol.find_one(myquery)
            self.tf1.insert(0,result["name"])
            self.tf2.insert(0, result["Age"])
            self.tf3.insert(0, result["Post"])
            self.tf4.insert(0, result["salary"])


    def delete(self):
        myclient = MongoClient("mongodb://localhost:27017/")
        mydb = myclient["employee"]
        mycol = mydb["employee_data"]
        myquery = {"eid": self.tf5.get()}
        mycol.delete_one(myquery)
        showinfo("","Row deleted!!!!!!!")
        self.tf1.delete(0,END)
        self.tf2.delete(0, END)
        self.tf3.delete(0, END)
        self.tf4.delete(0, END)
        self.tf5.delete(0, END)
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Enter Employee details:").grid(row=0,column=1)
        self.lb2=Label(self.root,text="Name").grid(row=2,column=0)
        self.lb6 = Label(self.root, text="Employee id").grid(row=1, column=0)
        self.lb3 = Label(self.root, text="Age").grid(row=3,column=0)
        self.lb4 = Label(self.root, text="Post").grid(row=4,column=0)
        self.lb5 = Label(self.root, text="Salary").grid(row=5,column=0)
        self.tf1=Entry(self.root,text="")
        self.tf2 = Entry(self.root, text="")
        self.tf3 = Entry(self.root, text="")
        self.tf4 = Entry(self.root, text="")
        self.tf5 = Entry(self.root, text="")
        self.tf1.grid(row=2,column=1)
        self.tf2.grid(row=3, column=1)
        self.tf3.grid(row=4, column=1)
        self.tf4.grid(row=5, column=1)
        self.tf5.grid(row=1,column=1)
        self.bt1=Button(self.root,text="delete",command=self.delete)
        self.bt2=Button(self.root,text="search",command=self.search)
        self.bt1.grid(row=6,column=1)
        self.bt2.grid(row=1,column=2)
        self.root.mainloop()
