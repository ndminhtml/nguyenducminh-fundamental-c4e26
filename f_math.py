from random import randint, choice
#import calc
from calc import evalulate

print("***********")
x = randint(0,9)
y = randint(0,9)
pt = choice(["+", "-", "*", ":"])
error = randint(-1,1)
right = evalulate(x,y,pt)
r =  evalulate(x, y, pt)+ error


#string formating
print(f"{x} {pt} {y} = {r}")    #  = print(so1," + ", so2, "=", r)


answer = input("Y/N ? ")

if r == right and (answer == "Y"):
    print("Correct")
elif r == right and (answer == "N"):
    print("Wrong")
elif r !=right and (answer == "Y"):
    print("Wrong")
elif r !=right and (answer == "N"):
    print("Correct")