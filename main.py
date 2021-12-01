import csv


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
  print(out)

findNum()
