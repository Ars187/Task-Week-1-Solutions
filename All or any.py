s=list(input().split())
a=-1
for i in s:
    if int(i)<0:
        a=-1
        break
    else:
        if(i==i[::-1]):
            a=1
if a==1:
    print("True")
else:
    print("False")
    
    
