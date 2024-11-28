import Module_5 as Result

Result.add("Math",10,8)
Result.add("Science",10,9)
Result.printList()
cgpa = Result.cgpa()
print(f"CGPA : {cgpa}")


Result.add("Social Science",10,5.5)
Result.drop("Math")
Result.printList()

cgpa = Result.cgpa()
print(f"CGPA : {cgpa}")