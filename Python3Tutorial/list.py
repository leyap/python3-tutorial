
#same as list1 = list()
list1 = []

list2 = ["one","two","three","one"]
print(list2)
print(list2[1])
print(list2[-2])

print(list2.append('last'))

print(list2.count('one'))

print('+'.join(list2))

# index()
print('index of two is ' + str(list2.index('two')))

# in
print('one' in list2)

print(list('123'))

a_tuple = ('ab','cd','ef')
print(list(a_tuple))

list3 = ['four', list2]
print(list3)
print(list3[1][0])
list3[1][0] = 'five'
print(list3)
print(list3[0:1])

print(list3[::-1])


#extend()
list3.extend(['1','2'])
print(list3)

list3.insert(0, 'insert')
print(list3)

del list3[0]
print(list3)

list3.remove('1')
print(list3)


print(len(list3))

list_copy = list3.copy()

print(list_copy)


tuple1 = ()

tuple2 = 'tuple',
print(tuple2)

tuple3 = 'a','b','c'
print(tuple3)

a,b,c = tuple3
print(b)

a,b = '1','2'
a,b = b,a
print(a+b)



s = set('hello')
s.update("bc","ab","cd")
print(s)

l = list(s)
l.sort()
print(l)
