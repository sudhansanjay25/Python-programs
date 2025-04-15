def check(a):
    num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    b=0
    d=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i=0
    while(i<len(a)):
        for j in range(len(d)):
            if a[i]==d[j]:
                b+=num[j]
        i+=1
    return b
a=input()
print(check(a))