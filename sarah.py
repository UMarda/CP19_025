#money counting games
p=float(input("enter the number of pennies="))
n=float(input("enter the number of nickels="))
d=float(input("enter the number of dimes="))
q=float(input("enter the number of quarters="))
sum=p+n+d+q
if(sum==1):
    print("congratulations! you win")
elif(sum<=1):
    print("the amount entered was less than 1$")
else:
    print("the amount entered was greater than 1$")