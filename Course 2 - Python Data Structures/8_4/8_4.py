# Opening the file
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

#Defining the list
lst = list()

for line in fh:
    line.rstrip()
    ls = line.split()
    for word in ls:
        if word not in lst :
            lst.append(word)

lst.sort()
print(lst)
