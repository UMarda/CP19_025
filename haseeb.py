positive=0
negative=0
while True:
    value=input("Enter an integer from -35 to 35: ")
   
    if (value=="x"):
        break
    else:
        value=int(value)

        if (value>0 and value<35):
            positive+=1

        elif (value < 0 and value > -35):
            negative+=1
        else:
            print("You did not enter the Correct Integer ")

print("Total Positive Numbers=",positive)
print("Total Negative Numbers=",negative)
print("The End")
