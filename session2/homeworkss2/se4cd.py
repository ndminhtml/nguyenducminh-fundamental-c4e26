
#in 9 * va x
print("x*x*x*x*x")

#nhap n la tong so 8* va x
n = int(input("Enter a number :  "))
if n%2:
    for i in range(1, n, 2):
        print("x", end="*")
    print("x")
else:    
    for i in range(1, n, 2):
        print("x", end="*")

    