#TRIANGLESHAPE
i=1
while(i<8):
    j=8
    while(j>i+1):
        print(" ",end=" ")
        j=j-1
    k=1
    while(k<i*2):
        print("*",end=" ")
        k=k+1
    i=i+1
    print(" ")
