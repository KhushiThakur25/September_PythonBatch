#Second Max
li = [23,14,21,52,456,56,1]
maxs = float('-inf')
sec= float('-inf')
for i in li:
    if maxs < i:
        sec = maxs
        maxs = i
    if maxs > i and sec < i:
        sec = i
print(maxs,sec)
#Maximum
'''for i in li:
    if maxs < i:
        sec = maxs
        maxs = i'''
