#Roulette Wheel Colors

Pocket = int (input("Enter pocket no from (0-36): "))

if (Pocket < 0 or Pocket > 36):
    print("Error: Pocket no is out of range (0-36),")
elif (Pocket == 0):
    print ("Pocket color: GREEN")
elif ( (Pocket >= 1 and Pocket <= 10) or (Pocket >= 19 and Pocket <= 28)):
    if (Pocket%2 == 0):
        print ("Pocket color: RED")
    else:
        print ("Pocket color: BLACK")
else:
    if (Pocket%2 != 0):
        print ("Pocket color: RED")
    else:
        print ("Pocket color: BLACK")
