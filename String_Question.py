'''#Reverse of string...
n = input("Enter the string..")
rev = n[::-1]
print(rev)

#Reverse of words..
n = input("Enter the string..")
rev = n.split()
rev = rev[::-1]
rev = " ".join(rev)
print(rev)

#Even length print
n = input("Enter the string..")
li = n.split()
for i in li:
    if len(i)%2 == 0:
        print(i)'''

#Replace . with , and , with .
n = input("Enter the string..")
n = n.replace('.','*')
n = n.replace(',','.')
n = n.replace('*',',')
print(n)









    
