"""
user will input no students
input
user will input rollno and name for n students
    input
user will input marks of 3 subjects for n students
    input
store rollno and name in studentInfo.txt file
    1-Asit
    2-Nimesh
    3-Harshal
    4-Viren
store rollno and marks of 3 subjects in studentMarks.txt file
    1-99-99-99
    2-88-88-88
    3-77-77-77
    4-92-92-92
calculate the average of 3 subjects of marks
grade calculate
    store data in file by keep the average in descending order
    rollno-name-average
    80 to 100=>Agrade.txt
    1-Asit-99
    4-Viren-92
    2-Nimesh-88
    60 to 80=>Bgrade.txt
    3-Harshal-77
    40 to 60=>Cgrade.txt
"""

studentInfo = open("studentInfo.txt", "w+")
studentMarks = open("studentMarks.txt", "w+")

A = open("Agrade.txt", "w+")
B = open("Bgrade.txt", "w+")
C = open("Cgrade.txt", "w+")

def fn1(n):
    for i in range(n):
        roll_no = input("Enter Roll No=")
        name = input("Enter Name=")
        studentInfo.write(roll_no + " - " + name + "\n")
        studentMarks.write(roll_no)

        for j in range(3):
            marks = input("Enter marks of student:")
            studentMarks.write(" - " + marks)
        studentMarks.write("\n")

def fn2():
    studentInfo.seek(0)
    studentMarks.seek(0)
    ls1 = studentInfo.readlines()
    ls2 = studentMarks.readlines()
    print(ls1, ls2)
    return ls1, ls2

def fn3(ls1, ls2):
    ls3 = []
    ls4 = []
    for i in ls1:
        dummy = i.replace("\n", "")
        templs = dummy.split(" - ")
        print("ls1=", templs)
        ls3.append(templs)

    for j in ls2:
        dummy = j.replace("\n", "")
        templs = dummy.split(" - ")
        print("ls2=", templs)
        avg = (int(templs[1]) + int(templs[2]) + int(templs[3])) // 3
        ls4.append([templs[0], str(avg)])
    print("ls3=", ls3)
    print("ls4=", ls4)
    return ls3, ls4

def fn4(ls3, ls4):
    ls5 = []
    averageSet = {0}
    for i in ls3:
        for j in ls4:
            if i[0] == j[0]:
                dummy = i[0] + "-" + i[1] + "-" + j[1]
                averageSet.add(int(j[1]))
                ls5.append(dummy.split("-"))

    sortedList = list(averageSet)
    sortedList.sort(reverse=True)
    print(averageSet)
    print(sortedList)
    print("ls5= ",ls5)

    for i in sortedList:
        for j in ls5:
            if int(j[2]) == i and 80 < int(j[2]) <= 100:
                A.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")
            elif int(j[2]) == i and 60 < int(j[2]) <= 80:
                B.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")
            elif int(j[2]) == i and 40 < int(j[2]) <= 60:
                C.write(j[0] + "-" + j[1] + "-" + j[2] + "\n")

nostu = int(input("Enter No. Of students:"))
fn1(nostu)
ls1, ls2 = fn2()
ls3, ls4 = fn3(ls1, ls2)
fn4(ls3, ls4)

studentInfo.close()
studentMarks.close()
