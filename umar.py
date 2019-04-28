##################################Question 4#####################################
a=input("Enter the paragraph : ")
b=" "
l=len(a)
for i in range(l):
    if i==0:              # capital first letter of para
        b+=a[i].upper()
    if a[i]=="." and i+1!=l:  # after the full stop without give a space 
        b+="."
        c=a[i+1].upper()        # again capital the letter 
        b+=c
    else:
        d=len(b)
        if b[d-1]!=a[i].upper():
            b+=a[i]
print(b)
#################################################################################
