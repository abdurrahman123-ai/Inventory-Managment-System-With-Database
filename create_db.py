import sqlite3

def create_db():
    with sqlite3.connect('ims.db') as con:
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS EMPLOYEE (
            Emp_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            dob TEXT,
            doj TEXT,
            password TEXT,
            user_type TEXT,
            Adress TEXT,
            salary TEXT
        )
        """)
        con.commit()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS SUPPLIER (
            invoice INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            description TEXT
        )
        """)
        con.commit()
        
        cur.execute("""
        CREATE TABLE IF NOT EXISTS category (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            
        )
        """)
        con.commit()
        
        
        cur.execute("""
                    
                 CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text ,price text,qty text,status text)   
                                  
                    """)
        con.commit()
        
        
        
        
        
        
        
        
        
        
        

create_db()