#A)

#csv file
import pandas as p
import xlrd

filepath = "python/excel.csv"
df = p.read_csv(filepath)
print(df)

#list of tuples
import pandas as p
empdata = [
    (100,'bipin',10000,'01-01-2002'),
    (101,'mohit',20000,'01-01-2002'),
    (102,'rajesh',30000,'01-01-2002'),
    (103,'mitesh',14000,'01-01-2002'),
    (104,'minu',41000,'01-01-2002'),
]

df = p.DataFrame(empdata,columns = ["empId","empname","salary","doj"])
print(df)

#Dictionary
import pandas as p
empdate = {
    "empid" : [101,102,103],
    "ename" : ["bipin","hitesh","jitesh"],
    "salary" : [10000,20000,30000],
    "doj" : ['01-01-2020','02-12-2023','01-02-2022']
}
df = p.DataFrame(empdate)
print(df)

#B)
#data frame shape
import pandas as p
df = p.read_csv("python/excel.csv")
print(df)
print(df.shape)

#head
import pandas as a
df = a.read_csv('python/excel.csv')
print(df.head(2))

#tail
import pandas as a
df = a.read_csv('python/excel.csv')
print(df.tail(2))

#C)
#retriving columns 
import pandas as p
df = p.read_csv("python/excel.csv")
print(df)
print(df.shape)
print(df.columns)

#D)
import pandas as a
df = a.read_csv("python/excel.csv")
print("min salary: ",df['salary'].min())
print("max salary: ",df['salary'].max())

#E)
import pandas as p
df = p.read_csv("python/excel.csv")
print(df.index)

#F)
import pandas as p
df = p.read_csv('python/excel.csv')
df.set_index('empid',inplace=True)
print(df.loc[1004])

#G)
import pandas as p
import xlrd
df=p.read_csv("python/excel.csv")
df1=df.groupby("empname")
print(df1.first())

#H)
import pandas as p
import xlrd
filePath="python/excel.csv"
df=p.read_csv(filePath)
df1=df.fillna(0)
print(df1)
