num = input("Enter number : ");
output = 0;
count = 0;
count = len(num);

temp = int(num);
while temp != 0:
    temp = temp / 10;
    
    
temp = int(num);
while temp != 0:
    rem = int(temp % 10);
    output = output + pow(rem,count);
    temp = temp / 10;
    
if output == int(num):
    print(num,"is armstrong number");
else:
    print(num,"is not armstrong number");
