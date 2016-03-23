# dictionary key can be boolean int float tuple string ...
# key must be only, different each other

#create dictionary
dict1 = {}

# dict() can convert two-item list to dictionary
#list1 = [['name','lisper'],['age','18']]
list1 = [['name','lisper'],['age',18]]

dict2 = dict(list1)
print(dict2)

#add data
dict2['pythoner'] = 'yes'
print(dict2)

#change data
dict2['pythoner'] = 'no'
print(dict2)

#update()合并字典

#del 删除元素

#clear()删除所有元素

#in 判断是否存在

#[key]获取元素

#keys()获取所有键
keys = dict2.keys()
print(keys)

#keys()获取所有值
values = dict2.values()
print(values)

#items获取所有键值对,tuple
items = dict2.items()
print(items)
a,b,c = items
print(a)

#convet to list
print(list(items)[0])

# = 复制,copy()复制
dict3 = dict2
dict4 = dict2.copy()


