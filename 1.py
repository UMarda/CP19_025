r=int(input("range:"))
positive=0
negative=0
for i in range(r):
  y=input()
  if(y=="x"):
    print("the end")
    break
  else:
    z=int(y)
    if(z<0):
      negative+=1
    elif(z>=0):
      positive+=1
print("total positive numbers:",positive,"\nTotal negative numbers:",negative)
    