#cloning of a list

l1 =[1,2,3,4,5]
l2=l1[:]
print(l2)

##############################
l1 =[1,2,3,4,5]
l2=[]
l2.extend(l1)
print(l2)

#############################
l1 =[1,2,3,4,5]
l2=list(l1)
print(l2)