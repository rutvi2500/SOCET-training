"""
#perform all the tasks using user defined function
user will input filename
user will input no of lines
user will input data
write data in file
read data from file
count lines,words,with space chars & without space chars
"""
name=input("Enter file name with .txt:")
line_num = int(input("Enter number of lines: "))
def func1(name):
    fo=open(name,'w+')
    for i in range(line_num):
        fo.write(input("Enter data: ")+'\n')
    fo.close()

def func2():
    word=0
    sch=0
    wch=0
    line=0
    fo=open("1.txt",'r')
    s=fo.read()
    for i in s:
        if i=='\n':
            line+=1
            word+=1
        elif i==" ":
            word+=1
            sch+=1
        else:
            sch+=1
            wch+=1
    print("words=%d"%word,"lines=%d"%line,"char with space=%d"%sch,"char without space=%d"%wch)

func1(name)
func2()