p=int(input("which number you want to reverse?"))
ll=[]
while(p>0):
    r=p%10
    p=p-r
    p=p/10
    ll.append(r)
print(ll)
