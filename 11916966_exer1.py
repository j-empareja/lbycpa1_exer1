##################################################
# Author: John Emmanuel E. Pareja
# Date: January 25, 2020
# Course: LBYCPA1

# Program Description
#  4-VARIABLE EQUATION CALCULATOR>
##################################################

print("Welcome to the Engineering Calculator.")
print()

print("Here are some available equations:")
print("[1] ELECTRIC FORCE = (Coulomb's Constant * Charge1 * Charge2) / (Distance^2)")
print("[2] RESISTANCE = (Resistivity * Length) / Area")
print()
print("[0] QUIT PROGRAM")
print()

eqnChoice = ()
varMiss = ()

force = ()
q1 = ()
q2 = ()
r = ()

resist = ()
rho = ()
length = ()
area = ()
#Variable declaration

while(eqnChoice == "1" or "2" or "0"):
    eqnChoice = input("Please select an equation to solve. ")
    #Decision for equation

    print()
    print()
    if eqnChoice == "1":
    #for electric force

        print("You have chosen ELECTRIC FORCE.")
        print("[1] ELECTRIC FORCE")
        print("[2] Charge1")
        print("[3] Charge2")
        print("[4] Distance")
        print()
        print("[0] RETURN TO PREVIOUS OPTIONS")
        print()
        varMiss = input("Please select the missing variable to be solved in the given equation. ")
        print()
        print()

        while(varMiss == "1" or "2" or "3" or "4" or "0"):
            if varMiss == "1":
                print("You are solving for: ELECTRIC FORCE.")
                print()

                while True:
                    try:
                        q1 = float(input("Please enter a value for the first charge: "))
                        q2 = float(input("Please enter a value for the second charge: "))  
                        r = float(input("Please enter a value for the distance: "))
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                # Computation
                final = (8900000000 * q1 * q2) / (r * r)

                print()
                print("ELECTRIC FORCE is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "2":
                print("You are solving for: Charge1.")
                print()

                while True:
                    try:
                        force = input("Please enter a value for the ELECTRIC FIELD: ")
                        force = float(force)
                        q2 = input("Please enter a value for the Charge2: ")  
                        q2 = float(q2)
                        r = input("Please enter a value for the Distance: ")
                        r = float(r)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = ( force * (r * r) / (8900000000 * q2))

                print()
                print("Charge1 is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "3":
                print("You are solving for: Charge2.")
                print()

                while True:
                    try:
                        force = input("Please enter a value for the ELECTRIC FIELD: ")
                        force = float(force)
                        q1 = input("Please enter a value for the Charge1: ")  
                        q1 = float(q1)
                        r = input("Please enter a value for the Distance: ")
                        r = float(r)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = ( force * (r * r) / (8900000000 * q1))

                print()
                print("Charge2 is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "4":
                print("You are solving for: Distance")
                print()

                while True:
                    try:
                        force = input("Please enter a value for the ELECTRIC FIELD: ")
                        force = float(force)
                        q1 = input("Please enter a value for the Charge1: ")  
                        q1 = float(q1)
                        q2 = input("Please enter a value for the Charge2: ")
                        q2 = float(q2)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = (8900000000 * q1 * q2) / (force * force)

                print()
                print("Distance is equal to: ",final)

                break
                #breaks loop statement
            
            elif varMiss == "0":
                break
                #breaks loop statement -> goes to main menu

            else:
                varMiss = input("Please enter a valid number. ")
    

    elif eqnChoice == "2":
    #for resistance

        print("You are solving for: RESISTANCE")
        print("[1] RESISTANCE")
        print("[2] Resistivity")
        print("[3] Length")
        print("[4] Area")
        print()
        print("[0] RETURN TO PREVIOUS OPTIONS")
        print()
        varMiss = input("Please select the missing variable to be solved in the given equation. ")
        print()
        print()

        while(varMiss == "1" or "2" or "3" or "4" or "0"):
            if varMiss == "1":
                print("You are solving for: RESISTANCE.")
                print()

                while True:
                    try:
                        rho = input("Please enter a value for the Resistivity: ")
                        rho = float(rho)
                        length = input("Please enter a value for the Length: ")  
                        length = float(length)
                        area = input("Please enter a value for the Area: ")
                        area = float(area)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = (rho * length) / area

                print()
                print("RESISTANCE is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "2":
                print("You are solving for: Resistivity.")
                print()

                while True:
                    try:
                        resist = input("Please enter a value for the RESISTANCE: ")
                        resist = float(resist)
                        length = input("Please enter a value for the Length: ")  
                        length = float(length)
                        area = input("Please enter a value for the Area: ")
                        area = float(area)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = (resist * area) / length

                print()
                print("Resistivity is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "3":
                print("You are solving for: Length.")
                print()

                while True:
                    try:
                        resist = input("Please enter a value for the RESISTANCE: ")
                        resist = float(resist)
                        rho = input("Please enter a value for the Resistivity: ")  
                        rho = float(rho)
                        area = input("Please enter a value for the Area: ")
                        area = float(area)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = (resist * area) / rho

                print()
                print("Length is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "4":
                print("You are solving for: Area.")
                print()

                while True:
                    try:
                        resist = input("Please enter a value for the RESISTANCE: ")
                        resist = float(resist)
                        rho = input("Please enter a value for the Resistivity: ")  
                        rho = float(rho)
                        length = input("Please enter a value for the Length: ")
                        length = float(length)
                    except ValueError:
                        print()
                        print("INVALID INPUT. Start Again.")
                        print()
                        continue
                    else:
                        break

                final = (rho * length) / resist

                print()
                print("Area is equal to: ",final)

                break
                #breaks loop statement

            elif varMiss == "0":
                break
                #breaks loop statement -> goes to main menu

            else:
                varMiss = input("Please enter a valid number. ")

    elif eqnChoice == "0":
        print("Thank you for using the program.")
        exit()
    
    else:
        print("Please enter a valid number. ")
        print()

else:
    eqnChoice = input("Please enter a valid number. ")