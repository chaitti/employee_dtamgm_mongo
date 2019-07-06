
from pymongo import *
from tkinter import *
from tkinter.ttk import *
class view:
    def __init__(self):
        self.root=Tk()
        self.t1=Treeview(self.root,columns=("eid","name","Age","Post","salary"))
        self.t1.heading("eid", text="Employee_Id")
        self.t1.heading("name",text="Employee_Name")
        self.t1.heading("Age",text="Age")
        self.t1.heading("Post",text="Post")
        self.t1.heading("salary",text="Salary")
        self.t1["show"]="headings"
        myclient = MongoClient("mongodb://localhost:27017/")
        mydb = myclient["employee"]
        mycol = mydb["employee_data"]
        result=mycol.find({})
        i=0
        for row in result:
            self.t1.insert("",index=i,value=[row["eid"],row["name"],row["Age"],row["Post"],row["salary"]])
            i=i+1
        self.t1.pack()
        self.root.mainloop()
