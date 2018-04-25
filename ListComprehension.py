list=[x for x in range(0,10,1)]

dict={x:x for x in range(0,10,1)}

sets={x for x in range(0,10,1)}

print dict

print list

print  sets

# with condition

list=[x for x in range(0,10,1) if x>5]

print list

# If you don’t need the value from the list, it’s conventional to use an underscore as the
# variable

list=[0 for _ in range(0,10,1)]

print list

# multi for

list=[[x,y] for x in range(0,10) for y in range(0,10)]

print list

print list[0][0]

print list[0][1]


# another way

list=[[x,y] for x in range(0,10) for y in range(x,10)]
print list

# or you can using function inside

def is_event(x):
    return  x%2==0

list=[x for x in range(0,10) if is_event(x)]

print list


# lazy list

def lazy_list(x):
    i=0
    while(i<x):
        print 'i={0}'.format(i)
        yield i
        i+=1

print 'lazy'
# list=[x for x in lazy_list(1000000)]

list=[x for x in range(0,1000000)]


print list




print list