for i in range(5):
    for j in range(5-1-i):
        print("  ",end = "")
    for k in range(5-1-i,5):
        print("* ",end = "")
    print()

for i in range(5):
    for j in range(i):
        print("  ",end = "")
    for k in range(i,5):
        print("* ",end = "")
    print()
