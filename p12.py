def fact(n):
    # ans = 1;
    # for i in range(n,1,-1):
    #     ans *= i;

    if n == 1 or n == 0:
        return 1;
    else:
        return (n * fact(n - 1));
num = 6;
print("factorial of", num,"is : ", fact(num));