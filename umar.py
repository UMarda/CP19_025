##########finding factorial################# 
num = int(input("Please enter a number: "))
if(num>=0):
    factorial = 1
    i = 1
    while(i<=num):
        factorial = factorial*i
        i=i+1
    print(factorial)
else:
    print("Enter positive number")
############################################
