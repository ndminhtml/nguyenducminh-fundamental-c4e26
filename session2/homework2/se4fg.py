#f
for i in range(3):
    print("*******")

#g
n = int(input("n = "))
m = int(input("m = "))
for i in range(1, m+1):
    print("*", end="")
    for i in range(1, n):
        print("*", end="")
    print(end="\n")
   