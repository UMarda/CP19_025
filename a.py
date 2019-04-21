#PALINDROME
a=input("enter the word : ")
if a[::1]==a[::-1]:
    print("Palindroma")
else:
    print("not Palindroma")