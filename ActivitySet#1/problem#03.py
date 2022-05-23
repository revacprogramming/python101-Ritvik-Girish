# Variables, Expressions & Statements
def my_input():
  hrs = float(input("Enter Hours:"))
  rate = float(input("Enter Rate :"))
  return hrs,rate

def calc(hrs,rate):
  amount = hrs * rate
  return amount

def output(amount):
  print("Pay: ",amount)

def main():
  hrs,rate =my_input()
  amount=calc(hrs,rate)
  output(amount)

main()