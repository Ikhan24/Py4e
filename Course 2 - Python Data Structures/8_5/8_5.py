# Opening the file
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0

for line in fh:
    line.rstrip()
    words = line.split()
    # guardian in compund statement
    if len(words) < 3 or words[0] != 'From':
        continue
    count = count + 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
