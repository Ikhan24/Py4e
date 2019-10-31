numlist = list()
while True :
    inp = input ('Enter a Number :')
    if inp == 'done' :
        break
    try:
        value = float(inp)
    except:
        print('Invalid Input') 
        continue

    numlist.append(value)

avg = sum(numlist) / len(numlist)
print('Average is' , avg)
