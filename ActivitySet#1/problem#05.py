# Functions
def computepay(h, r):
    h=float(h)
    r=float(r)
    if (h<=40.0):
        return h*r
    else :
        o=h-40.0
        return (o*(1.5*r)+40*r)

hrs = input("Enter Hours:")
rt = input("Rate:")
hr = float(hrs)
rat = float(rt)
p=computepay(hrs,rt)
print("Pay", p)

