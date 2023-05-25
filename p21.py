#sql connection 
#installing sql module
#command : pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "addressBook"
)

def insert():
    
    #inserting data into database
    name = input("enter name : ")
    address = input("enter address : ")
    mobile = input("enter mobile : ")
    
    list = [name, address, mobile]
    c = mydb.cursor()
    
    sql = "insert into address(name,address,mobile) values(%s, %s, %s)"
    c.execute(sql,list)
    mydb.commit()
    print(c.rowcount, "record inserted")

def update():
    oldname = input("enter old name : ")
    name = input("enter new name : ")
    address = input("enter new address : ")
    mobile = input("enter new mobile : ")

    newlist = [name, address, mobile, oldname]
    c = mydb.cursor()

    sql = "UPDATE address SET name=%s,address=%s,mobile=%s WHERE name=%s"
    c.execute(sql,newlist)
    mydb.commit()
    print(c.rowcount, "record updated")

def delete():
    delname = input("enter name to delete : ")
    c = mydb.cursor()
    
    dellist = [delname]
    
    sql = "DELETE FROM address WHERE name=%s"
    c.execute(sql,dellist)
    mydb.commit()
    print(c.rowcount, "record deleted")

def view():
    print("Address Books : ")
    c = mydb.cursor()

    #Retrieving single row
    sql = "SELECT * from address"

    #Executing the query
    c.execute(sql)

    #Fetching 1st row from the table
    result = c.fetchall()
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
        case '5':
            break
        case _:
            print("enter valid choice")
            break