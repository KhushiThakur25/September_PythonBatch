file = open('data.txt','r')
#data = file.read()
#data = file.read(20)
#data = file.readline()
#data = file.readlines()
# file.seek(30)
# data = file.read()
# print(data)
# file.close()

file.seek(28)
data = file.read()
print(data)