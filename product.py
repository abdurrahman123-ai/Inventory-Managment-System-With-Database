from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class productclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x535+255+200')
        self.root.resizable(False,False)
        self.root.title('Inventory Management System | Developed by Abdurrahman Abdulcelil')
        self.root.config(bg='white')
        self.root.focus_force()
        
        #_______________________________________
        
        self.var_searchby=StringVar()
        self.varSearchtxt=StringVar()
        
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sub()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        
        
        
        
        #_________________________
        
        
        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        product_frame.place(x=10,y=10,width=450,height=520)
        
        
        title=Label(product_frame,text='Manage Product Details',bg='#7D27F5',fg='white',font=('goudy old style',15))
        title.pack(side=TOP,fill=X)
        
        
        lbl_category=Label(product_frame,text='Category :',font=('goudy old style',17),bg='white')
        lbl_category.place(x=30,y=60)
        lbl_supplier=Label(product_frame,text='Supplier :',font=('goudy old style',17),bg='white')
        lbl_supplier.place(x=30,y=120)
        lbl_name=Label(product_frame,text='Name :',font=('goudy old style',17),bg='white')
        lbl_name.place(x=30,y=170)
        lbl_price=Label(product_frame,text='Price :',font=('goudy old style',17),bg='white')
        lbl_price.place(x=30,y=230)
        lbl_qty=Label(product_frame,text='Quantity :',font=('goudy old style',17),bg='white')
        lbl_qty.place(x=30,y=290)
        lbl_status=Label(product_frame,text='Status :',font=('goudy old style',17),bg='white')
        lbl_status.place(x=30,y=350)
        
        
        
        #options
        self.cmb_cat = ttk.Combobox(product_frame, values=('Selcet'), textvariable=self.var_cat,
                            state='readonly', justify='center')
        self.cmb_cat.place(x=150, y=70)
        self.cmb_cat.current(0)

        self.cmb_sup = ttk.Combobox(product_frame, textvariable=self.var_sup,
                            state='readonly', justify='center')
        self.cmb_sup.place(x=150, y=130)
        
        
        
        
        
        
        
        txt_name=Entry(product_frame,textvariable=self.var_name,font=('goudy old style',12),bg='lightyellow',justify='center')
        txt_name.place(x=130,y=180)
        
        txt_price=Entry(product_frame,textvariable=self.var_price,font=('goudy old style',12),bg='lightyellow',justify='center')
        txt_price.place(x=130,y=230)
        
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=('goudy old style',12),bg='lightyellow',justify='center')
        txt_qty.place(x=140,y=300)
    
    
    
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=('Active'),state='readonly',justify='center')
        cmb_status.place(x=130,y=360)
        cmb_status.current(0)
    
    
    #_________buttons___________
    
    
        btn_save=Button(product_frame,text='Save',command=self.add,font=('goudy old style',15),bg='#1296f3',cursor='hand2')
        btn_save.place(x=10,y=420,width=110,height=35)
        btn_update=Button(product_frame,text='Update',command=self.update,font=('goudy old style',15),bg='#4caf50',cursor='hand2')
        btn_update.place(x=120,y=420,width=110,height=35)
        btn_delete=Button(product_frame,text='Delete',command=self.delete,font=('goudy old style',15),bg='#f44336',cursor='hand2')
        btn_delete.place(x=220,y=420,width=110,height=35)
        btn_clear=Button(product_frame,text='Clear',command=self.clear,font=('goudy old style',15),bg='#607d8b',cursor='hand2')
        btn_clear.place(x=320,y=420,width=110,height=35)
    
    #    __________     label frame    ________________
        SearchFrame=LabelFrame(self.root,text='Search Employee',bg='white')
        SearchFrame.place(x=590,y=20,width=600,height=70)
        
        comb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select",'Category','Supplier','Name'),state='readonly',justify='center',font=('times new roman',12))
        comb_search.place(x=10,y=10,width=180)
        comb_search.current(0)
        
        txt_Search=Entry(SearchFrame,textvariable=self.varSearchtxt,font=('goudy old style',15),bg='lightyellow')
        txt_Search.place(x=200,y=10)
        btn_search=Button(SearchFrame,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',cursor='hand2')
        btn_search.place(x=410,y=10,width=150,height=30)
    
    
        #_______________________Product_Details__________________________
        
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=600,y=110,width=600,height=400)
        
        scrrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        
        
        self.product_table = ttk.Treeview(p_frame, columns=('pid','Category','Supplier','name','price','qty','status'),show='headings')
        for col in ('pid','Category','Supplier','name','price','qty','status'):
         self.product_table.column(col, width=135)
        
        scrrollx.pack(side=BOTTOM,fill=X)
        scrrolly.pack(side=RIGHT,fill=Y)
        scrrollx.config(command=self.product_table.xview)
        scrrolly.config(command=self.product_table.yview)
        
        
        self.product_table.configure(xscrollcommand=scrrollx.set,
                             yscrollcommand=scrrolly.set)
        
        
        self.product_table.heading("pid", text="P ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("status", text="Status")
        
        
        self.product_table["show"] = "headings"
        

          
        self.product_table.column('pid',width=90)
        self.product_table.column('Category',width=100)
        self.product_table.column('Supplier',width=100)
        self.product_table.column('name',width=100)
        self.product_table.column('price',width=100)
        self.product_table.column('qty',width=100)
        self.product_table.column('status',width=100)
          
          
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind('<ButtonRelease>',self.get_data)
        self.show()
        self.fetch_cat_sub()
        self.cmb_cat['values'] = self.cat_list
        self.cmb_sup['values'] = self.sup_list
        
        self.cmb_cat.current(0)
        self.cmb_sup.current(0)
        
        
        
        #_______________________________________
        
        
    def fetch_cat_sub(self):
     self.cat_list.append('Empty')
     self.sup_list.append('Empty')

     con=sqlite3.connect(database=r'ims.db')
     cur=con.cursor()
     try:
        
         cur.execute('Select name from category')
         cat=cur.fetchall()
        
         if len(cat)>0:
             del self.cat_list[:]
             self.cat_list.append("Select")
             for i in cat:
                 self.cat_list.append(i[0])
        
         cur.execute('Select name from supplier')
         sup=cur.fetchall()
        
         if len(sup)>0:
             del self.sup_list[:]   
             self.sup_list.append("Select")
             for i in sup:
                 self.sup_list.append(i[0])  

     except Exception as ex:
        messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)
     
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror('Error','All fileds are required',parent=self.root)
            else:
                cur.execute('Select * from product where name=? ',(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','product already present , try diffrent ',parent=self.root)
                else:
                    cur.execute("""
                          INSERT INTO product
                          ('Category','Supplier','name','price','qty','status')
                           VALUES (?,?,?,?,?,?)
""",(
    self.var_cat.get(),
    self.var_sup.get(),
    self.var_name.get(),
    self.var_price.get(),
    self.var_qty.get(),
    self.var_status.get(),
    
))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Sucsses','product addes sucssesfully')
                    
                
                
                
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)
            
            
    def show(self):
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute('select * from product')
                rows=cur.fetchall()
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                 self.product_table.insert('',END,values=row)
                    
                    
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to :{str(ex)}',parent=self.root)
                
                
                  
    def get_data(self, ev):
      f = self.product_table.focus()   
      content = self.product_table.item(f)   
      row = content['values']

      if row:   
        print(row)

        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.cmb_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
        

        

        
            



    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.var_pid.get()=='':
                messagebox.showerror('Error','please select product from list',parent=self.root)
            else:
                cur.execute('select * from product where pid=?',(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Inviled product',parent=self.root)
                else:
                    cur.execute(' Update product  set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid =?',(
                        
    self.var_cat.get(),
    self.var_sup.get(),
    self.var_name.get(),
    self.var_price.get(),
    self.var_qty.get(),
    self.var_status.get(),
    self.var_pid.get()
                        
                        
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Product Updated Successfully',parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)




    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=='':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                cur.execute('Select * from Category where pid=?',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Error','Inviled pid',parent=self.root)
                else:
                    op=messagebox.askyesno('Confirm','Do you want really to delete?',parent=self.root)
                    if op ==True:
                       cur.execute('delete from EMPLOYEE where Emp_ID=?',(self.var_emp_id.get(),))
                       con.commit()
                       messagebox.showinfo('Success','Employee deleted Successfully',parent=self.root)
                       self.show()
            
            
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)


    def clear(self):
        self.var_sup.set("Select"),
        self.var_name.set("Select"),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set("")
        
        
        self.varSearchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error','Select search by option',parent=self.root)
            elif self.varSearchtxt.get()=="":
                messagebox.showerror('Error','Search input should be required',parent=self.root)
            
            else:
                query = f"SELECT * FROM category WHERE {self.var_searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.varSearchtxt.get() + '%',))
                rows=cur.fetchall()
                if len(rows)!=0:
                      self.product_table.delete(*self.product_table.get_children())
                      for row in rows:
                       self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror('Error','No record found!!',parent=self.root)
                 
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}',parent=self.root)   
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
        
        
if __name__ == '__main__':
    root = Tk()
    obj = productclass(root)
    root.mainloop()      
        
        