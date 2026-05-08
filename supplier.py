from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class supplierclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x535+255+200')
        self.root.resizable(False,False)
        self.root.title('Inventory Management System | Developed by Abdurrahman Abdulcelil')
        self.root.config(bg='gray')
        self.root.focus_force()
        
        #All Variable
        self.var_searchby=StringVar()
        self.varSearchtxt=StringVar()
        self.var_sup_invoice=StringVar()


        self.var_contact=StringVar()
        self.var_name=StringVar()
       
        #_____________title________
        lbl_title=Label(self.root,text='Manage Supplier Details',justify='center',font=('time new roman',15),bg='#35F527')
        lbl_title.place(x=1,y=1,width=1273,height=40)
        
        #________search Frame_________
        
        
        
        lbl_search=Label(self.root,text='Invoicer No :',font=('time new roman',12),bg='white')
        lbl_search.place(x=800,y=130)
        
        
        txt_Search=Entry(self.root,textvariable=self.varSearchtxt,font=('goudy old style',15),bg='lightyellow',width=14)
        txt_Search.place(x=900,y=130)
        btn_search=Button(self.root,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',cursor='hand2')
        btn_search.place(x=1050,y=130,width=150,height=30)
        
        

        # ________________contenent_________________
        #row1
        lbl_supplier_invoice=Label(self.root,text='Invoicer No: :',font=('goudy old style',15),bg='white')
        lbl_supplier_invoice.place(x=10,y=50)
        txt_supplier=Entry(self.root,textvariable=self.var_sup_invoice,font=('goudy old style',15),bg='lightyellow')
        txt_supplier.place(x=150,y=50,width=180)
    
        
        #row2
        
        
        
        lbl_name=Label(self.root,text='Name :',font=('goudy old style',15),bg='white')
        lbl_name.place(x=10,y=100)
        
        
        
        txt_name = Entry(self.root, textvariable=self.var_name,
                 font=('goudy old style',15), bg='lightyellow')
        txt_name.place(x=150,y=100,width=180)
        
       #___ row 3 ___
       
       
       
       
       
        lbl_contact=Label(self.root,text='Contact :',font=('goudy old style',15),bg='white')
        lbl_contact.place(x=10,y=150) 
        txt_Contact = Entry(self.root, textvariable=self.var_contact,
                  font=('goudy old style',15), bg='lightyellow')
        txt_Contact.place(x=150,y=150,width=180)
        
        
        #row4
        
        lbl_desc=Label(self.root,text='Desecription :',font=('goudy old style',15),bg='white').place(x=10,y=200)
        
        self.txt_desc=Text(self.root,font=('goudy old style',15),bg='lightyellow')
        self.txt_desc.place(x=10,y=240,width=600,height=130)
        
        
        # ___________buttons_________
        
        btn_save=Button(self.root,text='Save',command=self.add,font=('goudy old style',15),bg='#1296f3',cursor='hand2')
        btn_save.place(x=100,y=400,width=110,height=40)
        btn_update=Button(self.root,text='Update',command=self.update,
                  font=('goudy old style',15),bg='#4caf50',cursor='hand2')
        btn_update.place(x=200,y=400,width=110,height=40)
        btn_delete=Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='#f44336',cursor='hand2')
        btn_delete.place(x=300,y=400,width=110,height=40)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#607d8b',cursor='hand2')
        btn_clear.place(x=410,y=400,width=110,height=40)

        
        #__________Employee_Details__________
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=165,width=550,height=300)
        
        scrrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        
        self.SupplierTabel = ttk.Treeview(emp_frame, columns=('invoice','Name','contact','desc'),show='headings')
        for col in ('invoice','Name','contact','desc'):
         self.SupplierTabel.column(col, width=135)
        
        scrrollx.pack(side=BOTTOM,fill=X)
        scrrolly.pack(side=RIGHT,fill=Y)
        scrrollx.config(command=self.SupplierTabel.xview)
        scrrolly.config(command=self.SupplierTabel.yview)
        
        
        self.SupplierTabel.configure(xscrollcommand=scrrollx.set,
                             yscrollcommand=scrrolly.set)
        
        
        self.SupplierTabel.heading("invoice", text="Invoice No")
        self.SupplierTabel.heading("Name", text="Name")
        self.SupplierTabel.heading("contact", text="Contact")
        self.SupplierTabel.heading("desc", text="description")
        
        self.SupplierTabel["show"] = "headings"      
        self.SupplierTabel.pack(fill=BOTH, expand=1)
        self.SupplierTabel.bind("<ButtonRelease-1>", self.get_data)
        #self.show()


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": 
                messagebox.showerror('Error','Invoicer must be required',parent=self.root)
            else:
                cur.execute('Select * from SUPPLIER where invoice=? ',(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','this invoicer no  is already assigned , try by difrent one',parent=self.root)
                else:
                 cur.execute("""
                            INSERT INTO SUPPLIER
                            (invoice, name, contact, description)
                              VALUES (?,?,?,?)
                             """, (
                              self.var_sup_invoice.get(),
                              self.var_name.get(),
                              self.var_contact.get(),
                              self.txt_desc.get("1.0","end-1c")
            ))
            con.commit()
            messagebox.showinfo('Sucsses','SUPPLIER addes sucssesfully')
            con.close()
            self.show()
                    
                
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)
            
            
    def show(self):
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute('select * from SUPPLIER')
                rows=cur.fetchall()
                self.SupplierTabel.delete(*self.SupplierTabel.get_children())
                for row in rows:
                 self.SupplierTabel.insert('',END,values=row)
                    
                    
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to :{str(ex)}',parent=self.root)
                
                
                       
    def get_data(self, ev):
      f = self.SupplierTabel.focus()   # الحصول على الصف المحدد
      content = self.SupplierTabel.item(f)   # الصحيح هنا
      row = content['values']

      if row:   # تأكد أن فيه بيانات
        print(row)

        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])

        self.txt_desc.delete("1.0", END)
        self.txt_desc.insert(END, row[3])
       

       
            



    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.var_sup_invoice.get()=='':
                messagebox.showerror('Error','Invoice No must required',parent=self.root)
            else:
                cur.execute('select * from SUPPLIER where invoice=?',(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Inviled invoice_id',parent=self.root)
                else:
                   cur.execute("""
                              UPDATE SUPPLIER SET
                            name=?,
                             contact=?,
                                description=?
                                   WHERE invoice=?
                                    """, (
                                       self.var_name.get(),
                                     self.var_contact.get(),
                                  self.txt_desc.get("1.0","end-1c"),
                           self.var_sup_invoice.get()
             ))
                con.commit()
                messagebox.showinfo('Success','SUPPLIER Updated Successfully',parent=self.root)
                self.show()
                    
        except Exception as ex:
         messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)




    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=='':
                messagebox.showerror('Error','invoice_id must be required',parent=self.root)
            else:
                cur.execute('Select * from SUPPLIER where invoice=?',(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Error','Inviled invoice_id',parent=self.root)
                else:
                    op=messagebox.askyesno('Confirm','Do you want really to delete?',parent=self.root)
                    if op ==True:
                       cur.execute('delete from SUPPLIER where invoice=?',(self.var_sup_invoice.get(),))
                       con.commit()
                       messagebox.showinfo('Success','SUPPLIER deleted Successfully',parent=self.root)
                       self.show()
            
            
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0','end-1c')
        self.varSearchtxt.set("")
        
        self.show()
        


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            
            if self.varSearchtxt.get()=="":
                messagebox.showerror('Error','Invoice No should be required',parent=self.root)
            
            else:
                
                cur.execute(
                "SELECT * FROM SUPPLIER WHERE invoice=?",
                (self.varSearchtxt.get(),)
            )
                row = cur.fetchone()

                self.SupplierTabel.delete(*self.SupplierTabel.get_children())
                if row:
                  self.SupplierTabel.insert('', END, values=row)
                else:
                    messagebox.showerror('Error','No record found!!',parent=self.root)
                 
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}',parent=self.root)   
        

























if __name__ == '__main__':
    root = Tk()
    obj = supplierclass(root)
    root.mainloop()



