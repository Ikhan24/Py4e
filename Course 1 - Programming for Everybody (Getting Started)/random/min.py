smallest = None
print("Before")
for i in [9,41,12,3,74,15] :
    if smallest is None :
        smallest = i
    elif i < smallest :
        smallest =  i
    print(smallest,i)
print("After", smallest)
