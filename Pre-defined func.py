def km_to_m(km):
    return km*1000

def c_to_f(c):
    return 9/2*c + 32

km = [2,356,496,46,34,5]
c = [10,56,23,47,82]
'''m = []
f = []
for i in km:
    m.append(km_to_m(i))
print(m)

for i in c:
    f.append(c_to_f(i))
print(f)'''
print(list(map(km_to_m,km)))
print(list(map(c_to_f,c)))

#filter
def even_odd(i):
    return i%2 == 0


li = [56,12,2,3,31,45,7,1,22]
e = []
o = []
'''for i in li:
    if i%2 == 0:
        e.append(i)
    else:
        o.append(i)'''
for i in li:
    if even_odd(i):
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)
print(list(filter(even_odd,li)))
s = [i for i in range(50)]
print(s)

di = {i:i**2 for i in range(5)}
print(di)

for i in enumerate(km,101):
    print(i)
name = ["om","jay","ram","yash"]
marks = [32,56,74,95]
print(dict(zip(name,marks)))

