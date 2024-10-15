file = open('mysticker.png','rb')
data = file.read()
print(data)
file.close()
#write operation on byte file
data = file.read()
file = open('mysticker_3.png','wb')
file.write(data)
file.close()
