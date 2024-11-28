
import re
fh = open("txtFiles/Prog_12.txt","a+")
def add(name,phone,github):
    fh.write(name+" "+phone+" "+github+"\n")
    fh.flush()
def remove(name,phone,github):
    pattern ="{}\\s{}\\s{}".format(name,phone,github)
    print(pattern)
    fh.seek(0)
    content = fh.read()
    print(content)
    match = re.search(pattern,content)
    if match:
     print(match)
     fh.seek(0)
     pre=fh.read(match.start())
     fh.seek(match.end()+2)
     after = fh.read()
     fh2 = open("txtFiles/Prog_12.txt","w")
     fh2.writelines(pre)
     fh2.writelines(after)
     fh2.close()
     fh.seek(0)
     print("now Content : \n"+fh.read())
    else:
        print("record is Not Found")
def updatePhone(name,phone):
     pattern = "{}\\s\\w+\\s\\w+".format(name)
     fh.seek(0)
     content = fh.read()
     match = re.search(pattern,content)
     if match:
         pre_content = content[:match.start()]
         after_content = content[match.end():]
         specific_content = content[match.start():match.end()]
         specific_content=specific_content[:specific_content.find(" ")]+" "+phone+specific_content[specific_content.rfind(" "):]
         fh2 = open("txtFiles/Prog_12.txt","w")
         fh2.write(pre_content)
         fh2.write(specific_content)
         fh2.write(after_content)
         fh2.close()
     else:
         print("record is not found")
def updateGithub(name,github):
     pattern = "{}\\s\\w+\\s\\w+".format(name)
     fh.seek(0)
     content = fh.read()
     match = re.search(pattern,content)
     if match:
         pre_content = content[:match.start()]
         after_content = content[match.end():]
         specific_content = content[match.start():match.end()]
         specific_content=specific_content[:specific_content.rfind(" ")]+" "+github
         fh2 = open("txtFiles/Prog_12.txt","w")
         fh2.write(pre_content)
         fh2.write(specific_content)
         fh2.write(after_content)
         fh2.close()
     else:
         print("record is not found")
def printByName(name):
     pattern = "{}\\s\\w+\\s\\w+".format(name)
     fh.seek(0)
     content = fh.read()
     match = re.search(pattern,content)
     if match:
         specific_content = content[match.start():match.end()]
         print(specific_content)
     else:
         print("record is not found")
def printAll():
    fh.seek(0)
    content = fh.read()
    print("Print All content :\n"+content)
def readAll():
    fh.seek(0)
    content = fh.read()
    print("Read All content : \n"+content)
l=True
while l:
    print("1.ADD")
    print("2.Remove")
    print("3.UpdatePhone")
    print("4.UpdateGithub")
    print("5.printByName")
    print("6.PrintAll")
    print("7.ReadAll")
    print("8.exit")
    choice  = int(input("Enter your choice"))
    if(choice == 1):
        name = input("Enter Friend Name : ")
        phone = input("Enter Mobile No : ")
        github = input("Enter GitHub Id : ")
        add(name,phone,github)
    elif(choice == 2):
        name = input("Enter Friend Name : ")
        phone = input("Enter Mobile No : ")
        github = input("Enter GitHub Id : ")
        remove(name,phone,github)
    elif(choice == 3):
         name = input("Enter Name : ")
         mobile_no = input("Enter New Mobile NO")
         updatePhone(name,mobile_no)
    elif(choice ==4):
        name = input("Enter Name : ")
        github = input("Enter New GitHub Id : ")
        updateGithub(name,github)
    elif(choice ==5):
        name= input("Enter Name : ")
        printByName(name)
    elif(choice ==6):
        printAll()
    elif(choice == 7):
        readAll()
    elif(choice == 8):
        l=False
    else:
        print("please,enter above one of number choice")
fh.close()