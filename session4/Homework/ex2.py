prices = {
    "banana":4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana":6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
print(prices,stock,sep="\n")

for i in prices.keys():
    print(i)
    print("price",prices[i],sep=": ")
    print("stock",stock[i],sep=": ")
    print("------------------------------")

total = 0
for j in prices.keys():
    total += prices[j]*stock[j] 
    print(j,prices[j]*stock[j],sep=": ")

print("------------------------------")
print("Total: ",total)