print("This is superuser gateway")
username = input("Enter username :  ")
if username != "c4e":
    print("You're not superuser")
else:
    password = input("Enter password : ")
    if password != "codethechange":
        print("Invalid password")
    else:
        print("Access granted, welcome")

