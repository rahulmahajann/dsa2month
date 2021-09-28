arr=[0,0,2,0,1,2]

z,o,t=0,0,0

for _ in arr:
    if _==0:
        z+=1
    elif _==1:
        o+=1
    else:
        t+=1

# ans=[]
count=0

for _ in range(z):
    # ans.append(0)
    arr[count]=0
    count+=1

for _ in range(o):
    # ans.append(1)
    arr[count]=1
    count+=1

for _ in range(t):
    # ans.append(2)
    arr[count]=2
    count+=1


print(arr)