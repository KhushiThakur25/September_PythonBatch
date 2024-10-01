Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t = tuple()
type(t)
<class 'tuple'>
m = 2,36,56,5,12,3
type(m)
<class 'tuple'>
m
(2, 36, 56, 5, 12, 3)
m = 2
type(m)
<class 'int'>
m = 2,3
type(m)
<class 'tuple'>
m = 2,
type(m)
<class 'tuple'>
t = (2,356,615,6516,236)
type(t)
<class 'tuple'>
t
(2, 356, 615, 6516, 236)
t[1]
356
t[1] = 100
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[1] = 100
TypeError: 'tuple' object does not support item assignment
>>> temp = list(t)
>>> type(temp)
<class 'list'>
>>> temp
[2, 356, 615, 6516, 236]
>>> temp[1] = 100
>>> temp
[2, 100, 615, 6516, 236]
>>> t = tuple(temp)
>>> t
(2, 100, 615, 6516, 236)
>>> len(t)
5
>>> t.count(100)
1
>>> m = t
>>> m
(2, 100, 615, 6516, 236)
