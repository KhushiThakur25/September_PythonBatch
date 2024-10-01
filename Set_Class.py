Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = set()
>>> type(s)
<class 'set'>
>>> st = {2,356,24855,614655,6,1,2,3,True,"om","jay"}
>>> st[2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    st[2]
TypeError: 'set' object is not subscriptable
>>> st1 = {2,345,61,46,12,13,4,4}
>>> st1
{2, 61, 4, 345, 12, 13, 46}
>>> len(st1)
7
>>> a = {1,225,46,425,2,3}
>>> b = {5,161,511,13,46,2,1}
>>> a.union(b)
{1, 2, 3, 225, 161, 5, 425, 13, 46, 511}
a
{1, 2, 3, 225, 425, 46}
a.update(b)
a
{1, 2, 3, 225, 161, 5, 425, 13, 46, 511}
a = {1,225,46,425,2,3}
a.intersection(b)
{1, 2, 46}
a
{1, 2, 3, 225, 425, 46}
a.intersection_update(b)
a
{1, 2, 46}
a = {1,225,46,425,2,3}
a.difference(b)
{425, 225, 3}
a
{1, 2, 3, 225, 425, 46}
a.difference_update(b)
a
{3, 225, 425}
a = {1,225,46,425,2,3}
a.isdisjoint(b)
False
a.issubset(b)
False
a = {1,2,3,4,5}
b = {1,2,3}
a.issuper(b)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.issuper(b)
AttributeError: 'set' object has no attribute 'issuper'. Did you mean: 'issubset'?
a.issuperset(b)
True
a.issubset(b)
False
a.add(56)
a
{1, 2, 3, 4, 5, 56}
a.discard(3)
a
{1, 2, 4, 5, 56}
a.discard(100)
a
{1, 2, 4, 5, 56}
a.remove(100)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.remove(100)
KeyError: 100
b.pop()
1
b
{2, 3}
b.add(1)
b.add(6)
a.symmetric_difference(b)
{3, 4, 5, 6, 56}
a
{1, 2, 4, 5, 56}
a.symmetric_difference_update(b)
a
{3, 4, 5, 6, 56}
st = {2,356,{12,"om"},True}
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    st = {2,356,{12,"om"},True}
TypeError: unhashable type: 'set'
st = {[2,3],5,6}
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    st = {[2,3],5,6}
TypeError: unhashable type: 'list'
a.frozenset(b)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.frozenset(b)
AttributeError: 'set' object has no attribute 'frozenset'
frozenset(a)
frozenset({3, 4, 5, 6, 56})
