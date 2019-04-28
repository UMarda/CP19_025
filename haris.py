def num():
    num=int(input("Enter the number:"))
    c=num
    a=1
    newnum=0
    while(num>0):
        rem=num%10
        num=num//10
        newnum=newnum*10+(rem)
    print("reverse number is",newnum)
  
    if(c==newnum):
        print("reverse number is same")
    else:
        print("reverse number is not same")
num()    
