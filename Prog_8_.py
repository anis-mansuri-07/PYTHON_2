#Read Write Copy File

with open('txtFiles/Prog8.txt','r') as myfile:
    Read = myfile.read()
    with open("txtFiles/Prog8_copy.txt",'w+') as file:
        file.write(Read)
    print(Read)
    