filename='python.txt'

print("Reading the entire file")
with open(filename) as python_obj:
    lines=python_obj.read()
    print(lines)

with open(filename) as file:
    for line in file:
        print(line.rstrip())


with open(filename) as newFile:

    string_list=newFile.readlines()


for line in string_list:
    print(line.rstrip())