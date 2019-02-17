prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3,
}

stocks = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15,
}

total = 0
for k in prices.keys():
    print(k)
    print("prices : ", prices[k])
    print("stocks : ", stocks[k])
    total += prices[k] * stocks[k]
print(total)