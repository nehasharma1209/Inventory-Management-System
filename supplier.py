from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import time 
import os

class supplierclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1150x510+200+133")
        self.root.title("Supplier")
        self.root.config(bg="honeydew1")
        self.root.focus_force()
        #===========================
        #All variable
        self.var_emp_searchby=StringVar()
        self.var_emp_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()


        #======searchFrame==========

        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",15,"bold"),bd=2,relief=RIDGE,bg="honeydew1")
        SearchFrame.place(x=250,y=29,width=680,height=70)

        #=========option=========
        lbl_search=Label(SearchFrame,text="Search By Invoice No",bg="honeydew1",font=("goudy old style",15))
        lbl_search.place(x=10,y=10)


        txt_search=Entry(SearchFrame,textvariable=self.var_emp_searchtxt,font=("goudy old style",15,"bold"),bg="ivory3").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15,"bold"),cursor="hand2",bg="#4caf50",fg="white").place(x=430,y=9,width=150,height=30)


        #========title====
        title=Label(self.root,text="Supplier Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


        #========content=======
        #  row1=====

        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="honeydew1").place(x=50,y=150)


        txt_supplier_invoce=Entry(self.root,textvariable=self.var_sup_invoice,command=self.empid(),font=("gaudy old style",15),bg="ivory3").place(x=150,y=150,width=180)


        #============row 2

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="honeydew1").place(x=50,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="ivory3").place(x=150,y=190,width=180)


        #row 3============
        lbl_contact=Label(self.root,text="contact",font=("goudy old style",15),bg="honeydew1").place(x=50,y=230)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="ivory3").place(x=150,y=230,width=180)

        #row 4============
        lbl_description=Label(self.root,text="description",font=("goudy old style",15),bg="honeydew1").place(x=50,y=270)

        self.txt_description=Text(self.root,font=("goudy old style",15),bg="ivory3")
        self.txt_description.place(x=150,y=270,width=300,height=60)


        #====button 
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15,"bold"),cursor="hand2",bg="#2196f3",fg="white").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15,"bold"),cursor="hand2",bg="green",fg="white").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15,"bold"),cursor="hand2",bg="red",fg="white").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),cursor="hand2",bg="grey",fg="white").place(x=860,y=305,width=110,height=28)




        #===========Emloyee Deatail ===========
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Invoice No")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("description",text="Description")

        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("description",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def add(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="" or self.var_name.get()=="" or self.var_contact.get()=="":
                messagebox.showerror("Error","All fields are Required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=%s",(self.var_sup_invoice.get(),))  
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Invoice no. already asigned ,try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,description) values(%s,%s,%s,%s)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_description.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   
            
    def show(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
      
    
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[9])



    def update(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be Required",parent=self.root)
            else:
               cur.execute("Select * from supplier where invoice=%s",(self.var_sup_invoice.get(),))  
               row=cur.fetchone()
               if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
               else:
                    cur.execute("Update supplier set name=%s,contact=%s,description=%s where invoice=%s",(
                                        
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_description.get('1.0',END),
                                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
              messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    def delete(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims") 
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. must be Required",parent=self.root)
            else:
               cur.execute("Select * from supplier where invoice=%s",(self.var_sup_invoice.get(),))  
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
               else:
                   op=messagebox.askyesno("Confirm","Do you really want to delete??",parent=self.root)
                   if op==True:
                        cur.execute("delete from supplier where invoice=%s",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier deleted Succesfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)      



    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_description.delete('1.0',END)
        self.var_emp_searchtxt.set("")
        self.show()
        self.empid()



    def search(self):    
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.var_emp_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice no. should be required",parent=self.root) 
            else:
                cur.execute("select * from supplier where invoice=%s",(+self.var_emp_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                     messagebox.showerror("Error","No record found!!",parent=self.root)     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def empid(self):
            self.var_int_empid=int(time.strftime("%M%S"))+int(time.strftime("%d%Y"))
            #print(self.var_emp_id)
            #result=self.var_emp_id.insert()
            #self.var_emp_id.set(result)

            xnum=self.var_sup_invoice.get()+str(self.var_int_empid)
            self.var_sup_invoice.set(xnum)


if __name__=="__main__":
    root=Tk()
    obj=supplierclass(root)
    root.mainloop()         