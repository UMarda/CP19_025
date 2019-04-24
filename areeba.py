#MAGICDATE
month=int(input("enter month="))
day=int(input("enter day="))
year=int(input("enter year"))
magic=month*day
if(magic==year):
    print("the date is magic")
else:
    print("error")
