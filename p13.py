choice = None
while choice != 5:
    print("(1)Read line\n(2)Read lines\n(3)Write lines\n(4)View file\n(5)Exit")
    choice = int(input("Enter choice : "))
    match choice:
        case 1:
            file = open("python/hello.txt", "r")
            print(file.readline())
        case 2:
            file = open("python/hello.txt", "r")
            print(file.readlines())
        case 3:
            f = open("python/hello.txt", "a")
            f.writelines(input("enter data : "))
            f.close()
        case 4:
            file = open("python/hello.txt", "r")
            print(file.readlines())
