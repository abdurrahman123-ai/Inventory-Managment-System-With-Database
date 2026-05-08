from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
import os
from tkinter import messagebox

class salesclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x535+255+200')
        self.root.resizable(False,False)
        self.root.title('Inventory Management System | Developed by Abdurrahman Abdulcelil')
        self.root.config(bg='white')
        self.root.focus_force()
        
        
        
        
        
        
        
        
        self.bill_List=[]
        self.var_invoicer=StringVar()
        
        
        
        
        
        #_____________title________
        lbl_title=Label(self.root,text='View Customer Bill',justify='center',font=('time new roman',30), relief=RIDGE,bg='#184a45',fg='white')
        lbl_title.place(x=1,y=1,width=1273,height=40)
        
        lbl_invoice=Label(self.root,text='Invoice No:',font=('times new roman',15),bg='white')
        lbl_invoice.place(x=50,y=100)
        
        txt_invoice=Entry(self.root,textvariable=self.var_invoicer,font=('times new roman',15),bg='lightyellow')
        txt_invoice.place(x=160,y=100,width=180,height=28)
        
        btn_search=Button(self.root,text='Search',command=self.search,font=('times new roman',15,'bold'),cursor='hand2',fg='white',bg='#2196f3')
        btn_search.place(x=360,y=100,width=120,height=28)
        
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('times new roman',15,'bold'),cursor='hand2',fg='black',bg='lightgray')
        btn_clear.place(x=490,y=100,width=120,height=28)
        
        
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50, y=140,width=200,height=375)
       
       
       
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_frame,font=('goudy old style',15),bg='white',yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
        
        
        
        #Bill Area
        
        
        bill_frame=Frame(self.root,bd=3,relief=RIDGE,bg='lightyellow')
        bill_frame.place(x=280,y=140,width=410,height=375)
        
        bill_title=Label(bill_frame,text='Customer Bill Area',justify='center',font=('times new roman',15),bg='#F5BE27',fg='black')
        bill_title.pack(fill=X,side=TOP)
        
        
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=('gody old style',15),bg='lightyellow',yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        
        
        #===========Image=============
        
        self.bill_photo=Image.open('images/sales.png')
        self.bill_photo=self.bill_photo.resize((450,375))
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)


        lbl_image=Label(self.root,image=self.bill_photo)
        lbl_image.place(x=700,y=140)
        
        self.show()
#________________bill__________________

    def show(self):
        self.bill_List[:]
        self.Sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.bill_List.append(i.split('.')[1])
        
        
    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_[0])
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
            

        fp.close()
        
        
        
        
    def search(self):
        if self.var_invoicer.get()=="":
            messagebox.showinfo('Error','Invoicer no. should be required',parent=self.root)
        else:
            #print(self.bill_List,self.var_invoicer.get())
            if self.var_invoicer.get() in self.bill_List:
                print('yes find the invoicer')
                fp=open(f'bill/{self.var_invoicer.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror('Error',' Inviled Invoicer no.',parent=self.root )
                


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)












      
        
if __name__ == '__main__':
    root = Tk()
    obj = salesclass(root)
    root.mainloop()      
        
        
        
        
        