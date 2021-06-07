"""
Class StudentInfo
    student_rollno
    student_name

Class StudentMarks
    student_rollno
    student_marks_one
    student_marks_two
    student_marks_three

Class Main
    Constructor
    user will input no of students
    user will input data for StudentInfo-Constructor
    user will input data for StudentMarks-Constructor
    calculate the average-Function
    find the grade
    import the grade calculation function from file task (LEC 9)
"""

# Parent Class
class StudentInfo:
	def __init__(self, roll, name):
		self.roll = roll
		self.name = name

	def __repr__(self):
		return f"Student's roll NUMBER is {self.roll} and name is {self.name}"

# Child Class
class StudentMarks(StudentInfo):
	def __init__(self, name, roll, m1, m2, m3):
		StudentInfo.__init__(self, name, roll)
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		self.avg = round((self.m1 + self.m2 + self.m3) / 3)

	def grade(self):
		if self.avg >= 80 and self.avg <= 100:
			fa = open("A_grade.txt", "a+")
			fa.write(
				f"\nMarks of student with roll : {self.roll} and name : {self.name} has Marks\nsubject 1: {self.m1}\nsubject 2: {self.m2}\nsubject 3: {self.m3} and\navg is {self.avg}")
			fa.close
		elif self.avg >= 60 and self.avg <= 79:
			fa = open("B_grade.txt", "a+")
			fa.write(
				f"\nMarks of student with roll : {self.roll} and name : {self.name} has Marks\nsubject 1: {self.m1}\nsubject 2: {self.m2}\nsubject 3: {self.m3} and\navg is {self.avg}")
			fa.close
		elif self.avg >= 40 and self.avg <= 59:
			fa = open("C_grade.txt", "a+")
			fa.write(
				f"\nMarks of student with roll : {self.roll} and name : {self.name} has Marks\nsubject 1: {self.m1}\nsubject 2: {self.m2}\nsubject 3: {self.m3} and\navg is {self.avg}")
			fa.close
		else:
			fa = open("F_grade.txt", "a+")
			fa.write(
				f"\nMarks of student with roll : {self.roll} and name : {self.name} has Marks\nsubject 1: {self.m1}\nsubject 2: {self.m2}\nsubject 3: {self.m3} and\navg is {self.avg}")
			fa.close

	def __repr__(self):
		return f"\nMarks of student with rollo : {self.roll} and name : {self.name} has Marks\nsubject 1: {self.m1}\nsubject 2: {self.m2}\nsubject 3: {self.m3} and\navg is {self.avg}"

# This is the main class that performs entry function and calls for the parent methods using instances.
class main(StudentMarks, StudentInfo):
	def __init__(self, no):  # Child Class
		self.no = no
		i = 0
		# mega=[]
		while i < no:
			roll = int(input("Enter Roll Number: "))
			name = input("Enter Name: ")
			m1 = int(input("Marks for subject1: "))
			m2 = int(input("Marks for subject2: "))
			m3 = int(input("Marks for subject3: "))
			S = StudentMarks(roll, name, m1, m2, m3)
			b = S.avg()
			a = S.grade()
			i += 1

# Calling the main method on user input.
no = int(input("Enter number of students: "))
main(no)