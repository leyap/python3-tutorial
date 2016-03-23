# if, else, elif
'''
False: 
 False
 None
 0
 0.0
 ''
 []
 ()
 {}
 set()
 others is True
'''

'''
==
!=
<
<=
>
>=
in ...
'''
a = 1
b = 2

if a>b:
	print("a大于b")
else:
	print("a小于b")

# \
print("hello \
world")

if (a > b):
	print("a大于b")
elif (a == b):
	print("a等于b")
else:
	print("a小于b")

really = True
if really:
	print("really")


# run break, will pass else
while True:
	if (1 < 2):
		break
else:
	print('ok')


for i in range(0, 4):
	print(i)
print()

for i in range(0, 10, 2):
	print(i)
print()

for i in range(2, -1, -1):
	print(i)
print()
