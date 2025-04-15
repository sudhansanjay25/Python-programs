def check(a):
    num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    b=""
    d=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i=0
    while(a>0):
        if a//num[i]>0:
            c=a//num[i]
            a%=num[i]
            for j in range(c):
                b+=d[i]
        i+=1
    return b
a=int(input())
print(check(a))