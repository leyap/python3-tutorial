with open("temp.txt", 'wt') as out_file:
	out_file.write("hello")

with open("temp.txt", 'r') as in_file:
	text = in_file.read()

print(text)
