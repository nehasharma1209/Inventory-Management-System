import imp
from itertools import product
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import tkinter
import os


from tkinter import *
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("login System | Developed By Team-99 ")
        self.root.geometry("350x460+550+150")
        self.root.config(bg="#fafafa")
        #===================================

        #========Login Frame=======
        self.employee_id=StringVar()
        self.securitycode=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=0,y=0,width=350,height=460)

        title=Label(login_frame,text="Admin_Login",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Admin ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        text_username=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="security Code",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        text_pass=Entry(login_frame,textvariable=self.securitycode,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Login In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        btn_sign_in=Button(login_frame,command=self.sign_in,text="Sign In",font=("times new roman",13,"bold"),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=130,y=350,width=80,height=30)




    def login(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.securitycode.get()=="":
                messagebox.showerror('Error','All fields are required',parent=self.root)
            else:
                cur.execute("Select utype from employee where eid=%s AND securitycode=%s",(self.employee_id.get(),self.securitycode.get()))  
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error','Invalid Admin Id/Security Code',parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    '''else:
                        self.root.destroy()
                        os.system("python billing.py")'''
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    
    def sign_in(self):
       
        self.root.destroy()
        os.system("python register.py")




root=Tk()
obj=login_system(root)
root.mainloop()