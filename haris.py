num=int(input("Enter No : "))
def fibo(a,b):
    c=0
    print("0","1",end=' ')
    for i in range(1,num-2):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
        c=a+b
    return c
print(fibo(0,1))
