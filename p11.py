num = int(input("enter number : "));
def fibo():
    a, b = 0, 1;
    print(a, b, end = " ");
    for i in range(num):
        c = a + b;
        a = b;
        b = c;
        print(c, end =" ");
fibo();