import math
num=input("Enter a number: ")
while True:
    if num=="x":
        break
    else:
        num=int(num)
        sr=int(math.sqrt(num))
        if num==sr**2:
            print("The num ",num,"is a perfect square of ",sr)
        elif num!=sr**2:
            print("The num ",num,"is not a perfect square ")
    num=(input("Enter a number="))
    
