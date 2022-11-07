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
            
'''

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
'''
