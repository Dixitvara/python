import emp, pickle;

f = open("emp.dat",'wb')
n = int (input("enter emp count : "))

for i in range(n):
    id = int(input("id : "))
    name = input("name : ")
    salary = float(input("salary : "))

e = emp.emp(id, name, salary)
pickle.dump(e, f)
f.close()