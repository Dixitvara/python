a = int(input("Enter num1 ==> "));
b = int(input("Enter num2 ==> "));
choice = 0;

#user defined functions
def Addition():
    print("a + b = ", a + b);
def Subtraction():
    print("a - b = ", a - b);
def Division():
    print("a / b = ", a / b);
def Multiplication():
    print("a * b = ", a * b);

while  choice!= 5:
    print("Choice: \n1.addition\n2.subtraction\n3.division\n4.multiplication\n5.exit");
    choice = int(input("Enter your choice : "));
    if choice == 1:
        Addition();
    elif choice == 2:
        Subtraction();    
    elif choice == 3:
        Division();
    elif choice == 4:
        Multiplication();
    elif choice >= 6:
        print("Enter valid choice!");
        break;
