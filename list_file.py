Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [2,325,6.1,51,True, "Hello",15]
>>> li
[2, 325, 6.1, 51, True, 'Hello', 15]
>>> #heterogenous data
>>> #mutable
>>> li[2]
6.1
>>> li[2] = 100
>>> li
[2, 325, 100, 51, True, 'Hello', 15]
>>> del li[3]
>>> li
[2, 325, 100, True, 'Hello', 15]
>>> li[6] = "ok"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    li[6] = "ok"
IndexError: list assignment index out of range
li1 = [5,21,463,6]
li + li1
[2, 325, 100, True, 'Hello', 15, 5, 21, 463, 6]
li
[2, 325, 100, True, 'Hello', 15]
li = li + li1
li
[2, 325, 100, True, 'Hello', 15, 5, 21, 463, 6]
li.append(600)
li
[2, 325, 100, True, 'Hello', 15, 5, 21, 463, 6, 600]
li.insert(1,800)
li
[2, 800, 325, 100, True, 'Hello', 15, 5, 21, 463, 6, 600]
li.count(2)
1
len(li)
12
li.index(325)
2
li.remove(5)
li
[2, 800, 325, 100, True, 'Hello', 15, 21, 463, 6, 600]
li.pop(5)
'Hello'
li
[2, 800, 325, 100, True, 15, 21, 463, 6, 600]
li.popitem()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    li.popitem()
AttributeError: 'list' object has no attribute 'popitem'
li.pop(-1)
600
li[2:7:1]
[325, 100, True, 15, 21]
n = li
n
[2, 800, 325, 100, True, 15, 21, 463, 6]
n[4] = False
n
[2, 800, 325, 100, False, 15, 21, 463, 6]
li
[2, 800, 325, 100, False, 15, 21, 463, 6]
m = li.copy()
m
[2, 800, 325, 100, False, 15, 21, 463, 6]
m[2] = 900
m
[2, 800, 900, 100, False, 15, 21, 463, 6]
li
[2, 800, 325, 100, False, 15, 21, 463, 6]
li.remove*
SyntaxError: incomplete input
li.remove(False)
li
[2, 800, 325, 100, 15, 21, 463, 6]
sum(li)
1732
max(li)
800
min(li)
2
li.clear()
li
[]
k = list()
k
[]
li = [56,315,615,49,4]
li.append(56,24,1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    li.append(56,24,1)
TypeError: list.append() takes exactly one argument (3 given)
li.append([56,24,1])
li
[56, 315, 615, 49, 4, [56, 24, 1]]
li.extend(23,41,2)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    li.extend(23,41,2)
TypeError: list.extend() takes exactly one argument (3 given)
li.extend([23,41,2])
li
[56, 315, 615, 49, 4, [56, 24, 1], 23, 41, 2]
li[5]
[56, 24, 1]
li[6]
23
li[5][1]
24
li.reverse()
li
[2, 41, 23, [56, 24, 1], 4, 49, 615, 315, 56]
li.sort()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    li.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
li.pop(3)
[56, 24, 1]
li
[2, 23, 41, 4, 49, 615, 315, 56]
li.sort()
li
[2, 4, 23, 41, 49, 56, 315, 615]
li.sort(reversed = True)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    li.sort(reversed = True)
TypeError: 'reversed' is an invalid keyword argument for sort()
li.sort(reverse = True)
li
[615, 315, 56, 49, 41, 23, 4, 2]
nli = [2,3,5]
nli
[2, 3, 5]
nli = [[],[],[]]
nli
[[], [], []]
nli = [[1,2,3],[4,5,6],[7,8,9]]
nli
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
