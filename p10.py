import sys
def histogram(lsth):
    for i in lsth:
        for j in range(0, i):
            sys.stdout.write("*")
        sys.stdout.write("\n")

lst = []
n = int(input("Enter the number elements:- "))
print("Enter elements")
for i in range(0, n):
    elem = int(input())
    lst.append(elem)
histogram(lst)