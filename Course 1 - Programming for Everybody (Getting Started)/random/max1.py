#None is another type of Variable that has a Null Value
largest = None
print("Before")
for i in [9,41,12,3,74,15] :
    if largest is None :
        largest = i
    elif i > largest :
        largest =  i
    print(largest,i)
print("After", largest)
