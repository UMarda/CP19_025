import datetime
d=input("Enter:")
r=d.split("/")
date=datetime.datetime.now()
e=int(r[0])
f=int(r[1])
g=int(r[2])
if e>date.day or f>date.month or g>date.year:
    print("Greater")
elif e<date.day or f<date.month or g<date.year: 
    print("Lesser")
else:
    print("Equal")
