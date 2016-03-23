name = "hello"

print(name)

length = len(name)
print("lengh = "+str(name))

#hello
#01234  1:3 is el
print(name[1:3])

print(name[-3:])

print(name[-1::-1])

#          0123456789012345678901234
article = "what are you going to do?"
print(article.split())

s = article.split()
s.sort()
print(s)

j = ', '.join(s)
print(j)

# start with some string
print(article.startswith('what'))
# end with some string
print(article.endswith('?'))

print(article.find('are'));

print(article.rfind(' '));

#count
print(article.count(' '))

# is alnum
print(article.isalnum())

print("123abc".isalnum())


setup = 'nice to meet you....'
setup.strip('.')
print(setup)
setup = setup.strip('.')
print(setup)

print(setup.capitalize())

print(setup.title())

print("HellO WorlD".lower())
print("HellO WorlD".upper())

print("HellO WorlD".swapcase())

print("hello world".center(30))
print("hello world".ljust(30))
print("hello world".rjust(30))

print(setup.replace('e', 'h', 1))
print(setup.replace('e', 'h'))






