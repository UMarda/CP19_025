#Grade Calculator

T1=int(input("Enter a Test 1 points: "))
T2=int(input("Enter a Test 2 points: "))
Exam=int(input("Enter a Main exam points: "))
t=T1+T2+Exam

if(T1<0 or T1>25 or T2<0 or T2>25 or exam<0 or Exam>50):
     print("Error")
        
elif(t<50):
    print("Fail")
elif(exam<25):
    print("Fail")

elif(t>80):
    print("Distinction")

elif(t>60 and t<80):
    print("Credit")

elif(t<=60):
     print("Pass")

elif(t<60 and t>=50):
     print("Pass")
esle:
    print("End")
