'''try - logic
except - error
else - code
raise - user-defined-exception'''

try:
    num1 = int(input("Enter the value 1"))
    num2 = int(input("Enter the value 2"))

    add = num1 + num2
    sub = num1 - num2
    mul = num1* num2
    div = num1/num2
except ArithmeticError as msg:
    print(msg)
except Exception as msg:
    print("We can't divide any integer by zero..")

else:
    print(add)
    print(sub)
    print(mul)
    print(div)
finally:
    print("I'm always excute..")
    
