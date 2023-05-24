empNo = int(input("Enter empID : "))
name = input("Enter empName : ")
deptNo = int(input("Enter departmentNO : "))
basic = float(input("Enter basic salary : "))
da = float(input("Enter DA(in percentage) : "))
hra = float(input("Enter HRA(in percentage) : "))
con = float(input("Enter Conveyance : "))

#file = open('salary.txt','w')

salary = basic + basic * (da / 100)
salary = salary + salary * (hra / 100)

print(name, "your net salary is :", salary)