#This python code finds the most common word in a text
# Asking user to enter the source file
fname = input("Enter file:")
if len(fname) < 1 : fname = "clown.txt"
# Opening the source file
fhandle = open(fname)

di = dict()
for line in fhandle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:

        # if w in di:
        #     di[w] = di[w] + 1
        #     #print('**EXISTING**')
        # else:
        #     di[w] = 1
        #     #print('**NEW**')

        #print('**',w,di.get(w,0))

        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w,'new',newcount)

        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1


print(di)


#now we want to find the most common word
k_max = None
v_max = None

for k,v in di.items():
    if v_max is None or v > v_max:
        k_max = k
        v_max = v

#Printing out the most common word
print('the most frequent word is',k_max, v_max)
