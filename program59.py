#//program no 59
#//16/11/22
#//biggest of three integer number using nested if ternay expression

a = int(input())
b = int(input())
c = int(input())
d=(a if a>c else c) if a>b else(b if b>c else c)

print(d)