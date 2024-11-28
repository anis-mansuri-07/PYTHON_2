with open("txtFiles/Prog_10.txt",'r') as f:
    content = f.read()
    content = content.replace("Gujarat","Gujrat")
    with open('txtFiles/Prog_10.txt','w') as x:
        x = x.write(content)    