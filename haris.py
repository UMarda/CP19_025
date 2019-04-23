s1=input("Enter a sentence:")
s2=input("Enter a sentence:")
se1=s1.split(" ")
se2=s2.split(" ")
for i in se1:
    for j in se2:
        if i==j:
            print(i)
