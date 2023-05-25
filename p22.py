#sql connection 
#installing sql module
#command : pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "eventRegistration"
)

def register():
    print("please fill this details to Registration :\n")
    #inserting data into database
    name = input("enter name : ")
    address = input("enter address : ")
    mobile = input("enter mobile : ")
    email = input("enter emailId : ")
    
    list = [name, address, mobile, email]
    c = mydb.cursor()
    
    sql = "insert into evenreg(name,address,mobile,email) values(%s, %s, %s, %s)"
    c.execute(sql,list)
    mydb.commit()
    print(c.rowcount, " student registred successfully")

def cancelRegister():
    delemail = input("enter email id to cancel registration : ")
    c = mydb.cursor()
    
    dellist = [delemail]
    
    sql = "DELETE FROM evenreg WHERE email=%s"
    c.execute(sql,dellist)
    mydb.commit()
    print(c.rowcount, "registration cancelled")

def viewRegistration():
    print("Registration details : ")
    c = mydb.cursor()

    #Retrieving single row
    sql = "SELECT * from evenreg"

    #Executing the query
    c.execute(sql)

    #Fetching 1st row from the table
    result = c.fetchall()
    print(result)

#main program
print("Operations : \n\t1)Registration\n\t2)Cancel registration\n\t3)view\n\t4)exit")
choice = None
while choice != '5':
    choice = input("Enter choice : ")
    match choice:
        case '1':
            register()
        case '2':
            cancelRegister()
        case '3':
            viewRegistration()
        case '4':
            break
        case _:
            print("enter valid choice")
            break