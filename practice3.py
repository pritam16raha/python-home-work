p=int(input("print number to check palindrome or not \n"))
ll=[p]
print(ll)
ll2=[]
while(p>0):
    r=p%10
    p=p-r
    p=p/10
    ll2.append(r)
    print(ll2) 
if(ll==ll2):
    print("palindrom")
else:
    print("not palindrome")
    