# Variables, Expressions & Statements
def Input(hour , rate) :
  hour = input("Enter Hours:")
  rate = input("Enter Rate :")
  return hour,rate

def Calc(h,r):
  amt = h * r
  return amt

def Output(amt):
  amount = float(hrs) * float(rate)
  print("Pay: ",amount)
  