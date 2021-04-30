import string
s=sorted(input(),key=(string.ascii_letters+'1357902468').index)
for i in s:
    print(i,end='')
