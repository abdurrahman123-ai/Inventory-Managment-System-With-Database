from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierclass
from category import categoryclass
from product import productclass
from sales import salesclass

class IMS:
    def __init__(self, root):
        self.root = root
        
        self.root.geometry('1540x1300+0+0')
        self.root.resizable(False,False)
        self.root.title('Inventory Management System | Developed by Abdurrahman Abdulcelil')

       
        img = Image.open('images/large.png')
        img = img.resize((90, 80))
        
        self.icon_title = ImageTk.PhotoImage(img)

        
        title = Label(self.root,
                      text='Inventory Management System',
                      image=self.icon_title,
                      compound='left',
                      font=('times new roman',40,'bold'),
                      bg='green',
                      fg='white',
                      anchor='w')

        title.pack(fill=X, padx=8, ipady=10)
        
        btn_logout=Button(self.root, text='Logout',font=('times new roman',15,'bold'),bg='yellow',cursor='hand2').place(x=1340,y=30,height=50,width=150)
        # ------clock---------
        self.lbl_clock=Label(self.root,text='inventory Managment System \t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS',font=('TIMES NEW ROMAN',15),bg="#4d636d",fg='white')
        self.lbl_clock.place(x=7,y=100,relwidth=1,height=70)
        
        #-------left Menu--------
        self.MenuLogo = Image.open('images/logo2.png')
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        
        
        
        leftMenu=Frame(self.root,bd=2,relief=RIDGE)
        leftMenu.place(x=7,y=170,width=250,height=670)
        
        
        lbl_Menuloge=Label(leftMenu,image=self.MenuLogo)
        lbl_Menuloge.pack(side=TOP,fill=X)
        
        
        img = Image.open('images/rightarro.png')
        img = img.resize((20, 20))
        
        self.icon_side = ImageTk.PhotoImage(img)
        
        
        
        
        
        labl_Menu=Label(leftMenu,text='Menu',font=('times new roman',20),bg='#009688').pack(side=TOP,fill=X)
        btn_Employee=Button(leftMenu,text='Employee', command=self.employee,image=self.icon_side,compound=LEFT,padx=10,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP, fill=X)
        btn_Supplier=Button(leftMenu,text='Supplier',image=self.icon_side,command=self.supplier,compound=LEFT,padx=10,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP, fill=X)
        btn_Category=Button(leftMenu,text='Category',image=self.icon_side,command=self.category,compound=LEFT,padx=10,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP, fill=X)
        btn_Products=Button(leftMenu,text='Products',image=self.icon_side,command=self.product,compound=LEFT,padx=10,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP, fill=X)
        btn_Sales=Button(leftMenu,text='Sales',image=self.icon_side,command=self.sales,compound=LEFT,padx=10,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP, fill=X)
        btn_Exit=Button(leftMenu,text='Exit',image=self.icon_side,command=LEFT,compound=LEFT,padx=10,anchor='w',font=('times new roman',20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP, fill=X)
        
        # _____________content______________
        
        
        self.lbl_employee=Label(self.root,text='Total Employee\n[0] ',bd=5,relief=RIDGE,bg='green',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_employee.place(x=300,y=180,height=150,width=300)
        
        self.lbl_Supplier=Label(self.root,text='Total Supplier\n[0] ',bd=5,relief=RIDGE,bg='red',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_Supplier.place(x=700,y=180,height=150,width=300)
        
        
        self.lbl_Category=Label(self.root,text='Total Category \n[0] ',bd=5,relief=RIDGE,bg='gray',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_Category.place(x=1100,y=180,height=150,width=300)
        
        
        self.lbl_Product=Label(self.root,text='Total Product\n[0] ',bd=5,relief=RIDGE,bg='#D3F527',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_Product.place(x=300,y=400,height=150,width=300)
        
        
        self.lbl_Sales=Label(self.root,text='Total Sales\n[0] ',bd=5,relief=RIDGE,bg='#27F527',fg='white',font=('goudy old style',20,'bold'))
        self.lbl_Sales.place(x=700,y=400,height=150,width=300)
        
        
        
        
        
        
        
     #_____________foter________________
       
        lbl_footer = Label(
    self.root,
    text='IMS - Inventory Management System | Developed by Abdurrahman Abdulcelil\nFor any technical issue contact: 54444877730',
    font=('times new roman',12),
    bg='#4d636d',
    fg='white'
)

        lbl_footer.place(x=7, y=740, relwidth=1, height=90)
        
        #_____________________________
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)
        
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)    
        
        
    def sales(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=salesclass(self.new_win)
       
       
        
        
        
        
        
        
        

if __name__=='__main__': 
    root = Tk()
    obj = IMS(root)
    root.mainloop()