filename="guest.txt"



print("Write 'quit' to finish")

while True:
    name=input("Enter the name of guest: ")
    if name=='quit':
        break
    else:
        with open(filename,'a') as file:
            file.write(name+"\n")
            print("Hello "+name+" You have been added to our guest book Thanks :)")
with open(filename) as f:
    line=f.read()

print(line)