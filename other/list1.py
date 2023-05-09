#CREATING A LIST
fruits=['apples','orange','banana','grape']
price=[200,150,60,60]
items=['laptop',25000,'phone',30000,'desk',1234.32]

#ACCESSING LIST ITEMS
print("My fav fruit is:", fruits[0])
print ("price of a dozen apples :",price[0])
print("I purchased 6",fruits[1],"for",price[1])

#REPLACING LIST ITEMS
fruits[2]='Lemon'
print(fruits)
items[0:4]=['desktop',10000,'ipad',55000]
print(items)
price[2]=150
print(price)

#ADDING ITEMS TO LIST
fruits.append('watermelon')
print("updated fruits list",fruits)

price.extend([234,324,123])
print("updated price list",price)

items.insert(0,"Printer")
print("updated items list",items)

#DELETING ITEMS FROM LIST

del fruits[4]
print(fruits)

del price[1:3]
print(price)

#del price
#print(price)


#REMOVE
print(fruits)
fruits.remove('apples')
print(fruits)

#POP
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

"""#CLEAR
fruits.clear()
items.clear()
del items
print(fruits)
print(items) """



























































