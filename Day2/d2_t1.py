"""
TASK1:
user input values in a variable like
    a=1,a,2,b,3,4,55,asit,nimesh

str_list=[]
int_list=[]

store int values inside int_list as integer
    -perform min and max function

store string values inside str_list as string
    -perform reverse function
"""
n=input("enter values: ")
str_list=[]
int_list=[]
print(n)
ls=n.split(",")
print(ls)
for i in ls:
    if i.isdigit():
        int_list.append(int(i))
    else:
        str_list.append(i)
print("Integer list: ",int_list)
print("String List: ",str_list)
print("Reversed list= ",str_list.reverse())
print("minimum value= ",min(int_list))
print("Maximum value= ",max(int_list))