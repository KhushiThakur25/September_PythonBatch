n = int(input("Enter the value.."))
org = n
rev = 0
while n > 0:
  rem = n%10
  rev = rev * 10 + rem
  n //= 10
n = org
if (rev == n):
  print("Palindrome")
else:
  print("Not a Palindrome")