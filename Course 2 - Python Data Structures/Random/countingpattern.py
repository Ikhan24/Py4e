counts = dict()
print('Enter a line of text')
line = input('')

words = line.split()

print('Words:', words)

print('Counting....')
for word in words:
    counts[word] = counts.get(word,0) + 1

print('Counts', counts)

#For retrieving list of keys and values
#print(list(x)) or print(x.keys()) / print(x.values())
