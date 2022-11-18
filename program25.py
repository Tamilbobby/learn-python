#//program no 25
#//08/11/22
#/reverse the digit three digit num 

n = int(input())

r = n%10
q = n//10
r1 = q%10
q1 = q//10
a = r*100
b = r1*10
c = q1*1
add = (a+b+c)
print(add)
print(a)
print(b)
print(c)