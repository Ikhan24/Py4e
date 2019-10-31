data = 'From intesarul.khan@mail.mcgill.ca Sat Jan 5 09:14:16 2019'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)
