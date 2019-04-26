def main(mass,velocity):
  ke=0.5*(mass*(velocity**2))
  return(ke)

mass=int(input("Enter the value for mass:"))
velocity=int(input("Enter the value for velocity:"))
print(main(mass,velocity))
  
