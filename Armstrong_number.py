n = int(input("Enter the value.."))
count = 0
org = n
result = 0
while n > 0:
    count += 1
    n //= 10
n = org
#print(count,n)
while org > 0:
    rem = org %10
    result += rem**count
    org //= 10

if n == result:
    print("Number is Armstrong..")
else:
    print("Number is not an Armstrong..")
