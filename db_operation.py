#sql connection 
#installing sql module
#command : pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "demo"
)

def insert():
    
    #inserting data into database
    name = input("enter emp name : ")
    salary = input("enter emp salary : ")
    address = input("enter emp address : ")
    
    list = [name, salary, address]
    c = mydb.cursor()
    
    sql = "insert into myemp(ename,salary,address) values(%s, %s, %s)"
    c.execute(sql,list)
    mydb.commit()
    print(c.rowcount, "record inserted")

def update():
    oldname = input("enter old emp name : ")
    name = input("enter new emp name : ")
    salary = input("enter new emp salary : ")
    address = input("enter new emp address : ")

    newlist = [name, salary, address, oldname]
    c = mydb.cursor()

    sql = "UPDATE myemp SET ename=%s,salary=%s,address=%s WHERE ename=%s"
    c.execute(sql,newlist)
    mydb.commit()
    print(c.rowcount, "record updated")

def delete():
    delname = input("enter emp name : ")
    c = mydb.cursor()
    
    dellist = [delname]
    
    sql = "DELETE FROM myemp WHERE ename=%s"
    c.execute(sql,dellist)
    mydb.commit()
    print(c.rowcount, "record deleted")

def view():
    c = mydb.cursor()

    #Retrieving single row
    sql = "SELECT * from myemp"

    #Executing the query
    c.execute(sql)

    #Fetching 1st row from the table
    result = c.fetchall();
    print(result)

#main program
print("Operations : \n\t1)insert\n\t2)update\n\t3)delete\n\t4)view\n\t5)exit")
choice = None
while choice != '5':
    choice = input("Enter choice : ")
    match choice:
        case '1':
            insert()
        case '2':
            update()
        case '3':
            delete()
        case '4':
            view()