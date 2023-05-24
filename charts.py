#Bar chart
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
mat.show()

#histogram chart
import pandas as p
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

#pie chart
import pandas as p
import matplotlib.pyplot as mat

x = [10, 20, 30, 40, 50]
dept = ["sales", "production", "hr", "finance", "majur"]
color = ["red", "green", "blue", "yellow","pink"]
mat.pie(x, labels = dept, colors = color, startangle = 90, explode = (0, 0.2, 0.4, 0, 0), shadow = True, autopct = "%.2f%%")
mat.title("www.skyadav.com")
mat.legend()
mat.show()

#line chart
import pandas as p
import matplotlib.pyplot as mat

y = [1450,2000,6430,2500,3400]
x = [9,10,11,14,20]

mat.plot(x, y, label = 'sales data')
mat.xlabel('employee id')
mat.ylabel('employee salary')
mat.title('www.skyadav.com')
mat.legend()
mat.show()