Answer1 = {
    "1" : 35,
    "2" : 36,
    "3" : 40,
    "4" : 44,
}

Answer2 = {
    "1" : "About 55",
    "2" : "About 65",
    "3" : "About 75",
    "4" : "About 85",
}


print("Answer the following algebra question : ")
print("If x = 8, then what  is the value  of 4(x + 3)  ?")
correct = 0
for k,v in Answer1.items():
    print(k,"." , v)
n = int(input("Your Choice : "))
if n == 4:
    print("Bingo")
    correct +=1
else:
    print(" :( ")

print("Estimate this answer (exact caculation not needed) : ")
print("Jack scored these marks in 5 math test: 49, 81, 72, 66 and 52. What is the mean ? ")
for k,v in Answer2.items():
    print(k,"." , v)
n = int(input("Your Choice : "))
if n ==2:
    print("Bingo")
    correct +=1
else:
    print(" :( ")

print("You correct anwser",correct,"out of 2 question")