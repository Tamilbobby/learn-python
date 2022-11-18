#//program no 36
#//09/11/22
#//the given integer number polymorpishm or not:

    

n =int(input())
r = n%10
q = n//10
r1 = q%10
q1 = q//10
a = r*100
b = r1*10
c = q1*1
r = (a+b+c)
if n==r:
    print("polymorpihsm")
else:
    print("not polymorpishm")