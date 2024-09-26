Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = "Khushi"
type(n)
<class 'str'>
n = 'om'
type(n)
<class 'str'>
n = "This is the python programming.."
n[7]
' '
n[8]
't'
n[8]='l'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    n[8]='l'
TypeError: 'str' object does not support item assignment
n[-5]
'i'
n[2:7:1]
'is is'
n[12:18]
'python'
n[12:20:2]
'pto '
n[::-1]
'..gnimmargorp nohtyp eht si sihT'
n.lower()
'this is the python programming..'
n.upper()
'THIS IS THE PYTHON PROGRAMMING..'
n.title()
'This Is The Python Programming..'
n.swapcase
<built-in method swapcase of str object at 0x00000214D37FC670>
n.swapcase()
'tHIS IS THE PYTHON PROGRAMMING..'
n.capitalize()
'This is the python programming..'
n.index('y')
13
n.index('z')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    n.index('z')
ValueError: substring not found
n.find('z')
-1
n.find('y')
13
n.count('y')
1
n.count('m')
2
n.count('n')
2
n.count('h')
3
n.isupper()
False
n.isalpha()
False
n.isnumeric()
False
n.islower()
False
n.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    n.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
n.istitle()
False
"Hello" == "hello"
False
casefold("Hello") == casefold("hello")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    casefold("Hello") == casefold("hello")
NameError: name 'casefold' is not defined
"Hello".casefold() == "hello".casefold()
True
n.split()
['This', 'is', 'the', 'python', 'programming..']
m = n.split()
m
['This', 'is', 'the', 'python', 'programming..']
arr = m[::-1]
arr
['programming..', 'python', 'the', 'is', 'This']
" ".join(arr)
'programming.. python the is This'
l = "  djifiodjnf iodfnhvhfdu     "
l.strip()
'djifiodjnf iodfnhvhfdu'
>>> l.rstrip()
'  djifiodjnf iodfnhvhfdu'
>>> l.lstrip()
'djifiodjnf iodfnhvhfdu     '
>>> l = "+++kdnhcuifdfhvn ionhsfjd+++"
>>> l.strip('+')
'kdnhcuifdfhvn ionhsfjd'
>>> n.partition()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    n.partition()
TypeError: str.partition() takes exactly one argument (0 given)
>>> n.partion('py')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    n.partion('py')
AttributeError: 'str' object has no attribute 'partion'. Did you mean: 'partition'?
>>> n.partition('py')
('This is the ', 'py', 'thon programming..')
