#//program no 39
#//09/11/22
#//the given integer number is single digit,two digit,three digit,four digit or not


a = int(input())
if a>=0 and a<=9:
    print("the value is single digit :")
if a>=10 and a<=99:
    print("the value is two digit :")
if a>=100 and a<=999:
    print("the value is three digit :")
if a>=1000 and a<=9999:
    print("the value is four digit :")    
else:
    print("the value is not :")