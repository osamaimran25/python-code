# in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
# you to read and write to the file ('r+'). If you omit the mode argument,


nameOfGuest=input("what is the name of guest")
filename="guest.txt"
with open(filename,'w') as Wf:

    Wf.write(nameOfGuest)



with open(filename)as f:
    f=f.readlines()

for line in f:
    print(line.rstrip())