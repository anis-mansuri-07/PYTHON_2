a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
c=[[],[],[]]
#initialize matrix

#display first matrix
def Initialize_matrix():
    
    for i in range(3):
        for j in range(3):
            a[i][j]=int(input("\nEnter value for a[{}][{}]".format(i,j)))
    
#display second matrix
    print("  Second Matrix")
    for i in range(3):
        for j in range(3):
            b[i][j]=int(input("\nEnter value for b[{}][{}]".format(i,j)))
   


def print_matrix():
   print("First Matrix")
   for i in range(3):
        for j in range(3):
            print(" ", a[i][j], end="   ")
        print("\n")
   print("  Second Matrix") 
   for i in range(3):
        for j in range(3):
            print(" ", b[i][j], end="   ")
        print("\n")
#addition of matrix
def Addition_matrix():
    print("Addition of Matrix")
    for i in range(3):
        for j in range(3):
            print(" ", a[i][j] + b[i][j], end="   ")
        print("\n")

#multipication of matrix
def Multipicaton_matrix():
    print("Multipicaton of Matrix")
    for i in range(3):
        for j in range(3):
           mul=0
           for k in range(3):
              mul+=(a[i][k]*b[k][j])
           print(mul,end=" ")
        print("\n")