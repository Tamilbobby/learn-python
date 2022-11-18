#//program no 57
#//15/11/22
#//biggest of three integer number using ternay expression

a = int(input())
b = int(input())
c = int(input())
x=a if a>b else b
x=x if x>c else c
print(x)