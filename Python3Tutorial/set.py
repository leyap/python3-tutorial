#set1 = set()
set1 = set('hello')
set1.update("ab","cd")
print(set1)

print('a' in set1)

print('交集:&(与,且)')
set1 = set('abc')
set2 = set('bcd')
set3 = set1 & set2
print(set3)

print('并集:|(或)')
set1 = set('abc')
set2 = set('bcd')
set3 = set1 | set2
print(set3)

print('差集:-')
set1 = set('abc')
set2 = set('bcd')
set3 = set1 - set2
print(set3)

print('异或:^')
set1 = set('abc')
set2 = set('bcd')
set3 = set1 ^ set2
print(set3)

print('判断子集:<= (issubset())')
set1 = set('abc')
set2 = set('ab')
print(set1.issubset(set2))
print(set2.issubset(set1))

print(set2 <= set1)
print(set1 <= set1)

print('判断真子集:<')
set1 = set('abc')
set2 = set('ab')
print(set2 < set1)

print('判断超集:> (issuperset())')
set1 = set('abc')
set2 = set('ab')
print(set1 > set2)

