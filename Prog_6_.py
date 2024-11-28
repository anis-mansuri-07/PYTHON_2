import Module_6 as mo
t=True
while(t):
    print("1.Intialize Matrix:")
    print("2.Addition Matrix:")
    print("3.Multipication")
    print("4.Print Matrix")
    print("5.exit")
    c=int(input("Enter your choice:"))
    if(c==1):
        mo.Initialize_matrix()
    elif(c==2):
        mo.Addition_matrix()
    elif(c==3):
        mo.Multipicaton_matrix()
    elif(c==4):
        mo.print_matrix()
    elif(c==5):
        t=False
    else:
        print("\nPlease,enter valid choice")