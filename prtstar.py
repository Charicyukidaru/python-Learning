
nu1 = int(input("Enter the number of stars : "))
tp = input("Enter the type of stars : ").upper()

b = 0
c = 0
if tp == "A":
    for a in range(0,nu1):
        a = a + 1
        print("*"*a)
elif tp == "B": 
    for a in range(0,nu1):
        a = a + 1
        b = nu1 - a
        print(" "*b,"*"*a)
elif tp == "C":
    for a in range(0,nu1):
        b = nu1 - a
        c = (2*a+1)
        print(" "*b,"*"*c)
elif tp == "D":
    for a in range(-nu1,0):
        b = a + nu1 
        c = 2*(-a)-1
        abs(c)
        print(" "*b,"*"*c)
else:
    print("no type")

