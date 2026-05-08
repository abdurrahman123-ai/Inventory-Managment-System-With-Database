from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
class Billclass:
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
        
        self.var_search=StringVar()
        
        
        
        
        
        
        

        title.pack(fill=X, padx=8, ipady=10)
        
        btn_logout=Button(self.root, text='Logout',font=('times new roman',15,'bold'),bg='yellow',cursor='hand2').place(x=1340,y=30,height=50,width=150)
        # ------clock---------
        self.lbl_clock=Label(self.root,text='inventory Managment System \t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS',font=('TIMES NEW ROMAN',15),bg="#4d636d",fg='white')
        self.lbl_clock.place(x=7,y=100,relwidth=1,height=70)


# ________________product Frame__________________
        self.var_search=StringVar()

        
        productFrame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        productFrame1.place(x=6,y=180,width=410,height=600)


        pTitle=Label(productFrame1,text='All Products',font=('goudy old style',20,'bold'),bg='#262626',fg='white')
        pTitle.pack(side=TOP,fill=X)
        
        
        productFrame2=Frame(productFrame1 ,bd=2,relief=RIDGE,bg='white')
        productFrame2.place(x=6,y=42,width=400,height=90)
        
        
        lbl_search=Label(productFrame2,text='Search Product | By Name',font=("times new roman",15,'bold'),fg='black')
        lbl_search.place(x=1,y=1)


        txt_search=Label(productFrame2,text='Product Name:',relief='groove',fg='green',font=('goudy old style',15))
        txt_search.place(x=1,y=50)
        
        ent_search=Entry(productFrame2,bg='lightyellow',textvariable=self.var_search,font=('times new roman',12),fg='black')
        ent_search.place(x=130,y=50,width=120,height=28)
        
        btn_search=Button(productFrame2,text='Search',command=self.search,cursor='hand2',font=('goudy old style',15),bg='red',fg='white')
        btn_search.place(x=260,y=50,width=120,height=28)
        
        btn_show=Button(productFrame2,text='Show',command=self.show,cursor='hand2',font=('goudy old style',15),bg='#2196f3',fg='white')
        btn_show.place(x=260,y=20,width=120,height=28)
        
        
        #__________product_Details__________
        
        productFrame3=Frame(self.root,bd=3,relief=RIDGE)
        productFrame3.place(x=6,y=320,width=410,height=465)
        
        scrrolly=Scrollbar(productFrame3,orient=VERTICAL)
        scrrollx=Scrollbar(productFrame3,orient=HORIZONTAL)
        
        
        self.product_Table = ttk.Treeview(productFrame3, columns=('pid','Name','price','qty','status'),show='headings')
        for col in ('pid','Name','price','qty','status'):
         self.product_Table.column(col, width=135)
        
        scrrollx.pack(side=BOTTOM,fill=X)
        scrrolly.pack(side=RIGHT,fill=Y)
        scrrollx.config(command=self.product_Table.xview)
        scrrolly.config(command=self.product_Table.yview)
        
        
        self.product_Table.configure(xscrollcommand=scrrollx.set,
                             yscrollcommand=scrrolly.set)
        
        
        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("Name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Qty")
        self.product_Table.heading('status',text='Status')
        
        self.product_Table["show"] = "headings"  
        
        self.product_Table.column('pid',width=40)
        self.product_Table.column('Name',width=60)

        self.product_Table.column('price',width=40)

        self.product_Table.column('qty',width=40)
        self.product_Table.column('status',width=40)
        
        
        
        
        
        
        
            
        self.product_Table.pack(fill=BOTH, expand=1)
       # self.productTabel.bind("<ButtonRelease-1>", self.get_data)
        #self.show()
        
        lbl_note=Label(productFrame3,text='Note Enter 0 Quantity to remove product from the Cart',font=('goudy old style',12),anchor='w',bg='white',fg='red')
        lbl_note.pack(side=BOTTOM,fill=X)
        
        #___________________customer Frame _________________
        
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        CustomerFrame.place(x=420,y=180,width=530,height=70)
        
        custemer_txt=Label(CustomerFrame,text='Customer Details',font=('goudy old style',15,'bold'),bg='green',fg='white',justify='center')
        custemer_txt.pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text='Name :',bg='white',fg='black',font=('goudy old style',15))
        lbl_name.place(x=1,y=30)
        
        ent_name=Entry(CustomerFrame,textvariable=self.var_name,bg='lightyellow',justify='center')
        ent_name.place(x=70,y=33,height=25,width=150)
        
        
        lbl_contact=Label(CustomerFrame,text='Contact :',bg='white',fg='black',font=('goudy old style',15))
        lbl_contact.place(x=280,y=30)
        
        ent_contact=Entry(CustomerFrame,textvariable=self.var_contact,bg='lightyellow',justify='center')
        ent_contact.place(x=370,y=33,height=25,width=150)
        
        cal_cart_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        cal_cart_frame.place(x=415,y=250,width=535,height=380)
        
        Cal_Frame=Frame(cal_cart_frame,bd=2,relief=RIDGE,bg='white')
        Cal_Frame.place(x=5,y=10,width=270,height=360)
        
        
        #__________price_Details__________
        
        CartFrame=Frame(cal_cart_frame,bd=3,relief=RIDGE)
        CartFrame.place(x=280,y=10,width=250,height=360)
        lbl_cart_frame=Label(CartFrame,text='Cart     Total Product[0]',bg='gray',font=('goudy old style',15) )
        lbl_cart_frame.pack(fill=X,side=TOP)
        
        scrrolly=Scrollbar(CartFrame,orient=VERTICAL)
        scrrollx=Scrollbar(CartFrame,orient=HORIZONTAL)
        
        
        self.CartTable = ttk.Treeview(CartFrame, columns=('pid','Name','price','qty','status'),show='headings')
        for col in ('pid','Name','price','qty','status'):
         self.CartTable.column(col, width=75)
        
        scrrollx.pack(side=BOTTOM,fill=X)
        scrrolly.pack(side=RIGHT,fill=Y)
        scrrollx.config(command=self.CartTable.xview)
        scrrolly.config(command=self.CartTable.yview)
        
        
        self.CartTable.configure(xscrollcommand=scrrollx.set,
                             yscrollcommand=scrrolly.set)
        
        
        self.CartTable.heading("pid", text="PID")
        self.CartTable.heading("Name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="Qty")
        self.CartTable.heading('status',text='Status')
        
        self.CartTable["show"] = "headings"      
        self.CartTable.pack(fill=BOTH, expand=1)
       # self.CartTable.bind("<ButtonRelease-1>", self.get_data)
        #self.show()
        
        #Add Cart Wedgets
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        
        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Add_CartWidgetsFrame.place(x=420,y=630,width=530,height=155)
        
        
        lbl_name=Label(Add_CartWidgetsFrame,text='Product Name :',font=('new times roman',15),fg='black')
        lbl_name.place(x=1,y=1)
        
        txt_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_name,bg='lightyellow',justify='center',font=('goudy old style',15))
        txt_name.place(x=1,y=40,height=28,width=150)
        
        
        lbl_price=Label(Add_CartWidgetsFrame,text='Price Per Qty :',font=('times new roman',15),fg='black')
        lbl_price.place(x=200,y=1)
        
        txt_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,bg='lightyellow',justify='center',font=('goudy old style',15))
        txt_price.place(x=180,y=40,height=28,width=150)
        
        
        lbl_p_qty=Label(Add_CartWidgetsFrame,text='Quantity :',font=('times new roman',15),fg='black')
        lbl_p_qty.place(x=400,y=1)
        
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,bg='lightyellow',justify='center',font=('goudy old style',15))
        txt_p_qty.place(x=370,y=40,height=28,width=150)
        
        
        self.lbl_instock=Label(Add_CartWidgetsFrame,text='In Stock [999]',font=('times new roman',15),bg='white')
        self.lbl_instock.place(x=5,y=100)
        
        
        
        btn_cleare_cart=Button(Add_CartWidgetsFrame,text='Clear',font=('times new roman',15,'bold'),bg='lightgray')
        btn_cleare_cart.place(x=180,y=100,width=150,height=27)
        
        btn_add_update_cart=Button(Add_CartWidgetsFrame,text='Add | Update Cart',font=('times new roman',15),bg='orange')
        btn_add_update_cart.place(x=360,y=100,width=150,height=27)
        
        
        #__________________Calculator Frame_____________________
        self.var_cal_input=StringVar()
               
        self.txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=22,bd=10,relief='groove')
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        
        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor='hand2')
        btn_7.place(x=6,y=47)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor='hand2')
        btn_8.place(x=70,y=47)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor='hand2')
        btn_9.place(x=134,y=47)
        btn_plus=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor='hand2')
        btn_plus.place(x=198,y=47)
        
        
        
        
        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor='hand2')
        btn_4.place(x=6,y=120)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor='hand2')
        btn_5.place(x=70,y=120)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor='hand2')
        btn_6.place(x=134,y=120)
        btn_miness=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor='hand2')
        btn_miness.place(x=198,y=120)
        
        
        
        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor='hand2')
        btn_1.place(x=6,y=193)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor='hand2')
        btn_2.place(x=70,y=193)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor='hand2')
        btn_3.place(x=134,y=193)
        btn_dot=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor='hand2')
        btn_dot.place(x=198,y=193)
        
        
        
        btn_zero=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=10,cursor='hand2')
        btn_zero.place(x=6,y=266)
        btn_c=Button(Cal_Frame,text='c',command=self.clear_cal,font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_c.place(x=70,y=266)
        btn_equal=Button(Cal_Frame,text='=',command=self.perform_cal,font=('arial',15,'bold'),bd=5,width=4,pady=10,cursor='hand2')
        btn_equal.place(x=134,y=266)
        btn_divide=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=10,cursor='hand2')
        btn_divide.place(x=198,y=266)
        
        
        
        
        #__________________billing area___________________
        
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=950,y=180,width=570,height=450)
        
        
        Billtitle=Label(billFrame,text='Customer Bill Area',font=('goudy old style',20,'bold'),bg='#262626',fg='white')
        Billtitle.pack(fill=X,side=TOP)
        
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_Area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_Area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_Area.yview)
        
        
        #________________billing buttoms________________
        
        
        billMenuFrame=Frame(self.root,relief=RIDGE,bg='gray')
        billMenuFrame.place(x=950,y=640,width=570,height=145)
        
        
        self.bill_amnt=Button(billMenuFrame,text='Bill Amont\n[0]',font=('goudy old style',15,'bold'),bg='green',fg='black')
        self.bill_amnt.place(x=5,y=1,width=180,height=60)
        
        self.bill_discount=Button(billMenuFrame,text='Discount \n[5%]',font=('goudy old style',15,'bold'),bg='red',fg='black')
        self.bill_discount.place(x=190,y=1,width=180,height=60)
        
        self.new_py=Button(billMenuFrame,text='net pay \n[0]',font=('goudy old style',15,'bold'),bg='gray',fg='black')
        self.new_py.place(x=380,y=1,width=180,height=60)
        
        
        self.bill_print=Button(billMenuFrame,text='Print',font=('goudy old style',15,'bold'),bg='yellow',fg='black')
        self.bill_print.place(x=5,y=70,width=180,height=60)
        
        self.bill_clear=Button(billMenuFrame,text='Clear All',font=('goudy old style',15,'bold'),bg='lightgreen',fg='black')
        self.bill_clear.place(x=190,y=70,width=180,height=60)
        
        self.generate_save=Button(billMenuFrame,text='Generate/Save Bill',font=('goudy old style',15,'bold'),bg='lightyellow',fg='black')
        self.generate_save.place(x=380,y=70,width=180,height=60)
        
        
        #_____________footer________________
        self.show()
        
        
        
        
        
        
        
        
        
        
        
    def get_input(self,num):
        xnum=self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')  
        
    def perform_cal(self):
        result=self.var_cal_input.get()  
        self.var_cal_input.set(eval(result))  
        
        
        
    def show(self):
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute('select pid,name,price,qty,status from product')
                rows=cur.fetchall()
                self.product_Table.delete(*self.product_Table.get_children())
                for row in rows:
                 self.product_Table.insert('',END,values=row)
                    
                    
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to :{str(ex)}',parent=self.root)  

    
    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=='':
                messagebox.showerror('Error','Search iunput should be required',parent=self.root)
            else:
                cur.execute("select pid,name,price,qty,status from product where name LIKE '%"+self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                    
                else:
                    messagebox.showerror('Error','No record found !',parent=self.root)
    
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=self.root)
    
    
    
    
    
    
    
    
    







if __name__=='__main__': 
    root = Tk()
    obj = Billclass(root)
    root.mainloop()



















































