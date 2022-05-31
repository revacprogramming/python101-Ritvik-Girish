# Tuples
l = None
s = None
def 
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if l is None or l < num:
            l = num
        if s is None or s > num:
            s = num
    except:
        print ("Invalid input")
        continue
print ("Maximum is",l)
print ("Minimum is",s)