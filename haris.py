n=input("Enter a string:")
a=n.split(",")
maxx=0
minn=99999999
for k in a:
    if int(k)>maxx:
        maxx=int(k)
    if int(k)<minn:
        minn=int(k)
print("Maximum value in this list is",maxx)
print("Minimum value in this list is",minn)
