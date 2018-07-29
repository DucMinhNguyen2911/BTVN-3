prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for i in prices:
    print(i,"Price:",prices[i],"Stock:",stock[i],sep='\n')
total = 0
b= prices['banana']*stock['banana']
a= prices['apple']*stock['apple']
o= prices['orange']*stock['orange']
p= prices['pear']*stock['pear']
total = b+a+o+p
print("Total $=",total)
