#money counting games
p=float(input("Enter the number of pennies= "))
n=float(input("Enter the number of nickels= "))
d=float(input("Enter the number of dimes= "))
q=float(input("Enter the number of quarters= "))
sum=p+n+d+q
if(sum==1):
    print("Congratulations! you win")
elif(sum<=1):
    print("The amount entered was less than 1$")
else:
    print("The amount entered was greater than 1$")
