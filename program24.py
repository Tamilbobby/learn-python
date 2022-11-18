#//program no 24
#//o1/11/22
#//products of the digit of three digits no

n = int(input())

r = n%10
q = n//10
r1 = q%10
q1 = q//10

product = (r*r1*q1)
print(r)
print(q)
print(r1)
print(q1)
print(product)
