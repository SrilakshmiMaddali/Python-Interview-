def extendList(val, list=[]):
    if list == []:
       list =[]
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[14])
list4 = extendList(12,[18,11])
list3 = extendList('a')
list4 = extendList('b')

print( "list1 = %s" % list1)
print ("list2 = %s" % list2)
print("list4 = %s" % list4)
print ("list3 = %s" % list3)


list =[1,2,3,4]

print(list[10:])