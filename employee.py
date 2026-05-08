from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x535+255+200')
        self.root.resizable(False,False)
        self.root.title('Inventory Management System | Developed by Abdurrahman Abdulcelil')
        self.root.config(bg='white')
        self.root.focus_force()
        
        #All Variable
        self.var_searchby=StringVar()
        self.varSearchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        self.var_adress=StringVar()


        
        #________search Frame_________
        
        SearchFrame=LabelFrame(self.root,text='Search Employee',bg='white')
        SearchFrame.place(x=320,y=20,width=600,height=70)
        
        comb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select",'Email','Name','Contact'),state='readonly',justify='center',font=('time new roman',12))
        comb_search.place(x=10,y=10,width=180)
        comb_search.current(0)
        
        txt_Search=Entry(SearchFrame,textvariable=self.varSearchtxt,font=('goudy old style',15),bg='lightyellow')
        txt_Search.place(x=200,y=10)
        btn_search=Button(SearchFrame,text='Search',command=self.search,font=('goudy old style',15),bg='#4caf50',cursor='hand2')
        btn_search.place(x=410,y=10,width=150,height=30)
        
        title_lab=Label(self.root,text='Employee Details',font=('goudy old style',12),bg="#0f4d7d",fg='white')
        title_lab.place(x=150,y=100,width=1000)

        # ________________contenent_________________
        #row1
        lbl_empid=Label(self.root,text='Emp ID :',font=('goudy old style',15),bg='white')
        lbl_empid.place(x=50,y=150)
        lbl_gender=Label(self.root,text='Gender :',font=('goudy old style',15),bg='white')
        lbl_gender.place(x=350,y=150)
        lbl_contact=Label(self.root,text='Contact :',font=('goudy old style',15),bg='white')
        lbl_contact.place(x=750,y=150)
        
        
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=('goudy old style',15),bg='lightyellow')
        txt_empid.place(x=150,y=150,width=180)
        comb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select",'Male','Female'),state='readonly',justify='center',font=('time new roman',12))
        comb_gender.place(x=450,y=150,width=180)
        comb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),bg='lightyellow')
        txt_contact.place(x=850,y=150,width=180)
        
        #row2
        
        lbl_name=Label(self.root,text='Name :',font=('goudy old style',15),bg='white')
        lbl_name.place(x=50,y=210)
        lbl_dob=Label(self.root,text='D.O.B :',font=('goudy old style',15),bg='white')
        lbl_dob.place(x=350,y=210)
        lbl_doj=Label(self.root,text='D.O.J :',font=('goudy old style',15),bg='white')
        lbl_doj.place(x=750,y=210)
        
        
        
        txt_name = Entry(self.root, textvariable=self.var_name,
                 font=('goudy old style',15), bg='lightyellow')
        txt_name.place(x=150,y=210,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=('goudy old style',15),bg='lightyellow')
        txt_dob.place(x=450,y=210,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=('goudy old style',15),bg='lightyellow')
        txt_doj.place(x=850,y=210,width=180)

       #___ row 3 ___
       
       
       
       
       
        lbl_email=Label(self.root,text='Email :',font=('goudy old style',15),bg='white')
        lbl_email.place(x=50,y=270)
        lbl_pass=Label(self.root,text='Passaword :',font=('goudy old style',15),bg='white')
        lbl_pass.place(x=350,y=270)
        lbl_utype=Label(self.root,text='User_Type :',font=('goudy old style',15),bg='white')
        lbl_utype.place(x=750,y=270)
        
        
        
        txt_email = Entry(self.root, textvariable=self.var_email,
                  font=('goudy old style',15), bg='lightyellow')
        txt_email.place(x=150,y=270,width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass,
                 font=('goudy old style',15),
                 bg='lightyellow', show='*')
        txt_pass.place(x=450,y=270,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=('Admin','Employee'),state='readonly',justify='center')
        cmb_utype.place(x=850,y=270,width=180,height=30)
        cmb_utype.current(0)
        
        
        #row4
        
        lbl_adress=Label(self.root,text='Adress :',font=('goudy old style',15),bg='white').place(x=50,y=330)
        lbl_salary=Label(self.root,text='Salary :',font=('goudy old style',15),bg='white').place(x=490,y=330)
        
        self.txtadress=Text(self.root,font=('goudy old style',15),bg='lightyellow')
        self.txtadress.place(x=150,y=310,width=280,height=60)
        
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=('goudy old style',15),bg='lightyellow').place(x=560,y=330)
        
        # ___________buttons_________
        
        btn_save=Button(self.root,text='Save',command=self.add,font=('goudy old style',15),bg='#1296f3',cursor='hand2')
        btn_save.place(x=800,y=330,width=110,height=30)
        btn_update=Button(self.root,text='Update',command=self.update,
                  font=('goudy old style',15),bg='#4caf50',cursor='hand2')
        btn_update.place(x=900,y=330,width=110,height=30)
        btn_delete=Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15),bg='#f44336',cursor='hand2')
        btn_delete.place(x=1000,y=330,width=110,height=30)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('goudy old style',15),bg='#607d8b',cursor='hand2')
        btn_clear.place(x=1100,y=330,width=110,height=30)

        
        #__________Employee_Details__________
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=385,relwidth=1,height=150)
        
        scrrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        
        self.EmployeeTable = ttk.Treeview(emp_frame, columns=('Emp_ID','Name','Email','Gender','Contact','DOB','DOJ','Password','User_Type','Adress','Salary'),show='headings')
        for col in ('Emp_ID','Name','Email','Gender','Contact','DOB','DOJ','Password','User_Type','Adress','Salary'):
         self.EmployeeTable.column(col, width=135)
        
        scrrollx.pack(side=BOTTOM,fill=X)
        scrrolly.pack(side=RIGHT,fill=Y)
        scrrollx.config(command=self.EmployeeTable.xview)
        scrrolly.config(command=self.EmployeeTable.yview)
        
        
        self.EmployeeTable.configure(xscrollcommand=scrrollx.set,
                             yscrollcommand=scrrolly.set)
        
        
        self.EmployeeTable.heading("Emp_ID", text="Emp_ID")
        self.EmployeeTable.heading("Name", text="Name")
        self.EmployeeTable.heading("Email", text="Email")
        self.EmployeeTable.heading("Gender", text="Gender")
        self.EmployeeTable.heading("Contact", text="Contact")
        self.EmployeeTable.heading("DOB", text="DOB")
        self.EmployeeTable.heading("DOJ", text="DOJ")
        self.EmployeeTable.heading("Password", text="Password")
        self.EmployeeTable.heading("User_Type", text="User_Type")
        self.EmployeeTable.heading("Adress", text="Adress")
        self.EmployeeTable.heading("Salary", text="Salary")
        self.EmployeeTable.bind('<ButtonRelease>',self.get_data)
        self.EmployeeTable["show"] = "headings"
        


 
 
        
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.show()


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror('Error','employee id must be required',parent=self.root)
            else:
                cur.execute('Select * from EMPLOYEE where Emp_ID=? ',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','this EMPLOYEE is already assigned , try by difrent one',parent=self.root)
                else:
                    cur.execute("""
                          INSERT INTO EMPLOYEE
                          (Emp_ID,Name,Email,Gender,Contact,DOB,DOJ,Password,User_Type,Adress,Salary)
                           VALUES (?,?,?,?,?,?,?,?,?,?,?)
""",(
    self.var_emp_id.get(),
    self.var_name.get(),
    self.var_email.get(),
    self.var_gender.get(),
    self.var_contact.get(),
    self.var_dob.get(),
    self.var_doj.get(),
    self.var_pass.get(),
    self.var_utype.get(),
    self.txtadress.get('1.0','end-1c'),
    self.var_salary.get()
))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Sucsses','employee addes sucssesfully')
                    
                
                
                
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)
            
            
    def show(self):
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                cur.execute('select * from EMPLOYEE')
                rows=cur.fetchall()
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                 self.EmployeeTable.insert('',END,values=row)
                    
                    
            except Exception as ex:
                messagebox.showerror('Error',f'Error due to :{str(ex)}',parent=self.root)
                
                
                       
    def get_data(self, ev):
      f = self.EmployeeTable.focus()   # الحصول على الصف المحدد
      content = self.EmployeeTable.item(f)   # الصحيح هنا
      row = content['values']

      if row:   # تأكد أن فيه بيانات
        print(row)

        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])

        self.txtadress.delete('1.0', END)
        self.txtadress.insert(END, row[9])

        self.var_salary.set(row[10])
            



    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        
        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error','Employee id must required',parent=self.root)
            else:
                cur.execute('select * from EMPLOYEE where Emp_ID=?',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Inviled Employee Id',parent=self.root)
                else:
                    cur.execute(' Update EMPLOYEE  set Name=?,Email=?,Gender=?,Contact=?,DOB=?,DOJ=?,Password=?,User_Type=?,Adress=?,Salary=? where Emp_ID =?',(
                        
    self.var_name.get(),
    self.var_email.get(),
    self.var_gender.get(),
    self.var_contact.get(),
    self.var_dob.get(),
    self.var_doj.get(),
    self.var_pass.get(),
    self.var_utype.get(),
    self.txtadress.get('1.0','end-1c'),
    self.var_salary.get(),
    self.var_emp_id.get()
                        
                        
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Employee Updated Successfully',parent=self.root)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)




    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                cur.execute('Select * from EMPLOYEE where Emp_ID=?',(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror('Error','Inviled Employee ID',parent=self.root)
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
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        
        self.var_dob.set("")
        self.var_doj.set("")
        
        
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txtadress.delete('1.0','end-1c')
        self.var_salary.set("")
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
                query = f"SELECT * FROM EMPLOYEE WHERE {self.var_searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.varSearchtxt.get() + '%',))
                rows=cur.fetchall()
                if len(rows)!=0:
                      self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                      for row in rows:
                       self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror('Error','No record found!!',parent=self.root)
                 
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}',parent=self.root)   
        

























if __name__ == '__main__':
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()



