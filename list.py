list=[1,2,3,4,5,6,2,1]
# dem so lan xuat hien cua 1 trong list
print list.count(1) #print 2

# count element in list
print len(list)#print 8

# append element to list

list.append(9)
print list

# get index of 1 in list
print list.index(1)

#insert at position 2
list.insert(2,"hungnv")
print list
# remove element
list.remove(1)#remove 1 from position 0,1 at the end of list is not deleted
print list

for x in list:
    if x==1:
        list.remove(x)
    print 'hunng'

print list

#get element in list using slice method

print list[0]

print list[2]
print list[3:5]#print element at postion 3,4
