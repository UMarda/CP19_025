# Number Analyser 

N=int(input("Please Enter a Number: "))

if(N>0):
  print("Positive Number")
  if(N%2==0):
    print("Even")
  else:
    print("Odd")
else:
  print("Negative Number")
