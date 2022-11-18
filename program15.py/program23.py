#//program no 23
#01/11/22
#//sum of the digit of three digit number

n = int(input())
r = n%10
q = n//10
r1 = q%10
q1 = q//10
s = (r+r1+q1)
print(s)
print(r)
print(q)
print(r1)
print(q1)