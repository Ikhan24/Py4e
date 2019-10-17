rawstr = input("Enter a number")
try:
    ifval = int(rawstr)
except:
    ifval = -1

if ifval > 0 :
    print("Great job you entered a number")
else :
    print("Not a number you smartass")
