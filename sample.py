
a=input("Enter the 1rst Number: ")
b=input("Enter the 2nd number: ")
if int(a) > 0:
    print('a is positive number')
elif int(a) < 0:
    print("a is negative number")
else: 
    print("a is zero")
print("Numbers before swaping:")
print('a='+a+"\n"+"b="+b)
a,b=b,a
print("Numbers after swapping: ")
print('a='+a+"\n"+"b="+b)\
