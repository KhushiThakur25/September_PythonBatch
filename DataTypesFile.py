Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 56
>>> m = 2.3
>>> st = "Rahul"
>>> li = ["ram",5.2,63,[2,3]]
>>> li
['ram', 5.2, 63, [2, 3]]
>>> tu = (2.3,"om",'raja',56)
>>> s = {5,2,35,3,2,3,6}
>>> s
{2, 35, 3, 5, 6}
>>> dic = {"name":"Jay","RollNo":32}
>>> dic
{'name': 'Jay', 'RollNo': 32}
>>> m = True
>>> m
True
>>> n + 1
57
>>> n
56
>>> n = n + 1
>>> n
57
>>> n = 100
n
100
st[0]
'R'
st[2]
'h'
st[2] = 'm'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    st[2] = 'm'
TypeError: 'str' object does not support item assignment
del st[2]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    del st[2]
TypeError: 'str' object doesn't support item deletion
del n
n
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    n
NameError: name 'n' is not defined
li[2]
63
li[2] = 100
li
['ram', 5.2, 100, [2, 3]]
tu[3]
56
tu[3] = 92
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tu[3] = 92
TypeError: 'tuple' object does not support item assignment
import sys
sys.getsizeof(li)
88
sys.getsizeof([])
56
sys.getsizeof("")
41
sys.getsizeof(0)
28
sys.geysizeof(0.0)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sys.geysizeof(0.0)
AttributeError: module 'sys' has no attribute 'geysizeof'. Did you mean: 'getsizeof'?
sys.getsizeof(0.0)
24
sys.getsizeof(())
40
sys.getsizeof(set())
216
sys.getsizeof({})
64
d = {}
type(d)
<class 'dict'>
s = set()
type(s)
<class 'set'>
#How can we take input
val = input()

val = input("Enter the value")
Enter the value56
val1 = input("Enter the value 1")
Enter the value 132
val + val1
'5632'
type(val)
<class 'str'>
val = int(input("Enter the value"))
Enter the value56
type(val)
<class 'int'>
val_1 = int(input("Enter the value"))
Enter the value32
val + val_1
88
f_name = input("Enter your first name..")
Enter your first name..Muskan
l_name = input("Enter your last name..")
Enter your last name..malik
full_name = f_name + l_name
print(full_name)
Muskanmalik
full_name = f_name + " " +l_name
print(full_name)
Muskan malik
val_1 = int(input("Enter the value 1.."))
Enter the value 1..32
val_2 = int(input("Enter the value 2.."))
Enter the value 2..65
val_3 = int(input("Enter the value 3.."))
Enter the value 3..84
product =  val_1 * val_2 * val_3
print(product)
174720
