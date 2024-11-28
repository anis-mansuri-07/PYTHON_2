with open("txtFiles/Prog9.txt",'r') as file:
    Read_file = file.read()
    print("Before Split\n",Read_file)
    
    File_Split = Read_file.split(" ")
    print("After Split",File_Split)
    
    with open("txtFiles/Prog9_Copy.txt",'w+') as C_obj:
        for i in File_Split:
            C_obj.write(i+" ")
        C_obj.seek(0)
        Obj_Read = C_obj.read()
        print("After Join\n",Obj_Read)
        
    
    
    
    