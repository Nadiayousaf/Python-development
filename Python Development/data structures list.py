'''list=[1,2,3,2,1]
listy=[4,5,6]
for x in range(min(len(list),len(listy))):
 sum=list[x]+listy[x]
 print(f"Hitting--> list:{list[x]} listy:{listy[x]},sum:{sum}")



List = ['a','b','c','e','e','c' ,'b' ,'a' ,'g'  ]

Done = []
index_tracking = []

for x in List:
    if x not in Done:
        res = List.count(x)
        indexes = [index  for index ,item in enumerate(List) if item == x]
        index_tracking.clear()
        index_tracking.append({'Indexes': indexes, 'Item' : x })
        print(f'Item {x} Occurs {res} times')
        print(index_tracking[0])
        Done.append(x)


def list_analyzer():
  list=['a','b','c','e','e','c','b','a','g']
  unique_element=[]
  for items in set(list):
    counter = list.count(items)
    if counter == 1:
      unique_element.append(items)
      print(f"unique_element:{[items]} counts {counter} times")
list_analyzer()





list=['a','b','c','e','e','c','b','a','g']
def list_analyzer():
  index=[]
  unique=[]
  duplicate=[]
  done=[]
  for  item in range(len(list)):
    value=list[item]
    if value not  in done:
       counter=list.count(value)
       indexes = [index for index, item in enumerate(list) if item== value]
       index.append({'Indexes':indexes,'count': counter})
       print(f"item: {value} index:{indexes} counter:{counter} times")
       done.append(value)
  for item in set(list):
       counter=list.count(item)
       if counter==1:
           unique.append(item)
       elif counter>1:
            duplicate.append(item)
  print(f"unique: {unique}")
  print(f"duplicate: {duplicate}, count : {counter} times")
list_analyzer()'''


'''def find_intersection():
    List1 = [1, 1, 2, 3, 4]
    List2 = [1, 1, 2, 6, 5]
    done=[]
    combined_list=List1+List2
    for item in enumerate(combined_list):
        value=combined_list[item[1]]
        if value not in done and value in List1 and value in List2:
            print([value],end=",")
            done.append(value)
find_intersection()'''''


'''def find_union():
    List1 = [1, 1, 2, 3, 4]
    List2 = [1, 1, 2, 6, 5]
    union=set(List1+List2)
    print(f"union: [{union}]")
    def find_intersection():
        intersection=set(List1)&set(List2)
        print([intersection])
    find_intersection()
find_union()


def find_union():
    List1 = [1, 1, 2, 3, 4]
    List2 = [1, 1, 2, 6, 5]
    union=[]
    [union.append(item) for item in List1+List2 if item not in (union:=union)]
    print(union)
find_union()'''


def data_pairing():
    list=[1,2,   3,4,   5,6]
    for x in range(0,len(list), 2):
         user_input = input(f"index:{x}")
         list[x]=user_input
         key=list[x]
         value=list[x+1]
         print(f"index: {x} key:{key}  value:{value}({x+1})")
data_pairing()



def data_pairing():
    list=[1,2, 3,4, 5,6]
    while True:
        user_input=int(input(f"key:"))
        if user_input==-1:
            break
        if user_input%2!=0:
             value=list[user_input]
             key=list[user_input-1]
             print(f"index:{user_input} key:{key} value:{value}({user_input-1})")
        else:
            print("Invalid input")
            break
data_pairing()



LIST = ["aa", "AA",       "bb", "BB",          "cc", "CC",        "dd", "DD"]
inp = int(input('Enter Key: '))
if inp % 2 == 0:
    key = inp - 2
    val = inp - 1
    print(f'Key: {LIST[key]}   Value: {LIST[val]}')

if inp % 2 != 0:
    key = inp - 1
    val = inp
    print(f'Key: {LIST[key]}   Value: {LIST[val]}')




def data_pairing():
    list=[1,2, 3,4, 5,6]
    while True:
        user_input=int(input(f"Enter key:"))
        if user_input%2==0 :
            print(f"{user_input} is even.")
            value=list[user_input]
            key=list[user_input-1]
            print(f"index:{user_input} key:{key} value:{value}({user_input-1})")
        if user_input%2!=0:
            print(f"{user_input} is odd.")
            value=list[user_input]
            key=list[user_input-1]
            print(f"index:{user_input} key:{key} value:{value}({user_input+1})")
data_pairing()





lst=[10, 20, 30, 40, 50]
for List in lst:
    print(List)

list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

lst=[5,10,15]
Sum=sum(lst)
print(Sum)

List1=[5,10,15]
List2=[1,4,3]
List1.extend(List2)
Sum=sum(List1)
print(Sum)


lst=[10,20,30,40,50]
for item in lst:
    print(item)


lst=[5,10,15,20]
index=lst[0],lst[-1]
print(index)

lst=[5,10,15,20]
length_of_list=len(lst)
lst.append(5)
lst.insert(2,45)
lst.remove(20)
lst.pop(-1)
print(lst)
print(length_of_list)
for item in lst:
    print(item)
lst.reverse()
print(lst)



def List_Questions():
    lst=[1,2,3,4,5,6]
    Sum=0
    for item in lst:
        if item%2==0:
            Sum+=item
    print(Sum)
    lst = [1, 2, 3, 4, 5, 6]
    for item in lst:
        if item % 2 != 0:
            print(item)
List_Questions()

lst=[2,4,5]
for item in lst:
    square=item*2
    print(square)

#check if list is empty or not.
lst=[]
if not lst:
 print("lst is empty")

lst=[1,2,3]
if lst==lst:
    print("list is not empty")

lst=['a','b','c']
index=[]
for item in lst:
    index=len(lst)
    #index.append(item)
    print(f"item : {item} ---> {index}")
#it means dont use the count and enumerate method , we use len also for count .




#concatenate two list
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst2
print(lst3)

lst1=[1,2,3,]
lst2=[4,5,6]
lst1.extend(lst2)
print(lst1)


x=98
tuple=(x,)
print(tuple)

tuple=(1,2,3)
lst=list(tuple)
print(lst)


t=(1,2,3)
a,b,c=(t)
print(a,b,c)


x=10
y=20
x,y=y,x
print(x,y)



# index print the index of the element
lst=[10,20,30,40,50]
print(lst.index(10))

#and dont use index only index element print the actual element.
lst=[10,20,30,40,50]
print(lst[0],lst[4])

#find length of lst
lst=[5,8,12,20,25]
print(len(lst))


#Searching
lst=[2,4,6,8,10]
search_value=6
if search_value in lst:
  print(search_value)

#Reverse lst-----------------------------------------------
#by slicing method
#by loop
#by reverse method
lst=[1,2,3,4,5]
reverse_lst=lst[::-1]
print(reverse_lst)


#Remove duplicates------------------------------------------
#by done method
#using set
#using loop


lst=[1,2,2,3,4,4,5]
unique_lst=[]
for item in lst:
  if item not in unique_lst:
    unique_lst.append(item)
print(unique_lst)

lst=[1,2,2,3,4,4,5]
unique_element=set(lst)
print(unique_element)

lst=[1,2,2,3,4,4,5]
done=[]
duplicates=[]
for item in lst:
  if item not in done:
    done.append(item)
    duplicates.append(item)
print(duplicates)

#maximum and minimum------------------------------
#by max and min method
# by sorted ,sorted(list)[0] → Minimum
# by  loop
#  by reduce 

lst=[12,45,13,89,67,54]
maximum=max(lst)
minimum=min(lst)
print(f"maximum number :{maximum} , minimum number : {minimum}")


lst=[12,45,13,89,67,54]
sorted_lst=sorted(lst)
maximum_value=sorted_lst[-1]
minimum_value=sorted_lst[0]

print(f"Maximum Value: {maximum_value}")
print(f"Minimum_Value : {minimum_value}")


lst=[12,45,13,89,67,54]
maximum_value=lst[0]
minimum_value=lst[0]
for item in lst:
  if item<=minimum_value:
    minimum_value=item
    
  if item>=maximum_value:
    maximum_value=item
print(f"Maximum Value :{maximum_value}")
print(f"Minimum_value: {minimum_value}")


#flatten a list

lst=[[1,2],[3,4],[5,6]]
flat_lst=[]
for sub_lst in lst:
    for item in sub_lst:
        flat_lst.append(item)
print(flat_lst)


lst=[[1,2],[3,4],[5,6]]
flat_lst=[]
for item in lst:
    flat_lst.extend(item)
print(flat_lst)



#Rotate a list
lst=[1,2,3,4,5]
k=2
sorted_lst=lst[-k:]+lst[:-k]
print(sorted_lst)


lst=[1,2,3,4,5]
lst.remove(4)
lst.remove(5)
lst.insert(0,5)
lst.insert(0,4)
print(lst)



#Linear Search List:
lst=[10,20,30,40,50]
for item,value in enumerate (lst):
    if value==30:
        print(f"Element found at index {item}")
        break
else:
        print(f"Element not found in the list.")
   
    
lst=[10,20,30,40,50]
value=30
for i in range(len(lst)):
     if lst[i]==value:   
      print(f"Element appears at {i} index.")   
      break       
else:
    print(f"Element not found in the list.")


#Binary Search Tuple

tuple=(5,10,15,20,25,30,35)
element=20
for i in range(len(tuple)):
    if tuple[i]==element:
        print(f"Element found at {i} index.")
        break
else:
    print(f"Element not found in the tuple.")





List = [64, 34, 25, 12, 22, 11, 90]
Sorted_lst=sorted(List)
print(Sorted_lst)
Tuple = (29, 10, 14, 37, 13)
Sorted_tuple=sorted(Tuple)
print(Sorted_tuple)


#second largest element find------------------
#by index not use the keyword index
#by use the sorted method
#by use sorted method and slicing.



lst=[10,20,3,45,6,89,78]
sorted_list=sorted(lst)
for i in range(len(sorted_list)):
 if i==len(sorted_list)-2:
  print(sorted_list[i])


lst = [10, 20, 3, 45, 6, 89, 78]
sorted_list = sorted(lst, reverse=True)
second_largest = sorted_list[1]
print(second_largest)


lst = [10, 20, 3, 45, 6, 89, 78]
sorted_list = sorted(lst)
for i in range(1, len(sorted_list) + 1):
    slice_part = sorted_list[-i:]  
    if len(slice_part) >= 2:
        second_largest = slice_part[1]
        print("Second largest:", second_largest)
        break


#find duplicates
lst= [1,2,3,2,4,5,1,6]
duplicate_element=[]
for i in lst:
    if lst.count(i)>1 and i not in duplicate_element:
     duplicate_element.append(i)
print(duplicate_element)


lst= [1,2,3,2,4,5,1,6]
duplicate_element=[]
for i in lst:
    if lst.count(i)>1 :
     duplicate_element.append(i)
print(duplicate_element)


#union of lst------------------------------------
#by done method remove duplicates 
#by extend print all items
#by set method remove duplicates
lst1=[1,2,3,4]
lst2=[3,4,5,6]
lst1.extend(lst2)
print(lst1)


lst1=[1,2,3,4]
lst2=[3,4,5,6]
union=list(set(lst1)|set(lst2))
print(union)

lst1=[1,2,3,4]
lst2=[3,4,5,6]
done=[]
for item in lst1+lst2:
   if item not in done:
      done.append(item)
print(done)
   
lst1=[1,2,3,4]
lst2=[3,4,5,6]
unique=[]
for item in set(lst1+lst2):
   unique.append(item)
print(unique)


lst1=[1,2,3,4]
lst2=[3,4,5,6]
intersection=[]
for items in lst1+lst2:
   if item not in intersection and item in lst1 and item in lst2:
      intersection.append(item)
print(intersection)

lst1=[1,2,3,4]
lst2=[3,4,5,6]
intersection=set(lst1)&set(lst2)
print(intersection)

nums=[3,2,2,3]
value=3
nums.pop(0)
nums.pop(-1)
print(nums)


#leetcode Questions

nums=[3,2,2,3]
value=3
nums.pop(0)
nums.pop(-1)
print(nums)


nums=[3,2,2,3]
value=3
for x in nums:
    if x!=value:
     print(x)

lst=[1,1,3]
done=[]
for x in lst:
   if x==0:
      done.append(x)
print(x)
        



lst1=[1,2,3]
lst2=[2,5,6]
done=[]
for x in lst1+lst2:
 if x not in done:
  done.append(x)
print(done)


lst=[1,2,3,1]
Unique=set(lst)
if len(lst)==len(Unique):
    print(True)
else:
    print(False)


lst=[1,2,3]
lst.insert(2,4)
lst.remove(3)
print(lst)


