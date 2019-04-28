def diamond():
    g=int(input("Enter shape lenght:"))
    h=int(input("Enter the first number:"))
    x=int(input("Enter second number:"))
    i=1
    while(i<=g-1):
        j=g-1
        while(j>=i):
            print(" ",end=' ')
            j-=1
        k=1
        while(k<i*2):
            if(k==i):
                print(h,end=' ')
            else:
                print(x,end=' ')
            k+=1
    
        i+=1
        print("")
    for z in range(1,(g*2)):
        print(h,end=' ')
    print("")
    a=1
    while(a<=g-1):
        b=2
        while(b<=a+1):
            print(" ",end=' ')
            b+=1
        c=g-1
        while(c>=a):
            if(c==a):
                print(h,end=' ')
            else:
                print(x,end=' ')
            c-=1
            d=g-2
        while(d>=a):
            print(x,end=' ')
            d-=1
        a+=1
        print()
diamond()
