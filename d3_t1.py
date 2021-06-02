"""
user will decide no. of lists
2
user wil input no. of elements for each list
ls1=>5
ls2=>7
user will input element for each list
ls1=[1,11,43,56,43]
ls2=[1,32,3,4,5,6,7]
calculate(ls1)=>print the list
calculate(ls1,ls2)=>concate both the lists=>print maximum-minimum element
    56,1
calculate(ls1,ls2,ls3)=>concate all the lists=>print internal addition of all elements
calculate(n list)=>concate all the lists
lambda function
    print the square of every element and store in list
    find the odd number and store in list
"""
main_list = int(input("Enter number of list you want to create: "))
i, j, k = 0, 0, 0
super_list = []

while i < main_list:
    new_list = list()
    super_list.append(new_list)
    while j < len(super_list):
        no_elements = int(input("Enter No of elements: "))
        while k < no_elements:
            elements = int(input("Enter your elements: "))
            super_list[j].append(elements)
            k += 1
        k = 0
        j += 1
    i += 1
print(super_list)
print("Total number of lists: ",len(super_list))
list1 = []
if len(super_list) == 1:
    print(super_list)
elif len(super_list) == 2:
    i=0
    while i<len(super_list):
        new = super_list[i] + super_list[i + 1]
        list1.extend(new)
        break
    print("Maximum is ",max(super_list),"Minimum is ",min(super_list))

elif len(super_list)==3:
    i = 0
    n1=0
    while i < len(super_list):
        new = super_list[i] + super_list[i + 1] + super_list[i + 2]
        list1.extend(new)
        break
    for n in new:
        n1+=n
    print("Sum is ",n1)

else:
    def flatten(list_of_lists):
        if len(list_of_lists) == 0:
            return list_of_lists
        if isinstance(list_of_lists[0], list):
            return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
        return list_of_lists[:1] + flatten(list_of_lists[1:])
    ls2 = (flatten(super_list))
    print(ls2)

    odd_list = list(filter(lambda x: (x % 2 != 0), ls2))
    print("Odd List: ",odd_list)
    even_list = list(filter(lambda x: (x % 2 == 0), ls2))
    print("Even List: ",even_list)
    square_list = list(map(lambda x: x * x, ls2))
    print("Square List: ",square_list)




