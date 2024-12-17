import imp
from itertools import product
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import tkinter
import os


from tkinter import *
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("login System | Developed By Team-99 ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        #===================================
        self.phone_image=ImageTk.PhotoImage(file="image/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #========Login Frame=======
        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login_System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        text_username=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        text_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Login In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        Or=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,command=self.forget_window,text="Forget Passwoed?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)
        btn_sign_in=Button(login_frame,command=self.sign_in,text="Sign In",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=420)

    #============Animation Image==================
        self.im1=ImageTk.PhotoImage(file="image/im1.png")
        self.im2=ImageTk.PhotoImage(file="image/im2.png")
        self.im3=ImageTk.PhotoImage(file="image/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()
    #====all function===========
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)



    def login(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error','All fields are required',parent=self.root)
            else:
                cur.execute("Select utype from employee where eid=%s AND password=%s",(self.employee_id.get(),self.password.get()))  
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error','Invalid USERNAME/PASSOWRD',parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     

    
    def sign_in(self):
       
        self.root.destroy()
        os.system("python register.py")



    def forget_window(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                cur.execute("Select email from employee where eid=%s",(self.employee_id.get()))  
                email=cur.fetchone()
                if email==None:
                     messagebox.showerror('Error','Invalid USERNAME/PASSOWRD',parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    #call send_email_function()
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title("RESET PASSWORD")
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    

                    title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),fg="black").pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP send on register email",font=("Andalus",15),fg="black").place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("Andalus",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                    
                    self.btn_reset=Button(self.forget_win,command=self.login,text="Submit",font=("Andalus",15),bg="lightblue")
                    self.btn_reset.place(x=280,y=100,width=100,height=30)

                    lbl_new_pass=Label(self.forget_win,text="New password",font=("Andalus",15),fg="black").place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_otp,font=("Andalus",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)

                    lbl_c_pass=Label(self.forget_win,text="Confirm password",font=("Andalus",15),fg="black").place(x=20,y=225)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("Andalus",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)

                    self.btn_update=Button(self.forget_win,command=self.login,text="Update",state=DISABLED,font=("Andalus",15),bg="lightblue")
                    self.btn_update.place(x=150,y=300,width=100,height=30)

                    

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)     




root=Tk()
obj=login_system(root)
root.mainloop()