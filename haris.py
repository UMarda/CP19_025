d=input("Enter a paragraph:")
v=""
d_c=True
for j in d:
    if j==".":
        d_c=True
    if j.isalpha() and d_c:
        v+=j.upper()
        d_c=False
    else:
        v+=j
print(v)        
