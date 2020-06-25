a=[]
n=int(input('enter number of elements:'))
for i in range(1,n+1):
    b=int(input('enetr element:'))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print('the even list',even)
print('the odd list',odd)
