Answer = {
    "1" : 35,
    "2" : 36,
    "3" : 40,
    "4" : 44,
}

print("Answer the following algebra question : ")
print("If x = 8, then what  is the value  of 4(x + 3)  ?")

for k,v in Answer.items():
    print(k,"." , v)
n = int(input("Your Choice : "))
if n == 4:
    print("Bingo")
else:
    print(" :( ")
