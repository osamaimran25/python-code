filename="programming_Poll.txt"

polls=[]



while True:
    poll=input("Enter your favrite programming language you like ")
    polls.append(poll)

    more_review=input("Do you like more polls (Y/N)")
    if more_review=='N':
        break

with open(filename,'a') as f:
    for poll in polls:
        f.write(poll+"\n")



with open(filename) as rf:
    lines=rf.readlines()
    for line in lines:
        print(line.rstrip())