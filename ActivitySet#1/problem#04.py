# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if(h<=40.0):
	amt=r*h
else :
    o=h-40
    amt=o*(1.5*r)+(40*r)
print("PAY :",amt)