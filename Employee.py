import mysql.connector as driver
def create_database():
    con=driver.connect(host='localhost',user='root', password='Aiswarya2006')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists employee')
    print()
    print("Database Created")
    con.close()


def show_databases():
    con=driver.connect(host='localhost',user='root',password='Aiswarya2006')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show databases')
    for i in cur:
        print(i)
    con.close()

def create_table():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute("create table if not exists emp(emp_id integer primary key, Name varchar(50),Phn_no int(10) UNSIGNED AUTO_INCREMENT, Designation varchar(50), Salary float)")
    print()
    print("Table Created -> EMP")
    cur.execute('DESC emp')
    for i in cur:
        print(i)
    con.close()
    
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()

def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        ID=int(input("ENTER EMPLOYEE ID : "))
        NAME=input("ENTER NAME OF EMPLOYEE : ")
        PHN_NO=int(input("ENTER PHONE NUMBER : "))
        DESIGNATION=input("ENTER THE DESIGNATION OF EMPLOYEE : ")
        SALARY=float(input("ENTER EMPLOYEE SALARY : "))
        query1="INSERT INTO emp VALUES({},'{}',{},'{}',{})".format(ID,NAME,PHN_NO,DESIGNATION,SALARY)
        cur.execute(query1)
        con.commit()
        print('Record Inserted')
        con.close()
    else:
        print("Error : Not Connected")

def update_record():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    cur=con.cursor()
    try:
        d=int(input("Enter Employee ID for update record : "))
        ID=int(input("ENTER NEW EMPLOYEE ID : "))
        NAME=input("ENTER NEW NAME OF EMPLOYEE : ")
        PHN_NO=int(input("ENTER PHONE NUMBER : "))
        DESIGNATION=input("ENTER THE DESIGNATION OF EMPLOYEE : ")
        SALARY=float(input("ENTER EMPLOYEE SALARY : "))
        query1="update emp set emp_id={}, Name={},Phn_no={}, Designation={}, Salary={} where emp_id= {}".format(ID,NAME,PHN_NO,DESIGNATION,SALARY,d)
        cur.execute(query1)
        con.commit()
        print("Record Updated")
    except:
        print("No such emp_id is there in the table")
    con.close()
    

def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID for deleting record : "))
    query1="delete from emp where emp_id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def search_record():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    cur=con.cursor()
    d=int(input("Enter Employee ID which you want to search : "))
    query1="select * from emp where emp_id={}".format(d,)
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    con.close()

def display_record():
    con=driver.connect(host='localhost',user='root',passwd='Aiswarya2006',database='employee')
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from emp')
        rec=cur.fetchall()
        for i in rec:
            print(i) 
        con.close()
    else:
        print("Error : Database Connection is not success" )
def menu():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print("1. CREATE DATABASE")
        print("2. SHOW DATABASES")
        print("3. CREATE TABLE")
        print("4. SHOW TABLES")
        print("5. INSERT RECORD")
        print("6. UPDATE RECORD")
        print("7. DELETE RECORD")
        print("8. SEARCH RECORD")
        print("9. DISPLAY RECORD")
        choice=int(input("Enter the choice (1-9) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databases()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_tables()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):
            display_record()
        else:
            print("Wrong Choice.")
        print ("==========================================================")
        print("THANK YOU, HAVE A NICE DAY")
        loop=input("Do you want more try? Press 'y' to continue...")
menu()


