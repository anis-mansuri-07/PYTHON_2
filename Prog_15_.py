import re
Number_file = """Hello i am anish mansuri and i am working as a software developer in microsoft
 here i am giving my bio- data : 
 M_No : 1052036408 here is my mobile number
 my secondery mobile number ::  5258469586"""
Check  = r"\d{10}" 
find  = re.findall(Check,Number_file)
for i in find:
    print(i)

