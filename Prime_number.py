n = int(input("Enter the value.."))
flag = True
for i in range(2,n):
    if n % i == 0:
        print("Number is not a prime..")
        flag = False
        break
else:
    print("Number is a prime..")
