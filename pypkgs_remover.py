import os
print("######This python script was created for removing offline outdated python packages######")
files = os.listdir(os.getcwd())
files.sort()
flag=0
names=[]
dupe=[]
dupefinal=[]
for x in files:
    div=x.find('-')
    if div > -1:
        names.append(x[0:div+1])
for x in names:
    if x not in dupe and names.count(x) > 1:
        dupe.append(x)

for x in dupe:
    for y in files:
        if x in y:
            dupefinal.append(y)

    for z in range(len(dupefinal) - 1):
        print("PERMANENTLY REMOVING outdated file ",
              dupefinal[z],"\nLatest: ",dupefinal[len(dupefinal)-1],
              "!!\n1 to continue|any other key to keep:")
        if(input() is '1'):
            os.remove(dupefinal[z])
            flag=1
        else:
            print(dupefinal[z]," not removed!")
            break

    dupefinal=[]
if flag is 1:
    print("Outdated Versions Removed!")
else:
    print("No Outdated Versions Found!")
input("press 'Enter' to exit")
