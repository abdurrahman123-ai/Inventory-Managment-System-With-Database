from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class categoryclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x535+255+200')
        self.root.resizable(False,False)
        self.root.title('Category Management System | Developed by Abdurrahman Abdulcelil')
        self.root.config(bg='white')
        self.root.focus_force()
        #_______ Variables ___________
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
        #_________title__________
        
        lbl_title=Label(self.root,text='Manage Product Category',font=('goudy old style',30),bd=3,fg='white',bg='#184a45',relief=RIDGE)
        lbl_title.pack(fill=X,side='top')
        
        lbl_name=Label(self.root,text='Enter Category Name :',font=('goudy old style',30),bg='white')
        lbl_name.place(x=50,y=100)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',18),justify='center',bg='lightyellow')
        txt_name.place(x=50,y=170,width=300)
        
        
        btn_add=Button(self.root,text='ADD',command=self.add,font=('goudy old style',12),bd=2,bg='green',fg='white',justify='center')
        btn_add.place(x=370,y=170,width=150)
        
        btn_del=Button(self.root,text='Delete',command=self.delete,font=('goudy old style',12),bd=2,bg='red',fg='white',justify='center')
        btn_del.place(x=530,y=170,width=150)
        
        
        # Category Details
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=750,y=80,width=520,height=250)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollX=Scrollbar(cat_frame,orient=HORIZONTAL)
               
        self.category_Table=ttk.Treeview(cat_frame,columns=('cid','name'),yscrollcommand=scrolly.set)
        scrollX.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollX.config(command=self.category_Table.xview)
        scrolly.config(command=self.category_Table.yview)
        
        self.category_Table.heading('cid',text='C ID')
        self.category_Table.heading('name',text='Name')
        self.category_Table['show']='headings'
        self.category_Table.column('cid',width=90)
        self.category_Table.column('name',width=100)
        self.category_Table.pack(fill=BOTH,expand=1)
        self.category_Table.bind('<ButtonRelease-1>',self.get_data)
        
        #___________images_________
        self.im1=Image.open('images/cat1.png')
        self.im1=self.im1.resize((500,250))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,bd=2,image=self.im1,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        
        
        self.show()
        
        
        
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="": 
                messagebox.showerror('Error','category name should be required',parent=self.root)
            else:
                cur.execute('Select * from category where name=? ',(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','this name no  is already assigned , try by difrent one',parent=self.root)
                else:
                 cur.execute("""
                            INSERT INTO category (name)
                VALUES (?)
                             """, (
                              
                              self.var_name.get(),
                              
                              
            ))
            con.commit()
            messagebox.showinfo('Sucsses','category addes sucssesfully')
            con.close()        
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)
        
        
    def show(self):
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute('select * from category')
                rows=cur.fetchall()
                self.category_Table.delete(*self.category_Table.get_children())
                for row in rows:
                 self.category_Table.insert('',END,values=row)
                    
                    
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to :{str(ex)}',parent=self.root)
                
    def get_data(self, ev):
      f = self.category_Table.focus()   # الحصول على الصف المحدد
      content = self.category_Table.item(f)   # الصحيح هنا
      row = content['values']

      if row:   # تأكد أن فيه بيانات
        print(row)

       
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

              
    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=='':
                messagebox.showerror('Error','please select category from list',parent=self.root)
            else:
                cur.execute('Select * from category where cid=?',(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Error','please try again ',parent=self.root)
                    
                else:
                    op=messagebox.askyesno('Confirm','Do you want really to delete?',parent=self.root)
                    if op ==True:
                       cur.execute('delete from category where cid=?',(self.var_cat_id.get(),))
                       con.commit()
                       messagebox.showinfo('Success','category deleted Successfully',parent=self.root)
                       self.show()
            
            
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        
        
if __name__ == '__main__':
    root = Tk()
    obj = categoryclass(root)
    root.mainloop()       
        
        
        