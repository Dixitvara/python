from tabulate import tabulate
import pandas as p
file = p.read_csv("python/excel.csv")
print(tabulate(file, tablefmt = "html"))