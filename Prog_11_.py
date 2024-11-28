import re
File_obj = open("txtFiles\Prog_11_.txt",'r')
Str = File_obj.read()
pattern ="credit hours- (\\d+)\npoint - (\\d+.\\d+)"
data= re.findall(pattern,Str)
print(data)
tp=0
tc = 0
for i in data:
    tp +=(int(i[0])*float(i[1]))
    tc += int(i[0])
print("CGPA : ",end=" ")
print(tp/tc)
File_obj.close()