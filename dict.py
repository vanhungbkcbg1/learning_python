dict={
    "a":"1",
    "b":"2",
    "c":"3"
}

print dict

# print all keys in dic

print dict.keys()

# print all values in dict

print dict.values()

# loop in key,value in dic

for key,value in dict.items():
    print "{0}={1}".format(key,value)

# check key exists in dict

if("a" in dict):
    print 'dict has {0}'.format("a")
else:
    print 'a not in dict'

#     get default of element in dict,not throw exception

print dict.get('d','default value')

print dict['a']



