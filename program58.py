#//program no 58
#//15/11/22
#//smallest of three integer number using ternay expression

a = int(input())
b = int(input())
c = int(input())
x=a if a<b else b
x=x if x<c else c
print(x)