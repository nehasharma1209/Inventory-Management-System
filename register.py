from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import time
import os

from setuptools import Command

class registerClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Register")
        self.root.config(bg="honeydew1")#honeydew3
        self.root.focus_force()
        #===========================
        #All variable
    

        self.var_emp_id=StringVar()
        self.var_emp_gender=StringVar()
        self.var_emp_contact=StringVar()
        self.var_emp_name=StringVar()
        self.var_emp_dob=StringVar()
        self.var_emp_doj=StringVar()
        self.var_emp_email=StringVar()
        self.var_emp_pass=StringVar()
        self.var_emp_utype=StringVar()
        self.var_emp_salary=StringVar()
        #========title====
        title=Label(self.root,text="Welcome to Inventory Managment ",font=("Fake Receipt",45),bg="honeydew1",fg="gray2").place(x=30,y=30)

        title=Label(self.root,text="-------------------------First Time Regitration------------------------",font=("Cancun",20),bg="honeydew1",fg="green").place(x=50,y=100)

        title=Label(self.root,text="Note: Email must be correct,It will help you to recover Password",font=("Caslon Bd BT",20,"bold"),bg="honeydew1",fg="red2").place(x=60,y=430)



        #========content=======
        #  row1=====

        lbl_empid=Label(self.root,text="Emp ID",font=("times new roman",15,"bold"),bg="honeydew1").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15,"bold"),bg="honeydew1").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,"bold"),bg="honeydew1").place(x=700,y=150)


        txt_empid=Entry(self.root,textvariable=self.var_emp_id,command=self.empid(),state=DISABLED,font=("times new roman",15,"bold"),bg="ivory3").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_emp_gender,values=("male","female","other"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_emp_contact,font=("times new roman",15,"bold"),bg="ivory3").place(x=850,y=150,width=180)


        #============row 2

        lbl_name=Label(self.root,text="Name",font=("times new roman",15,"bold"),bg="honeydew1").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B.",font=("times new roman",15,"bold"),bg="honeydew1").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J.",font=("times new roman",15,"bold"),bg="honeydew1").place(x=700,y=190)

        txt_name=Entry(self.root,textvariable=self.var_emp_name,font=("times new roman",15,"bold"),bg="ivory3").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_emp_dob,font=("times new roman",15,"bold"),bg="ivory3").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_emp_doj,font=("times new roman",15,"bold"),bg="ivory3").place(x=850,y=190,width=180)


        #row 3============
        lbl_email=Label(self.root,text="Email",font=("times new roman",15,"bold"),bg="honeydew1").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("times new roman",15,"bold"),bg="honeydew1").place(x=350,y=230)
        lbl_ytype=Label(self.root,text="User type",font=("times new roman",15,"bold"),bg="honeydew1").place(x=700,y=230)

        txt_email=Entry(self.root,textvariable=self.var_emp_email,font=("times new roman",15,"bold"),bg="ivory3").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_emp_pass,font=("times new roman",15,"bold"),bg="ivory3").place(x=500,y=230,width=180)
        txt_utype=Entry(self.root,textvariable=self.var_emp_utype,font=("times new roman",15,"bold"),bg="ivory3").place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_emp_utype,values=("Employee","Admin"),state='readonly',justify=CENTER,font=("times new roman",15,"bold"))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #row 4============
        lbl_adress=Label(self.root,text="Address",font=("times new roman",15,"bold"),bg="honeydew1").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("times new roman",15,"bold"),fg="black",bg="honeydew1").place(x=500,y=270)

        self.txt_address=Text(self.root,font=("times new roman",15,"bold"),bg="ivory3")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        self.var_emp_salary.set("NA")
        txt_salary=Entry(self.root,textvariable=self.var_emp_salary,state=DISABLED,font=("times new roman",15,"bold"),bg="ivory3").place(x=600,y=270,width=180)
       


        #====button 
        btn_register=Button(self.root,text="Register",command=self.register,font=("Elephant",23),cursor="hand2",bg="#2196f3",fg="gray2").place(x=350,y=355,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Elephant",23,"bold"),cursor="hand2",bg="red",fg="honeydew1").place(x=550,y=355,height=40)




       

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def register(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_emp_pass.get()==""or self.var_emp_gender.get()=="" or self.var_emp_contact.get()=="" or self.var_emp_name.get()=="" or self.var_emp_dob.get()=="" or self.var_emp_doj.get()=="" or self.var_emp_email.get()=="":
                messagebox.showerror("Error","All fields are Required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=%s",(self.var_emp_id.get(),))  
                row=cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","this Employee ID already asigned ,try different",parent=self.root)
                else:
                        
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,password,utype,address,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_emp_id.get(),
                                        self.var_emp_name.get(),
                                        self.var_emp_email.get(),
                                        self.var_emp_gender.get(),
                                        self.var_emp_contact.get(),
                                       
                                        self.var_emp_dob.get(),
                                        self.var_emp_doj.get(),
                                        
                                        self.var_emp_pass.get(),
                                        self.var_emp_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_emp_salary.get(),
                    ))
                    con.commit()
                    #messagebox.showinfo("Success","Employee Added Successfully",parent=self.root)
                    #os.system("python login.py")
                    
                    if self.var_emp_id.get()=="":
                            messagebox.showerror('Error','All fields are required',parent=self.root)
                    else:
                            cur.execute("Select utype from employee where eid=%s ",(self.var_emp_id.get()))  
                            user=cur.fetchone()
                    if user==None:
                            messagebox.showerror('Error','Invalid USERNAME/PASSOWRD',parent=self.root)
                    else:
                            if user[0]=="Admin":
                                self.root.destroy()
                                os.system("python login2.py")
                            else:
                                self.root.destroy()
                                os.system("python login.py")


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   
            
    def clear(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_emp_email.set("")
        self.var_emp_gender.set("Select")
        self.var_emp_contact.set("")
        
        self.var_emp_dob.set("")
        self.var_emp_doj.set("")
        
        self.var_emp_pass.set("")
        self.var_emp_utype.set("Admin")
        self.var_emp_salary.set("")
        self.empid()
    
    def empid(self):
            self.var_int_empid=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
            #print(self.var_emp_id)
            #result=self.var_emp_id.insert()
            #self.var_emp_id.set(result)

            xnum=self.var_emp_id.get()+str(self.var_int_empid)
            self.var_emp_id.set(xnum)

if __name__=="__main__":
    root=Tk()
    obj=registerClass(root)
    root.mainloop()         