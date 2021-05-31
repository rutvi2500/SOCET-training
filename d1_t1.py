'''
TASK1:
Differentiate the string and integer value from main list and sub list (layer1) with given output.
'''
ls=[1,2,3,['a','b','c'],4,5,6,["d","e","f"],7,8,9,'h',[9,10,'i','j'],11,'aansh']
def flatten(list_of_lists):
    if len(list_of_lists)==0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0])+flatten(list_of_lists[1:])
    return list_of_lists[:1]+flatten(list_of_lists[1:])
ls1=(flatten(ls))
print(ls1)
for i in ls1:
    if type(i)==str:
        print("   ",i)
    else:
        print(i)







