'''
TASK2:
Create an empty student dictionary, user will input number of students and for every student, the user will input
roll number, name, marks. Store the data in the student dictionary and display the student dictionary.
'''
x=int(input("Enter number of keys: "))
y=int(input("Enter number of students: "))
d={}
for i in range(x):
    key=input("Enter the key: ")
    ls=[]
    for i in range(y):
        value=input("Enter the value for the key: ")
        ls.append(value)
        d.update({key:ls})
print("Updated dictionary: ")
print(d)