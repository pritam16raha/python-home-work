'''
p=int(input("enter the no of numbers to find greatest among them \n"))
ll=[]
for i in range(p):
    n = int(input("Input numbr: "))
    ll.append(n)
    
if(ll[0]>ll[1]):
    if(ll[0]>ll[2]):
        print("max is:",ll[0])
    else:
        print("max is:",ll[2])
else:
    if(ll[1]>ll[2]):
        print("max is",ll[1])
    else:
        print("max is",ll[2])
            


num1=int(input("Input First Number: "))
num2=int(input("Input Second Number: "))
num3=int(input("Input Third Number: "))

if num1>num2:
    if num1>num3:
        print(num1, "is Maximum")
    else:
        print(num3, "is Maximum")
else:
    if num2>num3:
        print(num2, "is Maximum")
    else:
        print(num3, "is Maximum")



p=int(input("enter year to check leap year or not \n"))
if(p%400==0):
   print(p,"is leap year")
else:
    print(p,"is not leap year")





a=int(input("print the value of first coefficient"))
b=int(input("print the value of second coefficient"))
c=int(input("print the value of third coefficient"))
e=b*b
d=root(e-(4*a*c))
if(d>0):
    

a=int(input("type value to see word \n"))
num=['one','two','three','four','five','six','seven','eight','nine','ten']
if(a<10):
   print(num[a-1])
else:
    print("invalid order")
'''
p=int(input("range")
ll=['p']
sum=0
for sum in range (1,p)
     print(sum) 
