from tkinter import *
from tkinter.messagebox import *
from pymongo import *
class user:
    def check(self):
        if self.tf1.get()=="":
            showinfo("","Enter id before pressing enter")
        else:
            myclient = MongoClient("mongodb://localhost:27017/")
            mydb = myclient["employee"]
            mycol = mydb["employee_data"]
            myquery = {"eid": self.tf1.get()}
            result=mycol.find_one(myquery)
            self.lb4["text"]=result["eid"]
            self.lb5["text"] = result["name"]
            self.lb6["text"] = result["Age"]
            self.lb7["text"] = result["Post"]
            self.lb8["text"] = result["salary"]

    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Welcome User:")
        self.lb1.grid(row=0,column=1)
        self.lb2=Label(self.root,text="Enter your employee id:")
        self.tf1=Entry(self.root,text="")
        self.lb2.grid(row=1,column=0)
        self.tf1.grid(row=1,column=1)
        self.b1=Button(self.root,text="Enter",command=self.check)
        self.b1.grid(row=2,column=1)
        self.lb3=Label(self.root,text="Your details!!").grid(row=3,column=1)
        self.lb4=Label(self.root,text="")
        self.lb5 = Label(self.root, text="")
        self.lb6 = Label(self.root, text="")
        self.lb7 = Label(self.root, text="")
        self.lb8= Label(self.root, text="")
        self.lb4.grid(row=4,column=1)
        self.lb5.grid(row=5, column=1)
        self.lb6.grid(row=6, column=1)
        self.lb7.grid(row=7, column=1)
        self.lb8.grid(row=8, column=1)
        self.l1=Label(self.root,text="Employee id").grid(row=4,column=0)
        self.l2 = Label(self.root, text="Name").grid(row=5, column=0)
        self.l3 = Label(self.root, text="Age").grid(row=6, column=0)
        self.l4 = Label(self.root, text="Post").grid(row=7, column=0)
        self.l1 = Label(self.root, text="Salary").grid(row=8, column=0)

        self.root.mainloop()
