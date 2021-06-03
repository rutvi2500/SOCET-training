"""
#perform all the tasks using user defined function
user will input no of lines
user will input data
write data in demo.txt
read data from demo.txt
Hello C
Hello C++
Hello Java

linewise reverse write in dummy.txt
Hello Java
Hello C++
Hello C
-----------------------------------------
user will replace the word in dummy.txt
	user will input word to replace->Hello
	user will input word in replacement->Hi
data should be replace in dummy.txt
-----------------------------------------
Hi Java
Hi C++
Hi C
"""
line_num = int(input("Enter number of lines: "))
def fun1(line_num):
    demo_write=open("demo.txt",'w+')
    for i in range(line_num):
        demo_write.write(input("enter data: ")+'\n')
    demo_write.close()

def fun2():
    demo_read=open("demo.txt",'r')
    s=demo_read.readlines()
    s.reverse()
    print(s)
    demo_read.close()
    demo_reverse=open("dummy.txt",'w')
    demo_reverse.writelines(s)
    demo_reverse=open("dummy.txt",'r')
    s1=demo_reverse.read()
    print(s1)
    replaced=s1.replace('hello','hi')
    demo_replace = open("dummy.txt", 'w')
    demo_replace.writelines(replaced)
    demo_replace = open("dummy.txt", 'r')
    print(demo_replace.read())

fun1(line_num)
fun2()