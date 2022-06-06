# Use the file name mbox-short.txt as the file name
def myinput():
    fname = input("Enter file name")
    return fname

def file(fname):
  f=open(fname)
  count = 0
  sum=0
  for line in f:
      if line.startswith('X-DSPAM-Confidence'):
          count = count + 1
          x=float(line[20::1])
          sum=sum+x
  print('There were', count, 'subject lines in', "dataset/mbox-short.tx")
  avg=sum/(count)
  return avg
           
def output(avg):            
  print("Average spam confidence: ",avg)
  

def main():
    fn = myinput()
    av = file(fn)
    output(av)
    
main()