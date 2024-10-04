'''dep1 = {123:50,456:60,147:39,632:81}
dep2 = {333:45,621:75,458:49}
dep1.update(dep2)
print(dep1)
dep2.clear()
print(dep2)
dep1.pop(621)
print(dep1)
dep1.popitem()
print(dep1)
del dep1[122]
print(dep1)'''

'''key = ['1','2','3','4','5']
val = ['1','4','9','16','25']
dict = dict(zip(key,val))
print(dict)'''

'''st1 = {1:"ram","roll":23,"class":5}
st2 = {2:"amit","roll":2,"class":3}
st2.update(st1)
print(st2)

l1 = [5,6,82,3,4,6,97,1]#ascending sort
l2 = [64,52,12,02,34,87,2,54]#descending sort
# convert into dictionary...'''
'''dic = {
    'one':'1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    'zero' : '0'}

st = input("Enter the words..")
print(st)
res = ' '.join(dic[el] for el in st.split())
print(res)'''
key = [1,2,3,4,5]
val = [1,4,9,16,25]
dict = dict(zip(key,val))
print(dict)
x = []
for i in dict.values():
    x.append(i)
print(sum(x))









