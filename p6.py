#list for odd elements
odd = [];
print("Enter 10 numbers : ");
for i in range(0,10):
    userInput = int(input());
    if userInput % 2 != 0:
        odd.append(userInput);
if bool(odd):
    print("Largest odd is",max(odd));
else:
    print("No odd number found!");
