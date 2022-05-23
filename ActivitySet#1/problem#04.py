# Conditional Execution
def my_input():
  hrs = float(input("Enter Hours:"))
  rate = float(input("Enter Rate:"))
  return hrs,rate

def calc(h,r):
  if(h<=40.0):
	  amt=r*h
  else :
    o=h-40
    amt=o*(1.5*r)+(40*r)
  return amt

def output(amt):
  print("PAY :",amt)

def main():
  hrs,rate=my_input()
  a=calc(hrs,rate)
  output(a)

main()