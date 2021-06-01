"""
TASK2:
student={
's1':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's2':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's3':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's4':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
's5':{
    'rollno':input,
    'name':input,
    'marks':input,
    'grade':None,
},
s6:{
'rollno':input,
'name':input,
'marks':input,
'grade':None,
}
}

create the data structure dynamically
user will input no of students
user will input the data roll no., name, and marks.
find the grade and assign
90 to 100->A grade assign
80 to 90->B grade assign
60 to 80->C grade assign
40 to 60->D grade assign
<40->Fail
<0 or > 100=>invalid marks=>None
display the student dictionary
student={
's1':{
    'rollno':1,
    'name':"asit",
    'marks':88,
    'grade':"B"
}
}
"""
n=int(input("Enter number of students: "))
i=1
r=[]
while i<n+1:
    id1=1
    name=str(input("enter name: "))
    roll=int(input("enter roll number: "))
    marks=float(input("enter overall marks: "))
    if marks>=90 and marks<=100:
        grade="A"
    elif marks>=80 and marks<=90:
        grade="B"
    elif marks>=60 and marks<=80:
        grade="C"
    elif marks>=40 and marks<=60:
        grade="D"
    elif marks<=40:
        grade="Fail"
    else:
        grade="Invalid"

    record={"id":"S"+str(i),"Student name":name,"roll no.":roll,"marks1:":marks,"Grade":grade}
    r.append(record)
    i+=1
print("Id","Name","Roll Number","Marks","Grade")

for r1 in r:
    print(r1.values())

