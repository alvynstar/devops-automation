
# writing to a file
with open('text.txt', 'w') as file:
    file.write("Kupal ba kayo? \n")
    file.write("Kupal din kase ako eh \n")
	
# reading a file
with open('text.txt', 'r') as file:
	content = file.read()
	print(content)