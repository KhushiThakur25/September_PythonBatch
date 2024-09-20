n = int(input("Enter the value"))
fact = 1
# while n > 1:
#   fact *= n
#   n -= 1
# print(fact)

i = 1
while i <= n:
  fact *= i
  i += 1
print(fact)
