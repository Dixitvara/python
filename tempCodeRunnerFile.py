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