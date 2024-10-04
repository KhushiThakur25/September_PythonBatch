#function arguments...
#1. positional arguments..
def add(a,b):
    print(a+b)
add(3,4)
#2. keyword arguments..
def add(b,a):
    print(a+b)
add(a = 3,b = 4)
#3. defaults arguments..
def add(a = 5,b = 6):
    print(a+b)
add(2,3)
#4. arbitrary arguments..
def add(**a):
    print(a)
add(a = 3,b=  4,c =5 ,d =6 )
'''def add(a,b):
    print("Sum is:",a+b)
def sub(a,b):
    print("Sub is:",a-b)
def mul(a,b):
    print("mul is:",a*b)
def div(a,b):
    print("div is:",a/b)

a  = int(input("Enter the val 1"))
b = int(input("Enter the val 2"))
while True:
    
    print("""
    press 1 for addition..
    press 2 for subtraction..
    press 3 for multiplication..
    press 4 for division..""")
    ch = input("Enter your choice..")
    if ch == '1':
        add(a,b)
    elif ch == '2':
        sub(a,b)
    elif ch == '3':
        mul(a,b)
    elif ch == '4':
        div(a,b)
    else:
        print("Invalid choice..")
        break;
'''
