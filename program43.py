#//program no 43
#//10/11/22
#//the given charater is uppercase,lowercase,digit,special character or not


a = input("enter the value :")
if a>='A' and a<='z':
    print("the value is uppercase :")
if a>='a' and a<='z':
    print("the value is lowercase :")
if a>='0' and a<='9':
    print("the value is digit :")
if a>='@' and a<='*':
    print("the value is special character :")
else:
    print("the value is not :")