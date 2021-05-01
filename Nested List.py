n=int(input())
l=[]
m=[]
for i in range(n):
    name=input()
    mark=float(input())
    l.append([name,mark])
    m.append(mark)
l.sort()
m.sort(reverse=True)
m.pop()
for name,mark in l:
    if mark==m[-1]:
        print(name)
