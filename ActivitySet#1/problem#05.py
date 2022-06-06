# Functions
def computepay(h, r):
    h=float(h)
    r=float(r)
    if (h<=40.0):
        rate = h*r
    else :
        o=h-40.0
        rate = (o*(1.5*r)+40*r)
    return rate

def my_input():
  hrs = float(input("Enter Hours:"))
  rt = float(input("Rate:"))
  return hrs,rt

def output(rate):
  print("Pay",rate)
  
def main():
  hrs,rt = my_input()
  p=computepay(hrs,rt)
  output(p)

main()