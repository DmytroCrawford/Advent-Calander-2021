import csv

#day 1 Pt 1

accum=[]
with open('data.csv') as f:
  reader=csv.reader(f)
  for el in reader:
    for t in el:
      accum.append(int(t))

  


def findNum():
  out=0
  t = range(len(accum))
  for ran in t:
    if accum[ran] > accum[ran-1]:
      out+=1
  

findNum()


#day 2 Pt 1

acum=[]
with open('MoreData.csv') as f:
  reader=csv.reader(f)
  for el in reader:
    for t in el:
      acum.append(t)



def main():
  horiz=0
  vert=0
  for i in acum:
    if 'up' in i:
      for t in i:
        if t.isdigit():
          vert-=int(t)
    elif 'forward' in i:
      for t in i:
        if t.isdigit():
          horiz+=int(t)
    elif 'down' in i:
      for t in i:
        if t.isdigit():
          vert+=int(t)
    else:
      None
  ans=horiz*vert


main()

#Day 3
# Build a function which iderates through each position
# And finds the occurences in each place
# Then build a function which gens a new binary number
# and another function which inverets that binary key
# and one last funciton to multiiply 

def day3():
  def newGammRate(x):
    arra = {}
    for line in x:
      rangefun = range(len(line))
      for ran in rangefun:
        if line[ran]=='1':
          if str(ran) in arra:
            arra[str(ran)]+=1
          else:
            arra[str(ran)]=1
    def buildBinary():
      gamma=''
      epsilon=''
      for ran in rangefun:
        if arra[str(ran)]>500:
          gamma+='1'
          epsilon+='0'
        else:
          gamma+='0'
          epsilon+='1'
      print(int(gamma,2)*int(epsilon,2))
    buildBinary()
  acu=[]
  with open('JustEvenMoreData.csv') as f:
    reader=csv.reader(f)
    for el in reader:
      for t in el:
        acu.append(t)
  newGammRate(acu)
  
day3()