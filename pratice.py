# elements = [13, 21, 37, 40, 95];
# a = bytes(elements);
# print(a[0]);
# a[0] = 60;
# print(a[0]);
# for i in range(5):
#     print("Hello")
# for i in range(10):
#    print(i);

# mydict = {'ten':10,'twenty':20,'therty':30,'forty':40,};
# print(mydict);
# print(list(mydict.keys()))
# print(list(mydict.values()))

# pi = 3.14;
# radius = 4;
# area = pi *(radius * radius);
# print(area);

# x = 15;
# if x % 2 == 0:
#     print(x ," is even");
# else:
#     print(x ," is odd");

# n = input("Enter your name : ");
# print("Your name is ", n);

# Bytearray
# element = [10, 20, 30, 40, 50];
# a = bytearray(element);
# print(a[0]);
# print(a[-2]);

# list
# list = [10, 20, "Dixit", 'Shivkaran'];
# print(list[3]);
# print(list[-3]);

# map example
"""def addition(n):
    return n + n;
def multiplication(m):
    return m * m;
numbers = (1,2,3,4,5);
sumofnum = map(addition,numbers);
print("Sum of num : ",list(sumofnum));

multiofnum = map(multiplication,numbers);
print("Multi of num : ",list(multiofnum));"""

# list example
"""array = ["sun","mon","tus"];
test = list(map(list,array));
print(test);"""

# dictionarie example

"""import os
demodict = dict(apple="red", banana="yellow", grapes="green")
"""  # print(demodict);

# add element in dictionarie
"""demodict["chikoo"] = "brown";
print(demodict);

#update in dictionarie
demodict["orange"] = "red";
print(demodict);

#removing element in dictionarie
del(demodict["banana"]);
print(demodict);

#length of dictionary
print("Total of dictionary element : ",len(demodict));

#loop through a dictionary
for i in demodict:
    print(i,":",demodict[i]);"""

# clear() function
"""demodict.clear();
print(demodict);"""

# copy() function
"""copydict = demodict.copy();
print(copydict);

#fromkeys() function
printdict = dict.fromkeys(demodict);
print(printdict);"""

# get()
"""person = {"name":"Dixit","age":"21"};
print("Name: ",person.get("name"));
print("Age: ",person.get("age"));

print("Salary: ",person.get("salary"));
print("Salary: ",person.get("salary",0.0));
"""

# printing memory address in python
"""x=10;
print(id(x));"""

# program to pass an integer to function and modify variable.
"""def modify(x):
    x=15;
    print(x,id(x));

x = 10;
modify(x);
print(x,id(x));"""

# program to modify list
"""def modify(val):
    val.append(10);
    val.append(12);
    val.append(14);
    print(val,id(val));
val = [1,2,3,4];
modify(val);"""

"""def modify(val):
    val.append(100);
    print(val,id(val));
val = [1,2,3,4];
modify(val);"""

# formal and actual arguments
# keyword argument
"""
print("Keyword argument: ");
def fun(a,b,c):
    print(a,b,c);
fun(a=1,c=3,b=2);

#positional argument
print("positional argument: ");
fun(10,20,5);

#default argument
print("default argument: ");
def fun(a,b=20,c=50):
    print(a,b,c);
fun(30);

#variable length argument
#  *args
def fun(*a):
    print(type(a),a);
fun(11,22,33);

# **kwargs
def fun(**kwarg):
    print(type(kwarg),kwarg);
fun(a=11,c=22,b=33);"""

# local and global variable
# local variable
"""
def myfun():
    a=1;
    a+=1;
    print("a =",a);
myfun();
print(a);"""

# global variable
"""
a = 1;
def myfun():
    a = 3;
    print("in function a =",a);
myfun();
print("out of function a =",a);"""

# using global variable in function
"""
a = 10;
def myfun():
    global a;
    print("inside function global a =",a);
    a = 20;
    print("inside function local modify =",a);
myfun();
print("out side function a =",a);
"""

"""
a = 10;
def myfun():
    a = 20;
    x = globals()["a"];
    print("x =",x);
    print("a =",a);
myfun();
"""

"""for i in str(12345):
    print(i);"""

# passing a group of element to a function
"""def display(demo):
    for i in demo:
        print(i);
display("Dixit");
"""
# take a group of string from keyboard
# print("Enter string separated by comma:");

# recursive function
# factorial program

"""
def fact(n):
    if n == 0:
        result = 1;
    else:
        result = n * fact(n-1);
    return result;
for i in range(1,6):
    print("factorial of {}` is {}".format(i,fact(i)));
"""

# anonymous/ lambda functions which have no function name
"""
ans = lambda x: x + x;
print(ans(20));
"""

# lambda with using map()
"""
lst = [int (x) for x in range(5,10)];
print("list: ",lst);
lst1 = list(map(lambda a:(a**2),lst));
print("list: ",lst1);
"""

# lambda with using reduce()
"""
import functools;
lst = [int(x) for x in range(1,5)];
print("sum : ", functools.reduce(lambda a,b : a + b,lst));
"""

# function decorators
# normal program

"""def fun(str):
    def wel():
        return "hello "
    return wel() + str
def demo(demo):
    return demo
print(fun(demo("dixit")))
"""
# using function decorators
"""
def fun(str):
    def demo(demo):
        return "hello " + str(demo);
    return demo;

@fun
def wel(demo):
    return demo;
print wel("dixit");
"""

# generate random number usign yield
"""
import random;
def num():
    for i in range(1):
        yield random.randint(1,6);
for i in num():
    print(i);
"""

# salary program
"""
salary = int(input("Enter salary : "));

# hra
salary = salary + 7/100;

# all basic allownce
salary = salary + 2 / 100;

# PF
salary = salary - 15 / 100;

print("Your salary : ", salary)
"""

# exception
"""
try:
    i = eval(input("enter data: "));
except SyntaxError:
    print("invalid data");
else:
    print(i);
"""

# handle IOError
"""
try:
    name = input("enter file name : ");
    f = open(name,"r");
except IOError:
    print("file not found", name);
else:
    print("file found", name);
    f.close();
"""

# handle multiple exception
"""
def avg(list):
    tot = 0;
    for x in list:
        tot += x;
    avg = tot / len(list);
    return tot, avg;
try:
    t,a = avg([1,2,3,4,5,6]);
    print("total = {},average = {}" .format(t,a));
except TypeError:
    print("typeError .. please provide numbers");
except ZeroDivisionError:
    print("zeroDivisionError");
"""

# finlly and try block
"""
try:
    x = int(input("input de : "));
    y = 1 / x;
finally:
    print("not catching exception");
print("division is :", y);
"""

# assert statement
"""
try:
    x = int(input("enter number between 1 to 100 : "));
    assert x >= 1 and x <= 100;
    print("Entered number is ",x);
except AssertionError:
    print("Condition is not fullfiled");
"""

# logging and exceptions
"""
import logging;
logging.basicConfig(filename = 'hello.txt', level = logging.ERROR);
logging.error("There is an error in program");
logging.critical("there is a problem in the design");
logging.warning("warning");
logging.info("info");
logging.debug("error in line 10");
"""

# write in file
"""
file = open("demo2.txt","w");
s = input("Enter string : ");
file.write(s);
file.close();
"""

# reading a file
"""
file = open("hello.txt","r");
print(file.read());
file.close();
"""

# writing in file
"""
file = open("demo2.txt", "w");
s = input("Enter String (@ to end): ");
while s != '@':
    s = input();
    if(s != '@'):
        file.write(s + "\n");
"""

# append a text
"""
file = open("demo2.txt", "a+");
s = input("Enter String (@ to end): ");
while s != '@':
    s = input();
    if(s != '@'):
        file.write(s + "\n");
file.seek(0,0);

print("file content : ");
s = file.read();
print(s);
"""

# file program
"""
import os, sys;
file = input("Enter file name to find : ");
if os.path.isfile(file):
    f = open(file,'r');
else:
    print(file + " does not exist");
    sys.exit();

print("the file content are : ");
s = file.read();
print(s);
file.close();
"""

# write image in another file
"""
f1 = open("image.jpg","rb");
f2 = open("image1.jpg","wb");

display = f1.read();
f2.write(display);

f1.close();
f2.close();
"""

# with statement write in file
"""
with open("hello.txt","w") as file:
    file.write("I am learning python\n");
    file.write("python is bad");
"""

# with statement read from file
"""
with open("hello.txt","r") as file:
    for line in file:
        print(line);
"""

# pickle in python
"""
import emp, pickle

f = open("emp.dat","rb")

print("employee details: ")
while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print("end of file reached")
        break
f.close()
"""

# seek in python
"""
s = "amazing python"
with open("demo.txt","wb") as f:
    f.write(s.encode())

with open("demo.txt",'rb') as f:
    print(f.seek(3))
    print(f.read(2))
    print(f.tell())
    print(f.seek(4,1))
    print(f.read(1))
    print(f.tell())
"""

# create zipfile in python
"""
from zipfile import *

with ZipFile("test.zip", "w") as f:
    f.write('demo.txt')
    f.write('demo2.txt')
    f.write('emp.dat')
print("test.zip file created")
f.close()
"""

# unzip file
"""
from zipfile import *
with ZipFile("test.zip", "r") as f:
    f.extractall()
f.close()"""

# create directory in python
"""
import os
print(os.getcwd())
os.mkdir("shiv/karan")
"""

# user defined exceptions
"""class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

try:
    raise (MyError(3*2))
except MyError as error:
    print("A new exception occured : ", error.value)
"""

# matplotlib example
"""
import pandas as p
import matplotlib.pyplot as mp

mp.figure(1)
mp.title("example-1")
mp.xlabel("x variable")
mp.ylabel("y variable")
mp.plot([1, 2, 3, 4], [1, 7, 3, 5])
mp.show()
mp.savefig("figure")
"""

# reading data from excel file
"""
import pandas as p
import xlrd

filepath = "excel.xlsx"
df = p.read_excel(filepath)
print(df)"""

# reading data from csv file
"""
import pandas as p
import xlrd

filepath = "excel.csv"
df = p.read_csv(filepath)
print(df)"""

# reading data from python dictionary
"""
import pandas as p
empdate = {
    "empid" : [101,102,103],
    "ename" : ["bipin","hitesh","jitesh"],
    "salary" : [10000,20000,30000],
    "doj" : ['01-01-2020','02-12-2023','01-02-2022']
}
df = p.DataFrame(empdate)
print(df)"""

# reading data from list of tuples
"""import pandas as p
empdata = [
    (100,'bipin',10000,'01-01-2002'),
    (101,'mohit',20000,'01-01-2002'),
    (102,'rajesh',30000,'01-01-2002'),
    (103,'mitesh',14000,'01-01-2002'),
    (104,'minu',41000,'01-01-2002'),
]

df = p.DataFrame(empdata,columns = ["empId","empname","salary","doj"])
print(df)"""

# data frame operation shape - gives shape of data
"""import pandas as p
df = p.read_csv("excel.csv")
print(df)
print(df.shape)"""

# data frame operation head - gives first (default 5) records
"""import pandas as a
df = a.read_csv('excel.csv')
print(df.head(2))
"""
# data frame operation tail - gives last (default 5) records
"""import pandas as a
df = a.read_csv('excel.csv')
print(df.tail(2))"""

# data frame operation range
"""import pandas as a
df = a.read_csv("excel.csv")
print(df[1:4])"""

# find min and max value of column
"""import pandas as a
df = a.read_csv("excel.csv")
print("min : ",df['salary'].min())
print("max : ",df['salary'].max())
"""

# display statistical info of data frame
"""import pandas as p
df = p.read_csv("excel.csv")
print(df.index)
"""

# set column as index
"""import pandas as p
df = p.read_csv("excel.csv")
df1 = df.set_index("empid")
print(df1)
"""

# data frame .loc[] attribute
"""import pandas as p
df = p.read_csv('excel.csv')
df.set_index('empid',inplace=True)
print(df.loc[1004])
"""

# bar chart using matplotlib.pyplot
"""
import pandas as p
import matplotlib.pyplot as mat

df = p.read_csv('python/excel.csv')
x = df["empid"]
y = df["salary"]
mat.bar(x, y, label = 'employee data', color = 'blue')
mat.xlabel('employee id')
mat.ylabel('employee salary')
mat.title('www.skyadav.com')
mat.legend()
mat.show()"""

# horizontal bar chart using matplotlib.pyplot

"""import pandas as p
import matplotlib.pyplot as mat

df = p.read_csv('python/excel.csv')
x = df["empid"]
y = df["salary"]
mat.barh(x, y, label = 'employee data', color = 'blue')
mat.xlabel('employee id')
mat.ylabel('employee salary')
mat.title('www.skyadav.com')
mat.legend()
mat.show()
"""

# bar graph from multiple data frames

"""import pandas as p
import matplotlib.pyplot as mat

x = [101,102,103,104,105]
y = [1000,2000,3000,4000,5000]

x1 = [111,112,113,114,115]
y1 = [1000,2000,3000,4000,5000]
mat.bar(x, y, label = 'sales data', color = 'orange')
mat.bar(x1, y1, label = 'production data', color = 'green')
mat.xlabel('employee id')
mat.ylabel('employee salary')
mat.title('www.skyadav.com')
mat.legend()
mat.show()"""

# Pie chart
"""
import pandas as p
import matplotlib.pyplot as mat

x = [10, 20, 30, 40, 50]
dept = ["sales", "production", "hr", "finance", "majur"]
color = ["red", "green", "blue", "yellow","pink"]
mat.pie(x, labels = dept, colors = color, startangle = 90, explode = (0, 0.2, 0.4, 0, 0), shadow = True, autopct = "%.2f%%")
mat.title("www.skyadav.com")
mat.legend()
mat.show()
"""

# line graph
"""import pandas as p
import matplotlib.pyplot as mat

y = [1450,2000,6430,2500,3400]
x = [9,10,11,14,20]

mat.plot(x, y, label = 'sales data')
mat.xlabel('employee id')
mat.ylabel('employee salary')
mat.title('www.skyadav.com')
mat.legend()
mat.show()
"""

# constructor in python
"""
class Student:
    def __init__(self):
        self.name = 'shiv'
        self.age = 30
        self.marks = 100
    def talk(self):
        print("name is", self.name)
        print("age is", self.age)
        print("marks is", self.marks)
obj = Student()
obj.talk()"""

# example of constructor
"""class Student:
    def __init__(self,name = "",mark = 0):
        self.name = name
        self.mark = mark
    def printData(self):
        print("name : ", self.name)
        print("mark : ",self.mark)
obj = Student("dixit",70)
obj.printData()
"""

# decorators example
"""
class Student:
    rno = 0
    def __init__(self,name = "",mark = 0):
        self.name = name
        self.mark = mark
    @classmethod
    def setRoll(cls):
        cls.rno = cls.rno + 1
    def printData(self):
        self.setRoll()
        print("roll no : ", self.rno)
        print("name : ", self.name)
        print("mark : ",self.mark)
obj = Student("dixit",70)
obj.printData()

obj2 = Student("shivkaran",66)
obj2.printData()
"""

# getter setter functions
"""
class Student:
    rno = 0
    def __init__(self,name = "",mark = 0):
        self.name = name
        self.mark = mark
    @classmethod
    def getRoll(cls):
        cls.rno = cls.rno + 1
    def printData(self):
        self.getRoll()
        print("roll no : ", self.rno)
        print("name : ", self.name)
        print("mark : ",self.mark)
    def setData(self,name,mark):
        self.name = name
        self.mark = mark
obj = Student()
obj.setData("dixit",70)
obj.printData()

obj2 = Student()
obj2.setData("shivkaran",66)
obj2.printData()

class Result:
    @staticmethod
    def isPass(s):
        if(s.mark >= 40):
            print(s.name, "is pass")
        else:
            print(s.name,"is fail")
obj = Student()
obj.setData("dixit",70)
obj.printData()

obj2 = Student()
obj2.setData("shivkaran",66)
obj2.printData()
Result.isPass(obj)
"""

# inner class
"""
class Person:
    def __init__(self):
        self.name = "Mr.Shivkiran"
        self.db = self.DOB()
    def display(self):
        print("name : ", self.name)

    class DOB:
        def __init__(self):
            self.dd = 20
            self.mm = 1
            self.yy = 2002
        def display(self):
            print("DOB : {}/{}/{}".format(self.dd,self.mm,self.yy))
p = Person()
p.display()
x = p.db
x.display()
"""

# sql connection
# installing sql module
# command : pip install mysql-connector-python


# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="demo"
# )


# def insert():

#     # inserting data into database
#     name = input("enter emp name : ")
#     salary = input("enter emp salary : ")
#     address = input("enter emp address : ")

#     list = [name, salary, address]
#     c = mydb.cursor()

#     sql = "insert into myemp(ename,salary,address) values(%s, %s, %s)"
#     c.execute(sql, list)
#     mydb.commit()
#     print(c.rowcount, "record inserted")


# def delete():
#     oldname = input("enter old emp name : ")
#     name = input("enter new emp name : ")
#     salary = input("enter new emp salary : ")
#     address = input("enter new emp address : ")

#     newlist = [name, salary, address, oldname]

#     c = mydb.cursor()

#     sql = "UPDATE myemp SET ename=%s,salary=%s,address=%s WHERE ename=%s"

#     c.execute(sql, newlist)
#     mydb.commit()
#     print(c.rowcount, "record inserted")

# constructor in inheritance
# class baap:
#     def __init__(self):
#         self.shoes = 80000
#     def shoeStyle(self):
#         print("baap ke pass se shoe : ", self.shoes,"ke")
# class beta(baap):
#     pass
# beta = beta()
# beta.shoeStyle()

# # something
# class Square:
#     def __init__(self,x):
#         self.x = x
#     def area(self):
#         print("area of square ==> ", self.x * self.x)
# class Rectangle(Square):
#     def __init__(self, x, y):
#         self.y = y
#         super().__init__(x)
#     def area(self):
#         super().area()
#         print("area of rectangle ==> ",self.x * self.y)
# a, b = [float(x) for x in input("enter two measurements : ").split()]
# r = Rectangle(a, b)
# r.area()

# #multiple inheritance
# class A():
#     def __init__(self):
#         self.a = 10
#         print("a : ", self.a)
#         super().__init__()
# class B():
#     def __init__(self):
#         self.b = 20
#         print("b : ", self.b)
#         super().__init__()
# class C(A,B):
#     def __init__(self):
#         self.c = 30
#         print("c : ", self.c)
#         super().__init__()
# obj = C()

# #Hybrid inheritance

# class A():
#     def __init__(self):
#         self.a = 10
#         print("a : ", self.a)
#         super().__init__()
# class B(A):
#     def __init__(self):
#         self.b = 20
#         print("b : ", self.b)
#         super().__init__()
# class C(A):
#     def __init__(self):
#         self.c = 30
#         print("c : ", self.c)
#         super().__init__()
# class D(B,C):
#     def __init__(self):
#         self.d = 40
#         print("d : ", self.d)
#         super().__init__()
# obj = D()


# operator overloading
"""class book1:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


class book2:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
b1 = book1(100)
b2 = book2(200)
bx = b1 + b2
print(bx)
"""

# __gt__
"""class book1:
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages

class book2:
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages
b1 = book1(300)
b2 = book2(200)

if b1 > b2:
    print("B1 have more pages")
else:
    print("B2 have more pages")
"""

# method overloading in python example
# it is not possible in python
"""
def product(a, b):
    p = a * b
    print(p)
def product(a, b, c):
    p = a * b * c
    print(p)

product(2, 10, 3)
"""

# method overloading example
"""
class overloading:
    def sum (self, a = None, b = None, c = None):
        if a!= None and b!= None and c!= None:
            print("sub : ", a + b + c)
        elif a!= None and b!= None:
            print("sum : ", a + b)
        else:
            print("enter 2 or 3 args")
obj = overloading()
obj.sum(5,1,4)
obj.sum(5,1)
obj.sum(1)
"""

# abstraction in python
"""
import math
from abc import ABC, abstractmethod
class myclass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass

class sub1(myclass):
    def calculate(self, x):
        print("square : ", x * x)

class sub2(myclass):
    def calculate(self, x):
        print("squaroot : ", math.sqrt(x))

class sub3(myclass):
    def calculate(self, x):
        print("cube : ", x * x * x)

obj = sub1()
obj.calculate(4)
obj = sub2()
obj.calculate(16)
obj = sub3()
obj.calculate(3)
"""

# abstract method example
"""
from abc import *
class car(ABC):
    def __init__(self, regno):
        self.regno = regno
    def openTank(self):
        print("fill the tank")
        print("car regno : ", self.regno)
    @abstractmethod
    def steering(self):
        pass
    def breaks(self):
        pass

class maruti(car):
    def steering(self):
        print("Maruti : manual steering")
    def breaks(self):
        print("Maruti : gas breaks")

class tesla(car):
    def steering(self):
        print("Tesla : auto pilot steering")
    def breaks(self):
        print("Tesla : automatic breaks")

obj = maruti(4204)
obj.openTank()
obj.steering()
obj.breaks()

obj = tesla(1230)
obj.openTank()
obj.steering()
obj.breaks()
"""

#example
from abc import *
class myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        pass

class oracle(myclass):
    def connect(self):
        print("Connecting to oracle")
    def disconnect(self):
        print("disconnecting to oracle")

class sql(myclass):
    def connect(self):
        print("Connecting to sql")
    def disconnect(self):
        print("disconnecting to sql")

dataBase = input("enter database name : ")
className = globals() [dataBase]
obj = className()
obj.connect()
obj.disconnect()

#example
from abc import *
class myclass(ABC):
    @abstractmethod
    def connect(self):
        print("connecting")
    @abstractmethod
    def disconnect(self):
        print("disconnecting")

class oracle(myclass):
    def connect(self):
        print("Connecting to oracle")
    def disconnect(self):
        print("disconnecting to oracle")

class sql(myclass):
    def connect(self):
        print("Connecting to sql")
    def disconnect(self):
        print("disconnecting to sql")

dataBase = input("enter database name : ")
className = globals() [dataBase]
obj = className()
obj.connect()
obj.disconnect()