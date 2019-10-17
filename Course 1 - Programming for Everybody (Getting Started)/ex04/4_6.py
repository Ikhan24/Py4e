def computepay(h,r):
    if h <= 40:
        return h*r
    else :
        return 40*r + (h-40)*1.5*r

hrs = input("Enter Hours:")
h1 = float(hrs)
rate = input("Enter rate :")
r1 = float(rate)

p = computepay(h1,r1)
print(p)
