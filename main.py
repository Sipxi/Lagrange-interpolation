from sympy import *
import os

x = symbols('x')    # Define x and y for sympy
y = symbols('y')

#   Get coordinates function
def input_coordinates() -> int:
    coordinates = []
    num_of_coordinates = int(input("Enter number of coordinates: "))
    for i in range(num_of_coordinates):
        first = int(input(f'x{i}: '))
        second = int(input(f'y{i}: '))
        coordinates.append([first,second])
    return coordinates
 
#   Printing table 
def printTable(coordinates) -> None:
    num_of_coordinates = len(coordinates)
    os.system('cls') # clear the screen
    print("\t \t Table 	\n")
    print("-"*20)
    for i in range(3):
        if i == 0:
            print("i:  ", end =" " )
        elif i == 1:
            print('xi: ', end =" ")
        elif i == 2:
            print('yi: ', end =" ")
        for j in range(num_of_coordinates):
            if i == 0:
                print(f'|{j}|', end =" ")
            elif i == 1:
                print(f'|{coordinates[j][0]}|', end =" ")
            elif i == 2:
                print(f'|{coordinates[j][1]}|', end =" ")
        print('\n')
    print("-"*20)

#Get the interpolated equation from coordinates           
def interpolate(coordinates) -> object:
    num_of_coordinates = len(coordinates)
    eq = 1
    for i in range(num_of_coordinates):
        term = coordinates[i][1]
        for j in range(num_of_coordinates):
            if j != i: # If
                term *= (x - coordinates[j][0]) / (coordinates[i][0] - coordinates[j][0]) # Sypmpy 'x'
    # In the end we're getting the equationg
    eq = Eq(term,y) # passing it to sympy 'Eq' and solving for 'y'
    return eq
    
#   Fancy print
def get_to_print(solved) -> str:
    return f'Solution is: y = {solved[0]}' 

if __name__ == "__main__":
    coordinates = input_coordinates()
    
    printTable(coordinates)
    
    eq = interpolate(coordinates)
    solved = solve (eq, y)
    
    print(get_to_print(solved))
    input("Press Enter to close...")