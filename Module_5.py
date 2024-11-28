courseList = []
creditList = []
earnedList = []

def add(course,credit,earn):
    courseList.append(course)
    creditList.append(credit)
    earnedList.append(earn)
    print("Course Added")

def drop(course):
    if course in courseList:
        index = courseList.index(course)
        courseList.pop(index)
        creditList.pop(index)
        earnedList.pop(index)
        print(course,"course droped..")
    else:
        print("Course not found..")

def printList():
    if len(courseList) > 0:
        print("\nCourse Details --  ")
        i=0
        print("{0}   {1}   {2}".format("Course","credit","earned"))
        for course in courseList:
            credit = creditList[i]
            earn = earnedList[i]
            print(f"{course}   {credit}   {earn}")
            i+=1
    else:
        print("No course are available..")

def cgpa():
    if len(creditList) > 0:
        total,totalcredit = 0,0
        i=0
        for credit in creditList:
            earn = earnedList[i]
            total += (credit*earn)
            totalcredit += credit
            i+=1

        return total / totalcredit
    else:
        print("No course are available to count CGPA.. ")