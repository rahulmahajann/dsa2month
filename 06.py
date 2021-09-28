st=[1,5,6,7,5]
s=0
e=len(st)-1
while(s<e):
    st[s],st[e]=st[e],st[s]
    s+=1
    e-=1
print(st)