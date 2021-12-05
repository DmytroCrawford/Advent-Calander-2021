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
  print(ans)

main()