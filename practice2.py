p=int(input("print number to see sum \n"))
sum=0
while(p>0):
    r=p%10
    p=p-r
    p=p/10
    sum=sum+r
print(sum)
