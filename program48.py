#//program no 48
#//14/11/22
#//given operator is an arthmetic,relatonal,logical operator or any operator


a = input()
if a=='+' or a=='-' or a=='*' or a=='/' or a=='%' or a=='//' or a=='**':
    print("the value is arthmetic operator :")
if a=='>' or a=='<' or a=='>=' or a=='<=' or a=='==' or a=='!=':
    print("the value is relational operator :")
if a=='and' or a=='or' or a=='not':
    print('the value is logical operator :')
else:
    print("the value is other operator :")
    