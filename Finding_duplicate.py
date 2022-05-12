def check_duplicates(list1):
    if len(list1) == len(set(list1)):
        return False
    else:
        return True
def para(size,list1):
    for i in range(0,size):    
        for j in range(i+1,size):    
            if(list1[i] == list1[j]):    
                print(f"The duplicate element in the list is {list1[j]}")
            else:
                return 1
    return 0

list1 =[]
size=int(input("Enter number of elements :"))
print("Enter the list of elements:")
for i in range(0,size):
    m=int(input())
    list1.append(m)
list1.sort()
print(list1)
result = check_duplicates(list1)
if result:
    print('Yes,list contains duplicates')
else:
    print('No duplicate elements found in list')   
para(size,list1)

