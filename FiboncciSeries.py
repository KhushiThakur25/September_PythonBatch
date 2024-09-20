n = int(input("Enter the value.."))
f = 0
s = 1
i = 1
print(f"{f} {s} ",end = " ")
while  i < n:
  t = f + s
  print(f"{t}",end = " ")
  f = s
  s = t
  i+=1
