def check(c,k):
    if sum(c)<k:
        k%=sum(c)
    if k==0:
        return 0
    for i in range(len(c)):
        if c[i]>k:
            return i
        k-=c[i]

c=eval(input())
k=int(input())
print(check(c,k))
#%%
