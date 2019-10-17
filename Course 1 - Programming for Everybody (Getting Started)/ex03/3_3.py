score = input("Enter Score: ")
try:
    ifval = float(score)
except:
    ifval = -1

if ifval > 0 :
    sc = float(score)
    if sc > 1.0 :
        print("Invalid Entry")
    elif sc >= 0.9 :
        print("A")
    elif sc >= 0.8 :
        print("B")
    elif sc >= 0.7 :
        print("C")
    elif sc >= 0.6 :
        print("D")
    elif sc < 0.6 :
        print("F")
else :
    print("Not a Score you smartass")
