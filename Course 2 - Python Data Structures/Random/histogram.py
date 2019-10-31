counts = dict()
names =  ['tanjiha', 'antu', 'tanjiha', 'shatil' , 'sara']
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)
