# Created by Krishno Mondol
# Date: 29 June, 2025, Sunday
# Institution: Khulna University of Engineering & Technology, Bangladesh, Asia
# Department of Computer Science and Engineering


import numpy as np   # Importing NumPy module
import sys,os

# For clearing the screen
def clear_scr():
    os.system("cls" if os.name=="nt" else "clear") # Windows/Linux/MacOS

# Title Showing
def show_title():
    print("**           **     **    ***********  *******   ******  **     **       ******    **     **         ******  **    **  **          **     ***********   ******   *******")
    print("** **     ** **    ** **      **       **    **    **     **   **       **        ** **   **        **       **    **  **         ** **       **       **    **  **    **")
    print("**  **   **  **   **   **     **       **    **    **      ** **       **        **   **  **       **        **    **  **        **   **      **       **    **  **    **")
    print("**   ** **   **   *******     **       *******     **       ***        **        *******  **       **        **    **  **        *******      **       **    **  *******")
    print("**    ***    **   **   **     **       **  **      **      ** **        **       **   **  **        **       **    **  **        **   **      **       **    **  **  **")
    print("**           **   **   **     **       **   **   ******   **   **        ******  **   **  ********   ******   ******   ********  **   **      **        ******   **   **")


# Taking a matrix input
def operation():
    row, col, valid = 0, 0, True
    
    # Taking input with error handling
    while valid:
        try:
            print("Enter Dimensions--")
            r = int(input("Enter the number of row: "))
            c = int(input("Enter the number of col: "))

            if r != 0 and c != 0:
                valid = False     # Breaking the loop
                row, col = r, c   # Setting row and column
            else:
                print("Invalid Row or Column. Row or Column can't be zero. Try Again!")
        except ValueError:
            print("Row and Column must be an integer. Try Again!!")

    while True:
        try:
            user = list(map(int, input(f"Enter {row*col} elements: ").split())) # List Input
            if len(user) == row*col:
                break
            else:
                print(f"Invalid elements number. You entered {len(user)} elements. Should be {row*col} elements. Try Again.")
        except ValueError:
            print("Please enter valid integers separated by spaces. Try Again!")
    
    matrix = np.array(user).reshape(row, col)  # Converting list into desired numpy array
    return matrix

def AddSubProduct(type):
    # type = 1(Addition), 2(Subtraction), 3(Multiplication)
    mat1,mat2,chk = np.array([]),np.array([]),True

    if type==1:
        print("Addition of two matrices.")
    elif type==2:
        print("Substraction of two matrices.")
    elif type==3:
        print("Multiplication of two matrices.")

    if type==1 or type==2:
        while chk:
            try:
                print("Enterint the 1st matrix...")
                m1 = operation()
                print()
                print("Enterint the 2nd matrix...")
                m2 = operation()

                if m1.shape==m2.shape:  # Checking condition
                    chk = False
                    mat1 = m1
                    mat2 = m2
                else:
                    print("Addition or Substraction of different dimensions is not possible. Dimensions must be same. Try Again!")
            except ValueError:
                print("Invalid elements. Please enter valid numbers. Try again!")
        if type==1:
            return mat1 + mat2
        if type==2:
            return mat1 - mat2
    else:
        while chk:
            try:
                print("Enterint the 1st matrix...")
                m1 = operation()
                print()
                print("Enterint the 2nd matrix...")
                m2 = operation()

                if m1.shape[1]==m2.shape[0]:  # Checking Condition
                    chk = False
                    mat1 = m1
                    mat2 = m2
                else:
                    print("Multiplication is not possible. The column of 1st matrix and the row of 2nd matrix must be equal")
            except ValueError:
                print("Invalid elements. Please enter valid numbers. Try again!")
        return mat1 @ mat2
        
def DetInvTrans(type):
    mat, chk = np.array([]), True
    # type = 4(Transpose), 5(Inverse), 6(Determint)

    if type==4:
        print("Transposing a matrix.")
    elif type==5:
        print("Inversing a matrix.")
    elif type==6:
        print("Finding Determinant of a matrix.")

    if type == 5 or type == 6:
        while chk:
            try:
                print("Enter the matrix--")
                m = operation()
                if m.shape[0] == m.shape[1]:  # Checking Condition
                    mat = m
                    chk = False
                else:
                    print("Invalid matrix. Must be a square matrix. Try again!")
            except ValueError:
                print("Invalid elements. Please enter valid numbers. Try again!")

        if type == 5:
            while True:
                if np.linalg.det(mat) == 0:  # Checking condition
                    print("The determinant is zero. Inverse not possible! Try again.")
                    try:
                        mat = operation()
                        if mat.shape[0] != mat.shape[1]:
                            print("Invalid matrix. Must be square.")
                            break
                        else:
                            continue
                    except ValueError:
                        print("Invalid elements. Try again!")
                else:
                    return np.linalg.inv(mat)
        else:
            return np.linalg.det(mat)

    else:
        while True:
            try:
                print("Enter the matrix--")
                mat = operation()
                return mat.T
            except ValueError:
                print("Invalid elements. Please enter valid numbers. Try again!")



def Menu():
    show_title() # Title
    print()
    print("Operations:")
    print("1.Addition\n2.Subtraction\n3.Multiplication")
    print("4.Transpose\n5.Inverse\n6.Determinant\n7.Exit")
    selection = [1,2,3,4,5,6,7]
    type,v,result = 0,True,np.array([])
    while v:
        try:
            t = int(input("Input the operation type: "))

            if t in selection:
                v = False
                type = t
            else:
                print("Selection must be between 1 and 7. Try Again!!")
        except ValueError:
            print("Selection must be an integer. Try Again!")
    if type==7:
        return
    clear_scr() # Clearing Screen
    if type==1 or type==2 or type==3:
        result = AddSubProduct(type)
    else:
        result = DetInvTrans(type)
    
    if result != None:
        if type==1:
            print("Result of Addition below:")
        elif type==2:
            print("Result of Substraction below:")
        elif type==3:
            print("Result of Multiplication below:")
        elif type==4:
            print("Transpose of the matrix: ")
        elif type==5:
            print("Inverse of the matrix: ")
        else:
            print("Determinant of the matrix: ")
        print(result)
    print()

    print("1.Return to main menu\n2.Exit")
    select,vv = 0,True
    while vv:
        try:
            ss = int(input("Enter the selection: "))
            if ss==1 or ss==2:
                select = ss
                vv = False
            else:
                print("Invalid Input!! Selection must be 1 or 2. Try Again!!")
        except ValueError:
            print("Invalid Input!! Input must be a number. Try Again!!")
    if select==1:
        clear_scr()
        Menu()
    else:
        clear_scr()
        return
        
    
def main():
    Menu()

if __name__=="__main__":
    main()
