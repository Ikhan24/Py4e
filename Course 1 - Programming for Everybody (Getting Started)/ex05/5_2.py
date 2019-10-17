largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
         break
    try:
        ifval = int(num)
    except:
        print('Invalid input')
        continue

    for i in [ifval] :
        if smallest is None :
            smallest = i
        elif i < smallest :
            smallest =  i

    for i in [ifval] :
        if largest is None :
            largest = i
        elif i > largest :
            largest =  i


print("Maximum is", largest)
print("Minimum is", smallest)
