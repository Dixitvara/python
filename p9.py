#a)
#checking number of vowels in string.
""""
inputString = input("Enter string : ");
vowels = ['a','e','i','o','u'];
count = 0;

for i in inputString:
    if i in vowels:
        count += 1;

print("Total vowels in string :", count);"""

#b)
#Count length of string without using len().
"""
s = "Shivkaran";
count = 0;
for i in s:
    count += 1;
print("Length of string :",count);
"""

#c)
#reverse string
'''
s = input("Enter string : ");
for i in range(len(s)-1,-1,-1):
    print(s[i],end="");
'''

#d)
#find and replace operation
'''
s = input("Enter strig : ");
print(s.replace(input("Enter char to replace :"),input("Enter new replacement :")));
'''

#e)
#check whether input string is palindrome or not
string = input("Enter string : ");
reverse = string[::-1];

if string == reverse:
    print("entered string is palindrome");
else:
    print("entered string is not palindrome");
