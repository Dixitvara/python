num = int(input("Enter number : "));
total = 0;
temp = num;

while num != 0:
    rem = num % 10;
    total = total * 10 + rem;
    num = int(num / 10);
    
if total == temp:
    print(total,"is palindrome number");
else:
    print(total,"is not palindrome number");
