from tkinter import*
import os
import pymysql
from tkinter import messagebox
from employee import employeeclass
from supplier import supplierclass
from category import categoryClass
from product import productClass
from sales import salesClass
import time

from PIL import Image,ImageTk #pip install pillow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#5F9EA0")
        self.root.title("Invetory Management System | Developed By Team ")

        #====title======
        #self.icon_title=PhotoImage(file="image/logo2.png")
        self.icon_title=Image.open("image/logo2.png")
        self.icon_title=self.icon_title.resize((64,64),resample=Image.LANCZOS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)

        title=Label(self.root,text="INVENTORY MANAGEMENT SYSTEM",image=self.icon_title,compound=LEFT,font=("time new roman",30,"bold"),bg="#1E1E1E",fg="white",anchor="w",padx=40).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,command=self.logout,text="Logout",font=("times new roman",15,"bold"),bg="#7AC5CD",cursor="hand2").place(x=1110,y=10,height=50,width=150)
       
        #==clock====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",font=("time new roman",15),bg="#E6E6FA",fg="black")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #======Left Menu==
        self.MenuLogo=Image.open("image/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),resample=Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=3,relief=RIDGE)
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo,bg="#CDCDC1")
        lbl_menuLogo.pack(side=TOP,fill=X)


        self.icon_side=PhotoImage(file="image/side.png")
        lbl_menu=Label(LeftMenu,text="MENU",bd=3,fg="black",font=("time new roman",20,"bold"),bg="#A3A3A3").pack(side=TOP,fill=X)

        self.icon_empl=Image.open("image/teamwork.png")
        self.icon_empl=self.icon_empl.resize((35,35),resample=Image.LANCZOS)
        self.icon_empl=ImageTk.PhotoImage(self.icon_empl)
        lbl_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_empl,compound=LEFT,padx=10,anchor="w",font=("time new roman",20),bg="#474747",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        
        self.icon_supp=Image.open("image/supplier.png")
        self.icon_supp=self.icon_supp.resize((35,35),resample=Image.LANCZOS)
        self.icon_supp=ImageTk.PhotoImage(self.icon_supp)
        lbl_supplier=Button(LeftMenu,text="Supplier",image=self.icon_supp,command=self.supplier,compound=LEFT,padx=10,anchor="w",font=("time new roman",20),bg="#4A4A4A",bd=1,cursor="hand2").pack(side=TOP,fill=X)        
        
        self.icon_cate=Image.open("image/category.png")
        self.icon_cate=self.icon_cate.resize((35,35),resample=Image.LANCZOS)
        self.icon_cate=ImageTk.PhotoImage(self.icon_cate)
        lbl_Category=Button(LeftMenu,text="Category",image=self.icon_cate,command=self.category, compound=LEFT,padx=10,anchor="w",font=("time new roman",20),bg="#575757",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        
        self.icon_pro=Image.open("image/gift.png")
        self.icon_pro=self.icon_pro.resize((35,35),resample=Image.LANCZOS)
        self.icon_pro=ImageTk.PhotoImage(self.icon_pro)
        lbl_Product=Button(LeftMenu,text="Product",image=self.icon_pro,command=self.product,compound=LEFT,padx=10,anchor="w",font=("time new roman",20),bg="#6B6B6B",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        
        self.icon_sales=Image.open("image/sales.png")
        self.icon_sales=self.icon_sales.resize((35,35),resample=Image.LANCZOS)
        self.icon_sales=ImageTk.PhotoImage(self.icon_sales)
        lbl_Sales=Button(LeftMenu,text="Sales",image=self.icon_sales,command=self.sales,compound=LEFT,padx=10,anchor="w",font=("time new roman",20),bg="#7D7D7D",bd=1,cursor="hand2").pack(side=TOP,fill=X)
        
        self.icon_exit=Image.open("image/logout.png")
        self.icon_exit=self.icon_exit.resize((35,35),resample=Image.LANCZOS)
        self.icon_exit=ImageTk.PhotoImage(self.icon_exit)
        lbl_Exit=Button(LeftMenu,text="Exit",image=self.icon_exit,compound=LEFT,padx=10,anchor="w",font=("time new roman",20),bg="#7D7D7D",bd=1,cursor="hand2").pack(side=TOP,fill=X)

        #======content=====
        self.icon_emplo=Image.open("image/teamwork2.png")
        self.icon_emplo=self.icon_emplo.resize((60,60),resample=Image.LANCZOS)
        self.icon_emplo=ImageTk.PhotoImage(self.icon_emplo)
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",image=self.icon_emplo,compound=LEFT,padx=20,relief=RIDGE,bd=4,bg="#FFE1FF",font=("goudy old style",15,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.icon_suppl=Image.open("image/supplier2.png")
        self.icon_suppl=self.icon_suppl.resize((60,60),resample=Image.LANCZOS)
        self.icon_suppl=ImageTk.PhotoImage(self.icon_suppl)
        self.lbl_Supplier=Label(self.root,text="Total Supplier\n[0]",image=self.icon_suppl,bd=4,compound=LEFT,padx=20,relief=RIDGE,bg="#FFE1FF",fg="black",font=("goudy old style",15,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)
        

        self.icon_categ=Image.open("image/category2.png")
        self.icon_categ=self.icon_categ.resize((60,60),resample=Image.LANCZOS)
        self.icon_categ=ImageTk.PhotoImage(self.icon_categ)
        self.lbl_category=Label(self.root,text="Total Category\n[0]",image=self.icon_categ,compound=LEFT,padx=20,bd=4,relief=RIDGE,bg="#FFE1FF",fg="black",font=("goudy old style",15,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.icon_prod=Image.open("image/gift2.png")
        self.icon_prod=self.icon_prod.resize((60,60),resample=Image.LANCZOS)
        self.icon_prod=ImageTk.PhotoImage(self.icon_prod)
        self.lbl_Product=Label(self.root,text="Total Product\n[0]",image=self.icon_prod,bd=4,compound=LEFT,padx=20,relief=RIDGE,bg="#FFE1FF",fg="black",font=("goudy old style",15,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)
        
        self.icon_sale=Image.open("image/sales2.png")
        self.icon_sale=self.icon_sale.resize((60,60),resample=Image.LANCZOS)
        self.icon_sale=ImageTk.PhotoImage(self.icon_sale)
        self.lbl_Sales=Label(self.root,text="Total Sales\n[0]",image=self.icon_sale,compound=LEFT,bd=4,padx=20,relief=RIDGE,bg="#FFE1FF",fg="black",font=("goudy old style",15,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)
        
        
        #==footer====
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By TEAM\nFor any Technical Issue Contact:83499xxxxx",font=("time new roman",15),bg="#E6E6FA",fg="black").pack(side=BOTTOM,fill=X)
        self.update_content()
#==========================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)




    def update_content(self):
        con=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="ims")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Product.config(text=f'Total Products\n[{str(len(product))}]')
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_Supplier.config(text=f'Total Suppliers\n[{str(len(supplier))}]')
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[{str(len(employee))}]')
            
            bill=len(os.listdir('bill'))
            self.lbl_Sales.config(text=f'Total Sales[{str(bill)}]')
            
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:{str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")



if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()